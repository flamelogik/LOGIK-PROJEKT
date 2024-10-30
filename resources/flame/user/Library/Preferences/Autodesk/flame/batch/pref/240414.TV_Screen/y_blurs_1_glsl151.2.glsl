#version 120

uniform sampler2D Strength;
uniform sampler2D adsk_results_pass1;
uniform float adsk_result_w, adsk_result_h;
vec2 res = vec2(adsk_result_w, adsk_result_h);
vec2 texel = vec2(1.0) / res;

uniform bool matte_is_strength;

void main(void) {

	vec2 st = gl_FragCoord.xy / res;
	vec4 front = texture2D(adsk_results_pass1, st);
   	float strength = texture2D(Strength, st).r;

	if (matte_is_strength) {
		strength = front.a;
	}

	gl_FragColor = vec4(front.rgb * front.a, strength);
}
