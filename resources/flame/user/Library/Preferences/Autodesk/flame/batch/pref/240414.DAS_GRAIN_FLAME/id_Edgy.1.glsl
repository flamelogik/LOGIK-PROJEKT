// Edgy (C)2021 Bob Maple
// bobm-matchbox [at] idolum.com

uniform sampler2D  in_front, in_matte;
uniform     float  adsk_result_w, adsk_result_h;
uniform      bool  showMatte, outputMatte;
uniform      vec3  colorHL;

vec3 adsk_rgb2yuv( vec3 );
vec3 adsk_yuv2rgb( vec3 );

//


void main(void) {

	// Convert pixel coords to UV position for texture2D
	// and fetch the input pixel into px

	vec2 uv  = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
	vec3 px  = texture2D( in_front, uv ).rgb;

	vec4  pxHL = vec4( colorHL, 1.0 );
	vec4  npx = vec4( px, 0.0 );
	vec3  rgbPx;

	// Do something important

	rgbPx = npx.rgb;

	npx = rgbPx.rgb == vec3(0.0,0.0,0.0) ? pxHL : npx;

	if( outputMatte )
		npx.rgb = npx.aaa;

	if( !showMatte )
		npx.a = texture2D( in_matte, uv ).r;

	gl_FragColor = npx;
}
