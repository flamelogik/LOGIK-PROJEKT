#version 120

uniform sampler2D front, matte;
uniform float adsk_result_w, adsk_result_h;

void main()
{
   vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   vec3 c = texture2D(front, uv).rgb;
   float m = texture2D(matte, uv).r;

   gl_FragColor = vec4(c, m);
}
