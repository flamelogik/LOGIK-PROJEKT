#version 120

#define ratio adsk_result_frameratio
#define center vec2(.5)
#define pi 3.1415926535897932384626433832795028841971693993751058209749445923078164062
#define samples 1

vec3  adsk_hsv2rgb( vec3 hsv );
float adsk_getLuminance( vec3 );

uniform float ratio;
uniform float adsk_result_w, adsk_result_h;
vec2 res = vec2(adsk_result_w, adsk_result_h);
vec2 texel = vec2(1.0) / res;

uniform float shape_size;
uniform int shape_sides;
uniform int num_shapes;
uniform float roundness;
uniform bool circle;

//uniform vec3 bg;
uniform vec3 fg;

uniform bool clamp_shape;

uniform float f;
uniform float rrr;
uniform float zzz;

uniform int i_colorspace;


vec3 adjust_gamma(vec3 col, float gamma)
{
    col.r = pow(col.r, gamma);
    col.g = pow(col.g, gamma);
    col.b = pow(col.b, gamma);

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


vec2 rotate(vec2 point, float r, vec2 c)
{
	mat2 rm = mat2(
		cos(r), -sin(r),
		sin(r), cos(r)
	);	

	point -= c;
	point.x *= ratio;
	point *= rm;
	point.x /= ratio;
	point += c;

	return point;
}

vec2 bary(vec2 pos, vec2 top, vec2 left, vec2 right)
{
	vec2 v0 = top - left;
	vec2 v1 = right - left;
	vec2 v2 = pos - left;

	float dot00 = dot(v0, v0);
    float dot01 = dot(v0, v1);
    float dot02 = dot(v0, v2);
    float dot11 = dot(v1, v1);
    float dot12 = dot(v1, v2);

    float id = 1.0 / (dot00 * dot11 - dot01 * dot01);
    float u = (dot11 * dot02 - dot01 * dot12) * id;
    float v = (dot00 * dot12 - dot01 * dot02) * id;

	/* 
		TRIVIA
		uv.x goes from bottom 0.0 to top 1.0
		bottom_edge = uv.x;

		 uv.y goes from left_edge 0.0 to bottom right corner 1.0
		left_edge = uv.y;

		right_edge = 1.0 - (uv.x + uv.y);
	*/

    return vec2(u,v);
}

vec2 in_tri(vec2 p1, vec2 p2, vec2 p3, vec2 p4)
{
	// get the barycentric coords to find boundary of the triangle 
	vec2 uv = bary(p1, p2, p3, p4);

	if (uv.x >= 0.0 && uv.y >= 0.0 && uv.x + uv.y < 1.0) {
		return uv;
	} else {
		if (uv.x >= 0.0 && uv.y >= 0.0) {
			uv = -uv;
		} else {
			uv = vec2(-1);
		}
		return uv;
	}
}

float get_angle(vec2 v1, vec2 v2)
{
	float angle = acos(dot(normalize(v1), normalize(v2)));

	return angle;
}

vec2 find_center(vec2 p1, vec2 p2, vec2 p3)
{
	vec2 cent = vec2( (p1.x + p2.x + p3.x) / 3.0, (p1.y + p2.y + p3.y) / 3.0);

	return cent;
}

float max3(float a1, float a2, float a3)
{
	return max(max(a1, a2), a3);
}

vec2 scale(vec2 p)
{
	return (p - center) * vec2(1.1) + center;
}

float draw_shape(vec2 point, vec2 top, vec2 left, vec2 right)
{
	float col = 0.0;

	// This is some hack to get rid of black edges inside some of the triangles
	top /= vec2(1.001);

	vec2 p = vec2(point.x * ratio, point.y);
	vec2 r = vec2(right.x * ratio, right.y);
	vec2 t = vec2(top.x * ratio, top.y);
	vec2 l = vec2(left.x * ratio, left.y);
	vec2 c = vec2(center.x * ratio, center.y);

	// Way above my paygrade here, trying to figure out how to round out the shape
	// got the outy, just not the inny (holes after 3 sides)
	// acos the dot product of 2 normalized vectors gives you the angle between the vectors
	// define some vector for easy recall
	vec2 vtl = vec2(t - l);
	vec2 vtr = vec2(t - r);

	vec2 vlt = vec2(l - t);
	vec2 vrt = vec2(r - t);

	vec2 vlr = vec2(l - r);
	vec2 vrl = vec2(r - l);

	vec2 vpl = vec2(p - l);
	vec2 vpt = vec2(p - t);
	vec2 vpr = vec2(p - r);

	vec2 vlp = vec2(l - p);

	vec2 vct = vec2(center - top);
	vec2 vcr = vec2(center - right);

	vec2 vlc = vec2(left - center);

    float theta_tpr = get_angle(vpt, vpr);
    float theta_tpl = get_angle(vpt, vpl);
    float theta_lpr = get_angle(vpl, vpr);

	float theta_plr = get_angle(vlp, vlr);

	float theta_tlr = get_angle(vlt, vlr);
	float theta_ltr = get_angle(vtl, vtr);
	float theta_trl = get_angle(vrt, vrl);

	float theta_tcr = get_angle(vct, vcr);

	// did this so I could get more stable values to compare length of edges
	float lt = floor(abs(length(t - l)) * 10);
	float rt = floor(abs(length(t - r )) * 10);
	float lr = floor(abs(length(l - r)) * 10);
	float cr = floor(abs(length(c - r)) * 10);

	float vmin = min(min(lt, rt), lr);
	float vmax = max(max(lt, rt), lr);

	// Get the midpoint of each edge of the triangle
	vec2 edge_center_left = vec2( (left.x + top.x) / 2.0, (left.y + top.y) / 2.0);
	vec2 edge_center_right = vec2( (right.x + top.x) / 2.0, (right.y + top.y) / 2.0);
	vec2 edge_center_bottom = vec2( (right.x + left.x) / 2.0, (right.y + left.y) / 2.0);

	// Scale them outwards to make an edge bend in or out 
	vec2 outer_center_left = (edge_center_left - center) * (rrr + .05) + center;
	vec2 outer_center_right = (edge_center_right - center) * (rrr + .05)  + center;
	vec2 outer_center_bottom = (edge_center_bottom - center) * (rrr + .05)  + center;

	float s = pi - abs(roundness);

	// Outer Spikes

	vec2 uvb = in_tri(point, center, left, right);
	vec2 uvb_o = in_tri(point, center, scale(left), scale(right));
	vec2 uvpb = in_tri(point, center, left, right);
	vec2 uvcb =in_tri(point, outer_center_bottom, left, right);

	vec2 uvl = in_tri(point, top, left, center);
	vec2 uvpl = in_tri(point, center, top, left);
	vec2 uvcl = in_tri(point, outer_center_left, left, top);

	vec2 uvr = in_tri(point, top, right, center);
	vec2 uvpr = in_tri(point, center, top, right);
	vec2 uvcr = in_tri(point, outer_center_right, right, top);

	bool bottom_out = false;
	bool left_out = false;
	bool right_out = false;


	// Outer spikes
	float oaa1 = .02;
	float oaa2 = .04;
	oaa1 = 0.01; //outer sharp edges
	oaa2 = 0.01; //outer round edges

	// Bottom Edge
	if (uvcb.x > 0.0  && uvpb.x < 0.0)
	{
		if (theta_lpr > s)
		{
			col = smoothstep(0.0, oaa1, min(uvcb.y, 1.0 - (uvcb.x + uvcb.y)));
			float d =  abs(theta_lpr - s);
			col = min(col, smoothstep(0.0, oaa2, d));
		}
	}
	// Left Edge
	else if (uvcl.x > 0.0 && uvpl.x < 0.0 && shape_sides <= 4)
	{
		if (theta_tpl > s)
		{
			col = smoothstep(0.0, oaa1, min(uvcl.y, 1.0 - (uvcl.x + uvcl.y)));
			float d =  abs(theta_tpl - s);
			col = min(col, smoothstep(0.0, oaa2, d));
		}

	}
	else if (uvcl.x > 0.0 && uvpl.x < 0.0 && shape_sides > 4 && lt == vmin && (point.x < center.x || point.x < right.x || point.y < right.y))
	{
		if (theta_tpl > s)
		{
			col = smoothstep(0.0, oaa1, min(uvcl.y, 1.0 - (uvcl.x + uvcl.y)));
			float d =  abs(theta_tpl - s);
			col = min(col, smoothstep(0.0, oaa2, d));
		}
	}
	// Right Edge
	else if (uvcr.x > 0.0 && uvpr.x < 0.0 && shape_sides <= 4)
	{
		if (theta_tpr > s)
		{
			col = smoothstep(0.0, oaa1, min(uvcr.y, 1.0 - (uvcr.x + uvcr.y)));
			float d =  abs(theta_tpr - s);
			col = min(col, smoothstep(0.0, oaa2, d));
		}
	}
	else if (uvcr.x > 0.0 && uvpr.x < 0.0 && shape_sides > 4 && rt == vmin && ((right.y > center.y && right.x > center.x) || point.x > top.x) )
	{
		if (theta_tpr > s)
		{
			col = smoothstep(0.0, oaa1, min(uvcr.y, 1.0 - (uvcr.x + uvcr.y)));
			float d =  abs(theta_tpr - s);
			col = min(col, smoothstep(0.0, oaa2, d));
		}
	}

	// Core Shape + Inner spikes
	// Bottom Edge
	float aa1 = .03;
	float aa2 = .1;
	float aa3 = 100;

	aa1 = 0.01;
	aa2 = 0.05;
	aa3 = 200.0; //Inner curve higher number is sharper edge
	if (lr == vmin &&  uvb.x > 0.0)
	{
		col = smoothstep(0.0, aa1, uvb.x);

		// Spikes
		if (theta_lpr > s)
		{
			float edge = 1.0 - aa2 / theta_lpr;
			float d = 1.0 - (theta_lpr - s);
			col = smoothstep(edge, 1.0, d);

			vec2 aae = uvcb;
			d = max(1.0 - aae.y, aae.x + aae.y);
			col = max(col, mix(col, d, 1.0 - clamp(aa3 * (1.0 - d), 0.0, 1.0)));
		}
	}
	// Left Edge
	else if (uvl.y > 0.0 && lr == vmin && lt == vmin)
	{
		col = smoothstep(0.0, aa1, uvl.y);

		// Spikes
		if (theta_tpl > s)
		{
			float edge = 1.0 - aa2 / theta_tpl;
			float d = 1.0 - (theta_tpl - s);
			col = smoothstep(edge, 1.0, d);

			vec2 aae = uvcl;
			d = max(1.0 - aae.y, aae.x + aae.y);
			col = max(col, mix(col, d, 1.0 - clamp(aa3 * (1.0 - d), 0.0, 1.0)));
		}
	} 
	// Right Edge
	else if (uvr.y > 0.0 && point.x > top.x && lr == vmin && rt == vmin)
	{
		col = smoothstep(0.0, aa1, uvr.y);

		// Spikes
		if (theta_tpr > s)
		{
			float edge = 1.0 - aa2 / theta_tpr;
			float d = 1.0 - (theta_tpr - s);
			col = smoothstep(edge, 1.0, d);

			vec2 aae = uvcr;
			d = max(1.0 - aae.y, aae.x + aae.y);
			col = max(col, mix(col, d, 1.0 - clamp(aa3 * (1.0 - d), 0.0, 1.0)));
		}
	}

	col = clamp(col, 0.0, 1.0);

	return col;
}

vec3 getRGB( float hue, float sat)
{
    vec3 rgb =  adsk_hsv2rgb( vec3( hue, sat, 1.0 ) );

    rgb = clamp(rgb, 0.0, 1.0);

    return rgb;
}


void main(void) {
	vec2 st = gl_FragCoord.xy / res;

	float shape = 0.0;

 	vec3 f_offset = getRGB( fg.x / 360.0, fg.z * .01 ) * vec3( fg.y * 0.01);
    vec3 fgcol = f_offset;

    //vec3 b_offset = getRGB( bg.x / 360.0, bg.z * .01 ) * vec3( bg.y * 0.01);
    //vec3 bgcol = b_offset;

	vec3 comp = vec3(0.0);

	float size = shape_size + .015;
	int sides = shape_sides;

	float shapes = float(num_shapes);

	// The top is always the same point
	vec2 top = vec2(center.x, center.y + size);

	// Make sure to cast the angles before the divide
	float angle = float(360) / float(sides);
	float shape_angle = angle / float(num_shapes);

	// Convert to radians
	angle = angle * pi / 180.0;
	shape_angle = shape_angle * pi / 180.0;

	// left and right change, after one triangle is made, the left becomes the right, and the
	// right rotates by the angle to become the new right
	vec2 left = rotate(top, angle, center);
	vec2 right = rotate(top, angle * 2.0, center);

	// number of triangles it takes to make a shape with n sides 
	int num_tri = sides - 2;

	float col;

	if (shape_size == 0.0)
	{
		col = 0.0;
	} else if (circle) {
		st.x *= ratio;
		float dist = distance(st, vec2(.5 * ratio, .5));
		col = 1.0 - smoothstep(shape_size, shape_size + 2.0 * texel.x, dist);

		//comp = mix(bgcol, fgcol, col);
		comp = mix(vec3(0.0), fgcol, col);
		shape = col;
	}
	else
	{
		for (float the_shape = 1.0; the_shape <= shapes; the_shape++)
		{
			// Draw one shape (potentially many triangles)
			for (int triangle = 0; triangle < num_tri; triangle++)
			{

				// hack
				vec2 t = top;
				vec2 l = left;
				vec2 r = right;

				col += draw_shape(st, t, l, r);
				col += draw_shape(st, t + texel, l + texel, r + texel);
				col += draw_shape(st, t - texel, l - texel, r - texel);

				left = right;
				right = rotate(right, angle, center);
	
				col = clamp(col, 0.0, 1.0);
			}
	
			shape += col;

			top = rotate(top, shape_angle, center);
			left = rotate(top, angle, center);
			right = rotate(top, angle * 2.0, center);

			col = clamp(col, 0.0, 1.0);

			if (the_shape == 1.0)
			{
				comp = mix(vec3(0.0), fgcol, col);
			} 
			else
			{
				if (clamp_shape)
				{
					comp = mix(comp, fgcol, col);
				}
				else
				{
					comp = mix(comp, fgcol * vec3(the_shape), col);
				}
			}

			col = 0.0;
		}
	}

	shape = clamp(shape, 0.0, 1.0);

	gl_FragColor = vec4(comp, shape);
}
