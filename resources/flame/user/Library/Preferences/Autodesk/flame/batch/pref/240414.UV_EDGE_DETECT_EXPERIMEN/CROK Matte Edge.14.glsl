#version 120
// overall blur
uniform float blur_matte_all, oblur_aspect, adsk_result_w, adsk_result_h;
uniform sampler2D adsk_results_pass13;

void main()
{
   vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   float b_aspect = oblur_aspect;
   if ( oblur_aspect > 1.0 )
    b_aspect = (b_aspect - 1.0) * 10.0 + 1.0;
   float blur = 1.0 / b_aspect * blur_matte_all;
   int f0int = int(blur);
   float accu = 0.0;
   float energy = 0.0;
   float blur_fg_y = 0.0;

   for( int y = -f0int; y <= f0int; y++)
   {
      vec2 currentCoord = vec2(coords.x, coords.y+float(y)/adsk_result_h);
      float aSample = texture2D(adsk_results_pass13, currentCoord).a;
      float anEnergy = 1.0 - ( abs(float(y)) / blur);
      energy += anEnergy;
      accu+= aSample * anEnergy;
   }

   blur_fg_y =
      energy > 0.0 ? (accu / energy) :
                     texture2D(adsk_results_pass13, coords).a;

   gl_FragColor = vec4( blur_fg_y );
}
