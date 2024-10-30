uniform sampler2D adsk_results_pass2;
uniform float adsk_result_w, adsk_result_h;

void main()
{
   vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );

   vec4 frontColor = texture2D(adsk_results_pass2,coords);

   float invMatte = 1.0 - frontColor.a;
   if (invMatte == 0.0)
      invMatte = 1.0;

   vec3 divided = vec3(frontColor.r / invMatte, frontColor.g / invMatte, frontColor.b / invMatte);

   vec4 finalColor = vec4(divided, frontColor.a);

   gl_FragColor = finalColor;   
}