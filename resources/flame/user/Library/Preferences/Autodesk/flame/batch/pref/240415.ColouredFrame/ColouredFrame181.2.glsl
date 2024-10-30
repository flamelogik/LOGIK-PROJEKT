#version 120

uniform float adsk_result_w, adsk_result_h;
vec2 res = vec2(adsk_result_w, adsk_result_h);

uniform sampler2D Back;

void main(void)
{
	vec2 st = gl_FragCoord.xy / res;
	vec3 back = texture2D(Back, st).rgb;

	gl_FragColor = vec4(back, 0.0);
}
