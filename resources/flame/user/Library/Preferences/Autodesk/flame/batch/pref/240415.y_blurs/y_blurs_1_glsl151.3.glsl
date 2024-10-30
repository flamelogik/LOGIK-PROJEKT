#version 120

uniform sampler2D adsk_results_pass1;
uniform float adsk_result_w, adsk_result_h;
vec2 res = vec2(adsk_result_w, adsk_result_h);
vec2 texel = vec2(1.0) / res;

void main(void) {

	vec2 st = gl_FragCoord.xy / res;
	vec4 front = texture2D(adsk_results_pass1, st);

	gl_FragColor = vec4(front.rgb * front.a, front.a);
}
