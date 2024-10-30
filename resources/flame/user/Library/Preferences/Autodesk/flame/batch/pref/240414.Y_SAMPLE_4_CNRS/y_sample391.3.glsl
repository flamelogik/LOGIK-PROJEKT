#version 120
#extension GL_ARB_shader_texture_lod : enable

#define ratio adsk_result_frameratio
#define edge .15

uniform float ratio;
uniform float adsk_result_w, adsk_result_h;
vec2 res = vec2(adsk_result_w, adsk_result_h);
vec2 texel = vec2(1.0) / res;

uniform sampler2D adsk_results_pass1;
uniform sampler2D adsk_results_pass2;

uniform vec2 pos;
uniform vec3 a_pos;
uniform bool col_only;
uniform float lod;
uniform bool action_coords;

vec4 preview(vec2 point, vec2 p, vec3 col, vec3 mm)
{
	float window = 0.0;
	float alpha = 0.0;
	vec3 ret_col = vec3(0.0);

	p.x *= ratio;
	point.x *= ratio;

	float d = distance(point, p);

	if (d < edge)
	{
		// Window Boundary
		alpha = smoothstep(edge, edge - .002, d);

		// Make window black border
		float inner = smoothstep(edge - .002, edge - .004, d);

		// Mix front into Window
		ret_col = mix(ret_col, mm, inner);

		if (point.x > p.x)
		{
			inner = smoothstep(edge - .006, edge - .008, d);

			// Mix picked Color into right side of window
			ret_col = mix(ret_col, col, inner);
		}
	}

	return vec4(ret_col, alpha);
}

void main(void) {
	vec2 st = gl_FragCoord.xy / res;
	vec4 front = texture2D(adsk_results_pass1, st);

	vec3 col = vec3(.3, .7, .6);
	vec4 window = vec4(0.0);

	vec2 p = pos;

	if (action_coords)
	{
		p = a_pos.xy;
		p = p / res + .5;
	}

	col = texture2DLod(adsk_results_pass2, p, lod).rgb;

	if (col_only)
	{
		front.rgb = col;
		window.a = 1.0;
	}
	else
	{
		vec3 scaled_front = texture2DLod(adsk_results_pass2, st, lod).rgb;

		window = preview(st, p, col, scaled_front);

		front.rgb = mix(front.rgb, window.rgb, window.a);
	}

	gl_FragColor = vec4(front.rgb, window.a);
}
