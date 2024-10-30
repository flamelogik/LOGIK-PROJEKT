#version 120

#define ratio adsk_result_frameratio

uniform float ratio;
uniform sampler2D adsk_results_pass1;
uniform float adsk_result_w, adsk_result_h;
vec2 res = vec2(adsk_result_w, adsk_result_h);
vec2 texel = vec2(1.0) / res;

uniform float scale;
uniform bool action_coords;
uniform vec2 pos;
uniform vec3 a_pos;

void main(void) {
	vec2 st = gl_FragCoord.xy / res;
	vec2 p = pos;

	if (action_coords)
    {
		p = a_pos.xy;
        p = p / res + .5;
    }

	st -= p;
	st.x *= ratio;
	st /= scale;
	st.x /= ratio;
	st += p;

	vec3 front = texture2D(adsk_results_pass1, st).rgb;

	gl_FragColor.rgb = front;
}
