#version 120
#extension GL_ARB_shader_texture_lod : enable

vec2 center = vec2(.5);

uniform float adsk_time, adsk_result_w, adsk_result_h, adsk_result_frameratio;
vec2 res = vec2(adsk_result_w, adsk_result_h);
float time = adsk_time *.05;

uniform sampler2D adsk_results_pass1, adsk_results_pass2, adsk_results_pass3, adsk_results_pass4, adsk_results_pass5;

// Global Uniforms
uniform int process;
uniform int result;
uniform bool ssat;
uniform bool slum;
uniform bool shue;

//Color Uniforms
uniform bool show_swatch;
uniform vec2 swatch_center;
uniform float swatch_size;
uniform bool show_palette;
uniform float palette_detail;
uniform vec3 color;

//Noise Uniforms
uniform bool static_noise;
uniform bool color_noise;
uniform float zoom;
uniform float cells;

//Checkerboard Uniforms
uniform vec3 cb_color1, cb_color2;
uniform float checkerboard_freq;
uniform float cb_aspect;
uniform bool show_cbpalette;
uniform float cbpalette_detail;

//Colorbars Uniforms
uniform int colorbars_type;
uniform int colorbars_p;
uniform int colorbars_softness;
uniform bool blue_only;

//Colorwheel Uniforms
uniform vec2 cw_center;
uniform float cw_size;
uniform float cw_val;
uniform float cw_aspect;

//Grad Uniforms
uniform int grad_type;
uniform int grad_fit;
uniform bool show_gpalette;
uniform float gpalette_detail;
uniform vec3 grad_color1;
uniform vec3 grad_color2;
uniform bool grad_rev;

//Shape
float softness = 0.0;

uniform int sides;
uniform int num_shapes;
uniform float shape_aspect;
uniform float shape_size;
uniform vec2 shape_offset;
uniform float shape_rotation;
uniform vec3 shape_color1;
uniform vec3 shape_color2;
uniform bool clamp_shape;

//Grid
uniform float g_sizeProp, g_lineProp, g_rotation, g_line;
uniform bool g_propwidth, g_propgridsize, g_invert;
uniform vec2 g_size;
uniform vec3 g_gridcolor, g_backcolor;

// Chrome Uniforms
uniform vec2 chrome_center;
uniform float chrome_zoom, chrome_detail, chrome_speed, chrome_offset;
uniform bool static_chrome;
uniform int chrome_type;
float chrome_time = time *.5 * chrome_speed + 200. + chrome_offset;




vec2 texel = vec2(1.0) / res;
const vec3 lum_c = vec3(0.2125, 0.7154, 0.0721);

const vec3 white = vec3(1.0);
const vec3 black = vec3(0.0);
const vec3 red = vec3(1.0, 0.0, 0.0);
const vec3 green = vec3(0.0, 1.0, 0.0);
const vec3 blue = vec3(0.0, 0.0, 1.0);
const vec3 cyan = white - red;
const vec3 magenta = white - green;
const vec3 yellow = white - blue;

bool isInTex( const vec2 coords )
{
   return coords.x >= 0.0 && coords.x <= 1.0 &&
          coords.y >= 0.0 && coords.y <= 1.0;
}

//CIRCLE
float draw_circle(vec2 st, vec2 center, float size, float aspect)
{
	vec2 v2 = center - (center + vec2(size));
	v2.x *= adsk_result_frameratio;
	vec2 v3 = center - st;
	v3.x *= adsk_result_frameratio;
	v3.x /= aspect;

    float circle =  1.0 - smoothstep(length(v2) - .005, length(v2), length(v3));

    return circle;
}

vec3 rgb2hsv(vec3 c)
{
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}

vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

//PALETTE
vec4 make_palette(vec2 st)
{
	vec2 coords = (st - vec2(.5)) / .65 + .5;

	vec4 palette;
   	if (isInTex(coords)) {
    	palette = texture2DLod(adsk_results_pass5, coords , palette_detail);


   		if (st.x < .2) {
       		palette.rgb -= .5;
       		palette = clamp(palette, 0.0, 1.0);
  		}

   		float thresh = .93;
   		if (palette.r > thresh && palette.g > thresh && palette.b > thresh) {
      		palette.rgb = white;
  		}
	}

	return palette;
}


