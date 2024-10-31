#version 120

uniform float adsk_result_w, adsk_result_h;
vec2 res = vec2(adsk_result_w, adsk_result_h);

uniform sampler2D Strength;

void main(void)
{
	vec2 st = gl_FragCoord.xy / res;
	float strength = texture2D(Strength, st).r;

	gl_FragColor = vec4(strength);
}
