//
// K_BlurMask v1.1
// Shader written by:   Kyle Obley (kyle.obley@gmail.com)
//
// Pass #6: Put everything back together
//

uniform sampler2D adsk_results_pass1, adsk_results_pass2, adsk_results_pass5;
uniform float adsk_result_w, adsk_result_h;
uniform int matte_output_selection;

void main() {
	vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);
	vec4 blurred = texture2D(adsk_results_pass5, uv).rgba;
	vec3 back = texture2D(adsk_results_pass1, uv).rgb;
	float src_matte = texture2D(adsk_results_pass1, uv).a;
	float strength = texture2D(adsk_results_pass2, uv).r;

	float fin_matte = 0.0;

	if (matte_output_selection == 0)
		fin_matte = src_matte;
	if (matte_output_selection == 1)
		fin_matte = blurred.a;
	if (matte_output_selection == 2)
		fin_matte = strength;

	gl_FragColor = vec4 (mix(back, (blurred.rgb/(blurred.a + 0.0001)), src_matte), fin_matte);
}
