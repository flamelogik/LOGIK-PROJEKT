#version 120

// tune the edge of the clean green / bluescreen
uniform sampler2D adsk_results_pass3, adsk_results_pass6, adsk_results_pass8;
uniform float adsk_result_w, adsk_result_h;
uniform float minInput;

void main()
{
   vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   vec4 c = vec4(0.0);
   vec3 org_c = texture2D(adsk_results_pass3, uv).rgb;
   vec3 clean_screen = texture2D(adsk_results_pass6, uv).rgb;
   float org_m = texture2D(adsk_results_pass3, uv).a;
   float b_e_m = texture2D(adsk_results_pass8, uv).a;

   // do some 2D Histogramm adjustments
   b_e_m = min(max(b_e_m - minInput, 0.0) / (1.0 - minInput), 1.0);

   // multiply blurred edge matte by org matte
   vec3 m2 = vec3(b_e_m * org_m);

   // comp result with the chromakey matte over original
   c.rgb = vec3(m2 * org_c + (1.0 - m2) * clean_screen);


  gl_FragColor = vec4(c.rgb, m2);
}
