//
// K_BlurMask v1.1
// Shader written by:   Kyle Obley (kyle.obley@gmail.com)
//
// Pass #1: Pass front along to the other shaders to get around the way things are implimented
//


uniform sampler2D front, matte;
uniform float adsk_result_w, adsk_result_h;

void main()
{
	vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);
	vec3 f = texture2D(front, uv).rgb;
	float m = texture2D(matte, uv).r;
	gl_FragColor = vec4(f, m);
}
