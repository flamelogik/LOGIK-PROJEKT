#version 120

// Change the folling 4 lines to suite
//#define STRENGTH adsk_results_pass2
//#define VERTICAL 
//#define STRENGTH_CHANNEL 

uniform sampler2D adsk_results_pass1;
uniform sampler2D adsk_results_pass2;

uniform bool output_blur;

#define PI 3.141592653589793238462643383279502884197969

#ifdef STRENGTH_CHANNEL
	uniform sampler2D STRENGTH;
#endif

#ifndef VERTICAL
	uniform float v_bias;
	float bias = v_bias;
	const vec2 dir = vec2(0.0, 1.0);
#else
	uniform float h_bias;
	float bias = h_bias;
	const vec2 dir = vec2(1.0, 0.0);
#endif

uniform float blur_amount;
uniform float blur_red;
uniform float blur_green;
uniform float blur_blue;
float blur_matte = 1.0;

uniform float adsk_result_w, adsk_result_h;
vec2 res = vec2(adsk_result_w, adsk_result_h);
vec2 texel  = vec2(1.0) / res;

uniform float amount;

vec4 gblur()
{
	 //The blur function is the work of Lewis Saunders.
	vec2 xy = gl_FragCoord.xy;

	float strength = 1.0;

	//Optional texture used to weight amount of blur
	#ifdef STRENGTH_CHANNEL
		strength = texture2D(STRENGTH, gl_FragCoord.xy / res).a;
	#endif

	float br = blur_red * blur_amount * bias * strength;
	float bg = blur_green * blur_amount * bias * strength;
	float bb = blur_blue * blur_amount * bias * strength;
	float bm = blur_matte * blur_amount * bias * strength;

	float support = max(max(max(br, bg), bb), bm) * 3.0;

	vec4 sigmas = vec4(br, bg, bb, bm);
	sigmas = max(sigmas, 0.0001);

	vec4 gx, gy, gz;
	gx = 1.0 / (sqrt(2.0 * PI) * sigmas);
	gy = exp(-0.5 / (sigmas * sigmas));
	gz = gy * gy;

	vec4 a = gx * texture2D(adsk_results_pass2, xy * texel);
	vec4 energy = gx;
	gx *= gy;
	gy *= gz;

	for(float i = 1; i <= support; i++) {
        a += gx * texture2D(adsk_results_pass2, (xy - i * dir) * texel);
        a += gx * texture2D(adsk_results_pass2, (xy + i * dir) * texel);
		energy += 2.0 * gx;
		gx *= gy;
		gy *= gz;
	}

	a /= energy;

	return a;
}

void main(void)
{
	vec4 blur = gblur();
	vec4 front = texture2D(adsk_results_pass1, gl_FragCoord.xy / res);

	vec4 sharp = mix(blur, front, amount * front.a);
	if (output_blur) {
		sharp = blur;
	}
	gl_FragColor = sharp;
}
