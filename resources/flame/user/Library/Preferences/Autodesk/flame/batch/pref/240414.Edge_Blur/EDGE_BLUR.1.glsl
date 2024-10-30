//*****************************************************************************/
// 
// Filename: zigmod_template.glsl
//
// Beak f(x), 2016




uniform sampler2D input1, input2, input3, fakeout;
uniform float adsk_result_w, adsk_result_h;
vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );

uniform bool bypass;
vec3 f = texture2D(input1, coords).rgb;
vec3 b = texture2D(input2, coords).rgb;
vec3 m = texture2D(input3, coords).rgb;
vec3 r = texture2D(fakeout, coords).rgb;

void main(void)
{
  if (bypass == 0)
    gl_FragColor.rgba = vec4( r,m );
  else
    gl_FragColor.rgba = vec4( f,f );
}