float mag(vec2 v) {
    // find the magnitude of a vector
    return sqrt(v.x * v.x + v.y * v.y);
}

float get_angle(vec2 center_to_point2, vec2 coords_from_center)
{
    float angle = acos(dot(center_to_point2, coords_from_center) / (mag(center_to_point2) * mag(coords_from_center)));

    return angle;
}

//COLORWHEEL
vec3 colorwheel(vec2 st) {
	vec2 v2 = cw_center - vec2(cw_center.x - .01, cw_center.y);
	v2.x *= adsk_result_frameratio;

	vec2 v3 = cw_center - st;
	v3.x *= adsk_result_frameratio;

	vec2 v4 = cw_center - vec2(cw_center.x - cw_size * .25, cw_center.y);
	v4.x *= adsk_result_frameratio;

	float rad = distance(v4, v2);
	float d = distance(v3, v2);
	

	float angle_in_radians = get_angle(v2, v3);
	float circle = draw_circle(st, cw_center, cw_size * .25, cw_aspect);

	float angle_in_degrees = degrees(angle_in_radians);

	 if (cross(vec3(v2, 0.0), vec3(v3, 0.0)).z < 0.0) {
        angle_in_degrees = 360.0 - angle_in_degrees;
    }

	vec3 col = vec3(angle_in_degrees / 360.0);
	col.g =  d / rad;
	col.b = cw_val;

	col = hsv2rgb(col) * vec3(circle);
	col = clamp(col, 0.0, 1.0);

	return col;
}

//OVERLAYS
vec3 make_overlays(vec2 st, vec3 front, bool show_p, bool show_s)
{
	vec4 palette = vec4(0.0);
	float swatch = 0.0;
	vec3 col;

	if (result == 0) {
       	col = front;
       	if (show_p) {
         	palette = make_palette(st);
       	}

       	if (show_s) {
         	swatch = draw_circle(st, swatch_center, swatch_size * .25, 1.0);
     	}

       	col = mix(col, palette.rgb, palette.a);
       	col = mix(col, vec3(color), swatch);
  	}

	return col;
}

//SCALE
vec2 scale(vec2 st, float scale_amnt, float aspect) {
	st -= vec2(.5);
	st.x *= aspect * adsk_result_frameratio;
	st /= scale_amnt;
	st += vec2(.5);

	return st;
}

float luminance(vec3 col) {
	return clamp(dot(col, lum_c), 0.0, 1.0);
}

//NOISE
float rand2(vec2 co) 
{
	return fract(sin(dot(co.xy,vec2(12.9898,78.233))) * 43758.5453);
}

vec3 noise(vec2 st) {
	vec2 c = (cells/100.*res.x)*vec2(1.,res.y/res.x);
	vec3 col = vec3(0.0);

    if ( static_noise )
    {
     	time = 1.0;
	}

   	float r = rand2(vec2((2.+time) * floor(st.x*c.x)/c.x, (2.+time) * floor(st.y*c.y)/c.y ));
   	float g = rand2(vec2((5.+time) * floor(st.x*c.x)/c.x, (5.+time) * floor(st.y*c.y)/c.y ));
   	float b = rand2(vec2((9.+time) * floor(st.x*c.x)/c.x, (9.+time) * floor(st.y*c.y)/c.y ));

   	col = vec3(r,r,r);

   	if (color_noise )
   	{
   		col = vec3(r,g,b);
   	}

	return col;
}

//CHECKERBOARD
vec3 checkerboard(vec2 st, vec3 first, vec3 second)
{
	vec2 p = scale(st, checkerboard_freq * .1, cb_aspect);
	return mix(first, second, max(0.0, sign(sin(p.x)) * sign(sin(p.y))));
}

