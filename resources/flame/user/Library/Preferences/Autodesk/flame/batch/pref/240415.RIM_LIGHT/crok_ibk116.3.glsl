#version 120

// create the clean green / bluescreen
uniform sampler2D adsk_results_pass1, adsk_results_pass2;
uniform float adsk_result_w, adsk_result_h;
uniform	bool use_external_matte;

void main()
{
   vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   vec3 f = texture2D(adsk_results_pass1, uv).rgb;
   float m = texture2D(adsk_results_pass2, uv).r;
   float ext_m = texture2D(adsk_results_pass1, uv).a;

   if ( use_external_matte )
 		m = 1.0 - ext_m;

  // multiply fg by matte
  f = f * m;
  
  gl_FragColor = vec4(f, m);
}
