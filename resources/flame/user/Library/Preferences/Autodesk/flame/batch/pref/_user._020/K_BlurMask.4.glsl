//
// K_BlurMask v1.1
// Shader written by:   Kyle Obley (kyle.obley@gmail.com)
//
// Pass #4: Horizontal blur
//

uniform sampler2D adsk_results_pass2, adsk_results_pass3;
uniform float adsk_result_w, adsk_result_h, sigma, h_bias;
const float pi = 3.141592653589793238462643383279502884197969;

void main() {
	vec2 xy = gl_FragCoord.xy;
	vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);

	//additional input strength
	float s = texture2D(adsk_results_pass2, uv).r;


	vec2 px = vec2(1.0) / vec2(adsk_result_w, adsk_result_h);

	float h_sigma = sigma * s * h_bias;

	int support = int(h_sigma * 3.0);

	// Incremental coefficient calculation setup as per GPU Gems 3
	vec3 g;
	g.x = 1.0 / (sqrt(2.0 * pi) * h_sigma);
	g.y = exp(-0.5 / (h_sigma * h_sigma));
	g.z = g.y * g.y;

	if(h_sigma == 0.0) {
		g.x = 1.0;
	}

	// Centre sample
	vec4 a = g.x * texture2D(adsk_results_pass3, xy * px);
	float energy = g.x;
	g.xy *= g.yz;

	// The rest
	for(int i = 1; i <= support; i++) {
		a += g.x * texture2D(adsk_results_pass3, (xy - vec2(float(i), 0.0)) * px);
		a += g.x * texture2D(adsk_results_pass3, (xy + vec2(float(i), 0.0)) * px);
		energy += 2.0 * g.x;
		g.xy *= g.yz;
	}
	a /= energy;

	gl_FragColor = a;
}