//SMPTE2
vec3 smpte2_colorbars(vec2 st)
{
	vec3 col = black;

	if (st.x < 1.0 / 7.0 * 1.0) {
		col = blue;
	} else if (st.x < 1.0 / 7.0 * 2.0) {
		col = black;
	} else if (st.x < 1.0 / 7.0 * 3.0) {
		col = magenta;
	} else if (st.x < 1.0 / 7.0 * 4.0) {
		col = black;
	} else if (st.x < 1.0 / 7.0 * 5.0) {
		col = cyan;
	} else if (st.x < 1.0 / 7.0 * 6.0) {
		col = black;
	} else if (st.x < 1.0 / 7.0 * 7.0) {
		col = white;
	}

	colorbars_p == 0 ? col *= vec3(.75) : col;

	return col;
}

//SMPTE
vec3 smpte_colorbars(vec2 st)
{
	vec3 col = black;

	if (st.y < 1.0 / 4.0) {
		if (st.x < 1.0 / 6.0 * 1.0) {
			col = vec3(0.0, 0.11761, 0.47827);
			colorbars_p == 0 ? col *= vec3(.5) : col;
		} else if (st.x < 1.0 / 6.0 * 2.0) {
			col = white;
		} else if (st.x < 1.0 / 6.0 * 3.0) {
			col = vec3(0.2666, 0.0, 0.54492);
			if (colorbars_p == 0) {
				col.r *= .5;
				col.b *= .676081;
			}
		} else if (st.x < 1.0 / 6.0 * 4.0) {
			col = black;
		} else if (st.x < 1.0 / 6.0 * 5.0) {
			col = vec3(.03922);
		} else if (st.x < 1.0 / 6.0 * 6.0) {
			col = black;
		}
	} else {
		if (st.x < 1.0 / 7.0 * 1.0) {
			col = white;
		} else if (st.x < 1.0 / 7.0 * 2.0) {
			col = yellow;
		} else if (st.x < 1.0 / 7.0 * 3.0) {
			col = cyan;
		} else if (st.x < 1.0 / 7.0 * 4.0) {
			col = green;
		} else if (st.x < 1.0 / 7.0 * 5.0) {
			col = magenta;
		} else if (st.x < 1.0 / 7.0 * 6.0) {
			col = red;
		} else if (st.x < 1.0 / 7.0 * 7.0) {
			col = blue;
		}

		colorbars_p == 0 ? col *= vec3(.75) : col;
	}

	return col;
}

//PAL
vec3 pal_colorbars(vec2 st)
{
	vec3 col = black;
	int allon = 0;

	if (st.y < 1.0 / 4.0) {
		if (st.x < 1.0 / 8.0 * 1.0) {
			col = white;
			colorbars_p == 0 ? col *= vec3(.75) : col;
		} else if (st.x < 1.0 / 8.0 * 2.0) {
			col = vec3(.88232);
			colorbars_p == 0 ? col = vec3(.66260) : col;
		} else if (st.x < 1.0 / 8.0 * 3.0) {
			col = vec3(.69775);
			colorbars_p == 0 ? col = vec3(.52539) : col;
		} else if (st.x < 1.0 / 8.0 * 4.0) {
			col = vec3(.58398);
			colorbars_p == 0 ? col = vec3(.43921) : col;
		} else if (st.x < 1.0 / 8.0 * 5.0) {
			col = vec3(.41162);
			colorbars_p == 0 ? col = vec3(.30566) : col;
		} else if (st.x < 1.0 / 8.0 * 6.0) {
			col = vec3(.29785);
			colorbars_p == 0 ? col = vec3(.22351) : col;
		} else if (st.x < 1.0 / 8.0 * 7.0) {
			col = vec3(.11371);
			colorbars_p == 0 ? col = vec3(.08234) : col;
		} else if (st.x < 1.0 / 8.0 * 8.0) {
			col = black;
		}
	} else {
		if (st.x < 1.0 / 8.0 * 1.0) {
			col = white;
		} else if (st.x < 1.0 / 8.0 * 2.0) {
			col = yellow;
			colorbars_p == 0 ? col *= vec3(.75) : col;
		} else if (st.x < 1.0 / 8.0 * 3.0) {
			col = cyan;
			colorbars_p == 0 ? col *= vec3(.75) : col;
		} else if (st.x < 1.0 / 8.0 * 4.0) {
			col = green;
			colorbars_p == 0 ? col *= vec3(.75) : col;
		} else if (st.x < 1.0 / 8.0 * 5.0) {
			col = magenta;
			colorbars_p == 0 ? col *= vec3(.75) : col;
		} else if (st.x < 1.0 / 8.0 * 6.0) {
			col = red;
			colorbars_p == 0 ? col *= vec3(.75) : col;
		} else if (st.x < 1.0 / 8.0 * 7.0) {
			col = blue;
			colorbars_p == 0 ? col *= vec3(.75) : col;
		} else if (st.x < 1.0 / 8.0 * 8.0) {
			col = black;
			colorbars_p == 0 ? col *= vec3(.75) : col;
		}
	}

	return col;
}

