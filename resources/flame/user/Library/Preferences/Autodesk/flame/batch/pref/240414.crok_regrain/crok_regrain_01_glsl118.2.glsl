uniform sampler2D adsk_results_pass1;
uniform float adsk_result_w, adsk_result_h;
vec2 resolution = vec2(adsk_result_w, adsk_result_h);
uniform vec3 rgb_blur;

void main(void)
{
	vec2 uv = gl_FragCoord.xy / resolution;
    int denominator = 0;
    const float intensity = 1.0;
    vec2 pixelWidth = vec2(1.0)/resolution.xy * intensity;
    const int size = 5;

	vec3 noise = texture2D(adsk_results_pass1, uv).rgb;

	if ( rgb_blur != vec3(0.0) )
        {
		    for (int x=-size; x<size; x++) {
		        for (int y=-size; y<size; y++) {

		        	float fx_r = float(x) * pixelWidth.x*rgb_blur.r;
		           	float fy_r = float(y) * pixelWidth.y*rgb_blur.r;
					noise.r += texture2D(adsk_results_pass1, uv + vec2(fx_r,fy_r)).r;

		        	float fx_g = float(x) * pixelWidth.x*rgb_blur.g;
		           	float fy_g = float(y) * pixelWidth.y*rgb_blur.g;
					noise.g += texture2D(adsk_results_pass1, uv + vec2(fx_g,fy_g)).g;

		        	float fx_b = float(x) * pixelWidth.x*rgb_blur.b;
		           	float fy_b = float(y) * pixelWidth.y*rgb_blur.b;
					noise.b += texture2D(adsk_results_pass1, uv + vec2(fx_b,fy_b)).b;

		        	denominator++;
		        }
		    }
			noise /= float(denominator);
        }
		gl_FragColor.rgb = noise;
	}
