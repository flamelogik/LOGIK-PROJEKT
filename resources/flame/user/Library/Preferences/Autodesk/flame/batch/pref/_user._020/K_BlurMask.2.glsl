//
// K_BlurMask v1.1
// Shader written by:   Kyle Obley (kyle.obley@gmail.com)
//
// Pass #2: Pass strength along to the other shaders to get around the way things are implimented
//


uniform sampler2D strength;
uniform float adsk_result_w, adsk_result_h;

void main()
{
	vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);
	float s = texture2D(strength, uv).r;
	gl_FragColor = vec4(s);
}
