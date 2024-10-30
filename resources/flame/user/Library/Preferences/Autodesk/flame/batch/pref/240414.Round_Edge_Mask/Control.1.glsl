// Variables (C)2019 Bob Maple
// bobm-matchbox [at] idolum.com


uniform sampler2D passthru;
uniform float adsk_result_w, adsk_result_h;

// Pass the back input to the output, no alpha

void main(void) {
	vec2 uv  = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
	gl_FragColor = vec4( texture2D( passthru, uv ).rgb, 0.0 );
}