//COLORBARS
vec3 colorbars(vec2 st) 
{
	vec3 bars;
	if (colorbars_type == 0) {
		bars = smpte_colorbars(st);
	} else if (colorbars_type == 1) {
		bars = pal_colorbars(st);
	} else if (colorbars_type == 2) {	
		bars = smpte_colorbars(st);
		if (st.y > .25 && st.y < .35) {
			bars = smpte2_colorbars(st);
		}
	}

	if (blue_only) {
		bars.rg = vec2(bars.b);
	}

	return bars;
}

//GRAD
vec4 gradient(vec2 st) {
	vec3 col = vec3(st.x);

	vec3 c1 = grad_color1;
	vec3 c2 = grad_color2;

	if (grad_rev) {
		vec3 t = c1;
		c1 = c2;
		c2 = t;
	}

	if (grad_type == 1) {
		col = vec3(st.y);
	} else if (grad_type == 2) {
		st -= vec2(.5);
		if (grad_fit == 0) {
			st.x *= adsk_result_frameratio;
			st /= .5;
		} else if (grad_fit == 2) {
			st /= .5;
		} else if (grad_fit == 1) {
			st.y /= adsk_result_frameratio;
			st /= .5;
		}

		st += vec2(.5);
		col = vec3(1.0 - distance(vec2(.5), st));
	}

	float a = col.r;
	col = mix(c2, c1, col);
	
	return vec4(col, a);
}


//GRID
vec3 grid(vec2 position)
{
	vec3 col = vec3(0.0);
	mat2 rotationMatrice = mat2( cos(-g_rotation), -sin(-g_rotation), sin(-g_rotation), cos(-g_rotation) );
   	position -= vec2(0.5, 0.5);
   	position.x *= adsk_result_frameratio;
   	position *= rotationMatrice;
   	position.x /= adsk_result_frameratio;
   	position += vec2(0.5, 0.5);
   	vec3 color1 = g_gridcolor;
	vec3 color2 = g_backcolor;
	
	if ( g_invert )
	{
		vec3 colorTemp;
		colorTemp = g_gridcolor;
		color1 = g_backcolor;
		color2 = colorTemp;
	}
   	if(mod(position.x, g_size.x / 10.0) <= g_line / adsk_result_w)
   	{
            col = color1;
   	}
   	else if(mod(position.y, g_size.y / 10.0) <= g_line / adsk_result_h)
   	{
            col = color1;
   	}
   	else
   	{
            col = color2;
   	}

	return col;
}

mat2 get_matrix(float angle)
{

    float r = radians(angle);

    mat2 rotationMatrice = mat2(
                                 cos(r),
                                -sin(r),
                                 sin(r),
                                 cos(r)
                            );


    return rotationMatrice;
}

