//KE_ObjectObliterator v.4
//Created by Ted Stanley (KuleshovEffect) July 2023
//Based on a setup by Renee Tymn (DigitalBanshee)

uniform sampler2D frontTex, matteTex;
uniform float adsk_result_w, adsk_result_h;

void main()
{
   vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );

   vec3 frontColor = texture2D(frontTex,coords).rgb;
   vec3 matteColor = texture2D(matteTex,coords).rgb;

   vec3 blackmult = (frontColor * (1.0 - matteColor)).rgb;

   vec4 finalColor = vec4(blackmult.rgb, matteColor);

   gl_FragColor = finalColor;
}