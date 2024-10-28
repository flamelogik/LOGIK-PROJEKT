uniform sampler2D adsk_results_pass4, frontTex, matteTex;
uniform float adsk_result_w, adsk_result_h, strength;
uniform bool addTexture;
uniform vec2 axis;

void main()
{
   vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );

   vec4 dividedColor = texture2D(adsk_results_pass4,coords);
   vec3 origColor = texture2D(frontTex, coords).rgb;
   vec3 origMatte = texture2D(matteTex, coords).rgb;

   vec3 over;
   vec2 position_coords = (coords-(axis/1000.0));

   
   if (addTexture)
   {
      vec3 offsetDivided = texture2D(adsk_results_pass4, position_coords).rgb;
      vec3 offsetOrig = texture2D(frontTex, position_coords).rgb;
      vec3 retexture =  ((strength / 100.0)*(offsetOrig.rgb - offsetDivided.rgb)) + dividedColor.rgb;
      over = (retexture * origMatte) + (origColor * (1.0 - origMatte));
   }
   else
      over = (dividedColor.rgb * origMatte) + (origColor * (1.0 - origMatte));
   
   vec4 finalColor = vec4(over.rgb, dividedColor.a);

   gl_FragColor = finalColor;
}