vec2 bary(vec2 pos, vec2 top, vec2 left,vec2  right)
{

    top -= center;
    top.x *= shape_aspect;
    top += center;
    left -= center;
    left.x *= shape_aspect;
    left += center;
    right -= center;
    right.x *= shape_aspect;
    right += center;

    top += shape_offset;
    left += shape_offset;
    right += shape_offset;

    vec2 v0 = top - left;
    vec2 v1 = right - left;
    vec2 v2 = pos - left;

    float dot00 = dot(v0, v0);
    float dot01 = dot(v0, v1);
    float dot02 = dot(v0, v2);
    float dot11 = dot(v1, v1);
    float dot12 = dot(v1, v2);

    float invDenom = 1.0 / (dot00 * dot11 - dot01 * dot01);
    float u = (dot11 * dot02 - dot01 * dot12) * invDenom;
    float v = (dot00 * dot12 - dot01 * dot02) * invDenom;

    return vec2(u,v);
}

vec2 rotate_shape(vec2 st, vec2 shape_p, float rot)
{
    shape_p -= center;
    shape_p.x *= adsk_result_frameratio;
    shape_p *= get_matrix(rot);
    shape_p.x /= adsk_result_frameratio;
    shape_p += center;

    return shape_p;
}

float draw_shape(vec2 st, vec2 top)
{
    float col = 0.0;

    //vec2 top = vec2(.5, .5 + shape_size * .5);

    //Works from here
   
    vec2 shape[60];

    shape[0] = top;
    shape[0] -= center;
    shape[0].x *= adsk_result_frameratio;

    float a;

    for (int i = 1; i <= sides; i++) {
        a = 360 / float(sides) * float(i);

        shape[i] = shape[0] * get_matrix(a);

        shape[i].x /= adsk_result_frameratio;
        //shape[i].x *= shape_aspect;
        shape[i] += center;

    }

    shape[0].x /= adsk_result_frameratio;
    shape[0] += center;

    if (sides < 3) {
        return 1.0;
    }

    float s = softness * .001;

    for (int i = 0; i < sides - 1 ; i++) {
        vec2 top = rotate_shape(st, shape[i], shape_rotation);
        vec2 left = rotate_shape(st, shape[i+1], shape_rotation);
        vec2 right = rotate_shape(st, shape[i+2], shape_rotation);

        vec2 uv = bary(st, top, left, right);

        if (uv.x >= 0.0 && uv.y >= 0.0 && uv.x + uv.y < 1.0) {
            col += 1.0;
        }

        if (uv.x > 0.0 && uv.x < s) { // bottom side
                col *= smoothstep(0.0, s, uv.x);
            }

            if (uv.y < s && uv.y > 0.0) { // left side
                col *= smoothstep(0.0, s, uv.y);
            }

            if (uv.x + uv.y < 1.0 && uv.x + uv.y > 1.0 - s) {
                col *= 1.0 - smoothstep(1.0 - s, 1.0, uv.x + uv.y); // right size
            }


        col = clamp(col, 0.0, 1.0);

        if (sides > 4) {
            vec2 top = rotate_shape(st, center, shape_rotation);
            vec2 left = rotate_shape(st, shape[i], shape_rotation);
            vec2 right = rotate_shape(st, shape[i+2], shape_rotation);

            uv = bary(st, top, left, right);

            if (uv.x >= 0.0 && uv.y >= 0.0 && uv.x + uv.y < 1.0) {
                col += 1.0;
            }

        col = clamp(col, 0.0, 1.0);
        }
    }



    return col;
}

vec4 multi_shape(vec2 st)
{
    float shape = 0.0;
    float angle_offset = 1.0 / float(num_shapes);
    float shape_angle = 360.0 / float(sides) * angle_offset;
    vec2 top = vec2(.5, .5 + shape_size * .5);


    for (int i = 1; i <= num_shapes; i++) {
        shape += draw_shape(st, top);
        top = rotate_shape(st, top, shape_angle);
    }

    if (clamp_shape) {
        shape = clamp(shape, 0.0, 1.0);
    }

    vec3 color_out = mix(shape_color1, shape_color2, shape);

	return vec4(color_out, shape);
}

