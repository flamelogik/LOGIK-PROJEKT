#version 120
// blur the matte to get a edge matte for the colourcorrection
uniform float blur_edge_matte, adsk_result_w, adsk_result_h;
uniform sampler2D adsk_results_pass1;

void main()
{
   vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   int f0int = int(blur_edge_matte);
   float accu = 0.0;
   float energy = 0.0;
   float blur_fg_x = 0.0;

   for( int x = -f0int; x <= f0int; x++)
   {
      vec2 currentCoord = vec2(coords.x+float(x)/adsk_result_w, coords.y);
      float aSample = texture2D(adsk_results_pass1, currentCoord).a;
      float anEnergy = 1.0 - ( abs(float(x)) / blur_edge_matte);
      energy += anEnergy;
      accu+= aSample * anEnergy;
   }

   blur_fg_x =
      energy > 0.0 ? (accu / energy) :
                     texture2D(adsk_results_pass1, coords).a;

   gl_FragColor = vec4( blur_fg_x );
}
