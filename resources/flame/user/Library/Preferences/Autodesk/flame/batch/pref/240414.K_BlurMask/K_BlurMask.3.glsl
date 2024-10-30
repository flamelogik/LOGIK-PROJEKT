//
// K_BlurMask v1.1
// Shader written by:   Kyle Obley (kyle.obley@gmail.com)
//
// Pass #3: Multiply front by the matte
//


uniform sampler2D adsk_results_pass1;
uniform float adsk_result_w, adsk_result_h;

void main()
{
	vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);
	vec3 f = texture2D(adsk_results_pass1, uv).rgb;
	float m = texture2D(adsk_results_pass1, uv).a;
	gl_FragColor = vec4((f*m), m);
}
