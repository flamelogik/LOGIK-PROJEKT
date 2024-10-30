#version 120

// tune the clean green / bluescreen
uniform sampler2D adsk_results_pass5;
uniform float adsk_result_w, adsk_result_h;

void main()
{
   vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   vec4 c = texture2D(adsk_results_pass5, uv);

  // divide blurred fg by blurred matte
  c = c / c.a;

  gl_FragColor = c;
}
