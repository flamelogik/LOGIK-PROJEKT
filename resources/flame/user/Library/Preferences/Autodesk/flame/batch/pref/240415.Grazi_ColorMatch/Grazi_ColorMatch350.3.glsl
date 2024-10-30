//*****************************************************************************/
// 
// Filename: PyramidBlur.1.glsl
//
// Copyright (c) 2016 Autodesk, Inc.
// All rights reserved.
//
// Use of this software is subject to the terms of the Autodesk license 
// agreement provided at the time of installation or download, or which 
// otherwise accompanies this software in either electronic or hard copy form. 
//*****************************************************************************/

uniform sampler2D colormatch;
uniform float adsk_result_w, adsk_result_h;
uniform vec2 blurAmount;
uniform bool propBlur;
uniform float propBlurAmount;

void main()
{
   vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   float blurValue = propBlur ? propBlurAmount : blurAmount.x;
   int intPart = int( blurValue );
   vec4 accu = vec4(0);
   float energy = 0.0;
   float matteEnergy = 0.0;
   vec4 finalColor = vec4(0.0);
   
   for( int x = -intPart; x <= intPart; x++)
   {
      vec2 currentCoord = vec2(coords.x+float(x)/adsk_result_w, coords.y);
      vec4 aSample = vec4( vec3(texture2D(colormatch, currentCoord).rgb),
                           1.0 );
      float anEnergy = 1.0 - ( abs(float(x)) / blurValue );
      energy += anEnergy;
      accu += aSample * anEnergy;
   }
   
   finalColor = 
      energy > 0.0 ? (accu / energy) : 
                     vec4( vec3(texture2D(colormatch, coords).rgb),
                           1.0 );
                     
   gl_FragColor = finalColor;
}