vec3 chrome(vec2 p)
{
	if (chrome_type == 0) {
		for(int i=1;i<12;i++)
		{
			vec2 newp=p;
			if ( static_chrome )
				chrome_time = chrome_offset + 200.;
			newp.x+=1./float(i)*sin(float(i)* chrome_detail/2.2 *p.y+chrome_time*.1)+1.;
			newp.y+=1./float(i)*cos(float(i)* chrome_detail/2.2 *p.x+chrome_time*.1)-1.;
			p=newp;
		}
		vec3 col= vec3(sin(p.x+p.y)*.5 + .5);
		return col;
		
	} else if (chrome_type == 1) {	
		int iter = int(7 * chrome_detail);
		p = p * .5;
		vec2 i = p;
		float c = 0.0;
		float inten = 1.0;

		for (int n = 0; n < iter; n++) 
		{
			float t = (chrome_time * .1 * (1.0 - (1.0 / float(n+1)))) + 20.;
			if ( static_chrome )
				chrome_time = chrome_offset + 200;
			i = (p + vec2(cos(t - i.x) + sin(t + i.y), sin(t - i.y) + cos(t + i.x))) - (i - (1.0 / vec2(n+1)));
			c += 1.0/length((p*i) / vec2(sin(i.x + t)/inten, cos(i.y + t) / inten));
		}
		c /= float(iter);
		c = smoothstep (0.00001, 1., c);
		vec3 col = vec3(c);
		return col;
	}
}


void main(void)
{
	vec2 st = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);
	vec3 front = texture2D(adsk_results_pass1, st).rgb;

	// Default output is solid color
	vec3 col = vec3(color);
	float matte_out = luminance(col);

	if (process == 0) {

		/* 
		make_overlays will create the palette and the swatch depending on the arguments.
		The first argument is the uvs, the second is what you want under the overlays.
		In the case of the color mode I want it over the front input. But other modes probably
		it would go over whatever was being generated. The last 2 arguments are uniform bools
		wether or not to show the palette and the swatch. Each mode needs to have its own
		unique bools
		*/

		col = make_overlays(st, front, show_palette, show_swatch);
	} else if (process == 1) {
		col = noise(st);
		matte_out = luminance(col);
	} else if (process == 2) {
		col = checkerboard(st, cb_color1, cb_color2);
		matte_out = checkerboard(st, white, black).r;
		col = make_overlays(st, col, show_cbpalette, false);
	} else if (process == 3) {
		col = colorbars(st);
		matte_out = luminance(col);
	} else if (process == 4) {
		col = colorwheel(st);
		matte_out = draw_circle(st, cw_center, cw_size * .25, cw_aspect);
	} else if (process == 5) {
		vec4 tmp = gradient(st);
		col.rgb = tmp.rgb;
		matte_out = tmp.a;
		matte_out = luminance(col);
		col = make_overlays(st, col, show_gpalette, false);
	} else if (process == 6) {
		//SHAPE
		vec4 tmp = multi_shape(st);
		col = tmp.rgb;
		matte_out = tmp.a;
	} else if (process == 7) {
		col = grid(st);
		matte_out = col.r;
	} else if (process == 8) {
		col = vec3(st.r, st.g, 0.0);
	} else if (process == 9 ) {
		vec2 p = 10. * (((gl_FragCoord.xy / res.xy) - 0.5) * chrome_zoom) + chrome_center;
		col = chrome(p);
	}
	
	if (result == 1)
		col = color;
	if (result == 2) {
		float matte = texture2D(adsk_results_pass3, st).r;
		col = mix(front, col, matte);
	} else if (result == 3) {
		float matte = texture2D(adsk_results_pass3, st).r;
		vec3 back = texture2D(adsk_results_pass2, st).rgb;
		col = mix(back, col, matte);
	}

	float strength = texture2D(adsk_results_pass4, st).r;
	if (ssat) {
		col = rgb2hsv(col);
		col.g = clamp(col.g - strength, 0.0, 1.0);
		col = hsv2rgb(col);
	}

	if (shue) {
		col = rgb2hsv(col);
		col.r += strength;
		col = hsv2rgb(col);
	}

	if (slum) {
		col *= vec3(strength);
	}

	gl_FragColor = vec4(col, matte_out);
}
