#version 120

#define ratio adsk_result_frameratio

vec3  adsk_hsv2rgb( vec3 hsv );
float adsk_getLuminance( vec3 );

uniform float ratio;
uniform float adsk_result_w, adsk_result_h;
vec2 res = vec2(adsk_result_w, adsk_result_h);
vec2 texel = vec2(1.0) / res;

uniform sampler2D adsk_results_pass1;
uniform sampler2D Front;
uniform sampler2D Matte;
uniform vec3 bg;

uniform int i_colorspace;
uniform bool usebg;

vec3 from_sRGB(vec3 col)
{
    if (col.r >= 0.0) {
         col.r = pow((col.r +.055)/ 1.055, 2.4);
    }

    if (col.g >= 0.0) {
         col.g = pow((col.g +.055)/ 1.055, 2.4);
    }

    if (col.b >= 0.0) {
         col.b = pow((col.b +.055)/ 1.055, 2.4);
    }

    return col;
}

vec3 from_rec709(vec3 col)
{
    if (col.r < .081) {
         col.r /= 4.5;
    } else {
         col.r = pow((col.r +.099)/ 1.099, 1.0 / .45);
    }

    if (col.g < .081) {
         col.g /= 4.5;
    } else {
         col.g = pow((col.g +.099)/ 1.099, 1.0 / .45);
    }

    if (col.b < .081) {
         col.b /= 4.5;
    } else {
         col.b = pow((col.b +.099)/ 1.099, 1.0 / .45);
    }

    return col;
}

vec3 to_rec709(vec3 col)
{
    if (col.r < .018) {
         col.r *= 4.5;
    } else if (col.r >= 0.0) {
         col.r = (1.099 * pow(col.r, .45)) - .099;
    }

    if (col.g < .018) {
         col.g *= 4.5;
    } else if (col.g >= 0.0) {
         col.g = (1.099 * pow(col.g, .45)) - .099;
    }

    if (col.b < .018) {
         col.b *= 4.5;
    } else if (col.b >= 0.0) {
         col.b = (1.099 * pow(col.b, .45)) - .099;
    }


    return col;
}

vec3 to_sRGB(vec3 col)
{
    if (col.r >= 0.0) {
         col.r = (1.055 * pow(col.r, 1.0 / 2.4)) - .055;
    }

    if (col.g >= 0.0) {
         col.g = (1.055 * pow(col.g, 1.0 / 2.4)) - .055;
    }

    if (col.b >= 0.0) {
         col.b = (1.055 * pow(col.b, 1.0 / 2.4)) - .055;
    }

    return col;
}

vec3 adjust_gamma(vec3 col, float gamma)
{
    col.r = pow(col.r, gamma);
    col.g = pow(col.g, gamma);
    col.b = pow(col.b, gamma);

    return col;
}

vec3 do_colorspace(vec3 front, int op)
{
    if (op == 0)
    {
        if (i_colorspace == 0) {
            front = from_rec709(front);
        } else if (i_colorspace == 1) {
            front = from_sRGB(front);
        } else if (i_colorspace == 2) {
            //linear
        } else if (i_colorspace == 3) {
            front = adjust_gamma(front, 2.2);
        } else if (i_colorspace == 4) {
            front = adjust_gamma(front, 1.8);
        }
    }
    else if (op == 1)
    {
        if (i_colorspace == 0) {
            front = to_rec709(front);
        } else if (i_colorspace == 1) {
            front = to_sRGB(front);
        } else if (i_colorspace == 2) {
            //linear
        } else if (i_colorspace == 3) {
            front = adjust_gamma(front, 2.2);
        } else if (i_colorspace == 4) {
            front = adjust_gamma(front, 1.8);
        }
    }

    return front;
}

vec3 getRGB( float hue, float sat)
{
    vec3 rgb =  adsk_hsv2rgb( vec3( hue, sat, 1.0 ) );

    rgb = clamp(rgb, 0.0, 1.0);

    return rgb;
}

void main(void) {
    vec2 st = gl_FragCoord.xy / res;
    vec3 front = texture2D(Front, st).rgb;
    float matte = texture2D(Matte, st).r;

    vec3 b_offset = getRGB( bg.x / 360.0, bg.z * .01 ) * vec3( bg.y * 0.01);
    vec3 bgcol = b_offset;

    front = do_colorspace(front, 0);

    vec4 shape = vec4(0.0);

    for (int i = -1; i <= 1; i++)
    {
        for (int j = -1; j <= 1; j++)
        {
            shape += texture2D(adsk_results_pass1, st + texel * vec2(i, j));
        }
    }

    shape /= vec4(9.0);


    float a = clamp(shape.a, 0.0, 1.0);

    shape.rgb /= vec3(max(shape.a, .0000000001));
    shape.rgb = do_colorspace(shape.rgb, 0);

    vec3 comp = mix(front, shape.rgb, a);

    if (usebg) {
        comp = mix(bgcol, shape.rgb, a);
    }

    comp = mix(front, comp, matte);

    comp = do_colorspace(comp, 1);
    
    gl_FragColor = vec4(comp, shape.a);
}
