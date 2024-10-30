//*****************************************************************************/
// 
// Filename: PyramidBlur.2.glsl
//
// Copyright (c) 2016 Autodesk, Inc.
// All rights reserved.
//
// Use of this software is subject to the terms of the Autodesk license 
// agreement provided at the time of installation or download, or which 
// otherwise accompanies this software in either electronic or hard copy form. 
//*****************************************************************************/

uniform sampler2D adsk_results_pass2, adsk_results_pass4, colormatch;
uniform float adsk_result_w, adsk_result_h;

void main()
{
   vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   vec4 sourceColor1 = vec4 (texture2D(adsk_results_pass2, coords).rgb , 1.0);
   vec4 sourceColor2 = vec4 (texture2D(adsk_results_pass4, coords).rgb , 1.0);
   vec4 sourceColor3 = vec4 (texture2D(colormatch, coords).rgb , 1.0);
   
   vec4 division_result = sourceColor1 / sourceColor2 ;
   vec4 multiply_result = division_result * sourceColor3;
                     
   gl_FragColor = multiply_result;
}
  