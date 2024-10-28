//*****************************************************************************/
//
// Filename: MultiExecutionSeparableGaussianBlur.1.glsl
//
// Copyright (c) 2017 Autodesk, Inc.
// All rights reserved.
//
// This computer source code and related instructions and comments are the
// unpublished confidential and proprietary information of Autodesk, Inc.
// and are protected under applicable copyright and trade secret law.
// They may not be disclosed to, copied or used by any third party without
// the prior written consent of Autodesk, Inc.
//*****************************************************************************/

/*
 * A multi-execution matchbox shader pass example :
 *
 * Implement in a single file the separable gaussian blur approximation
 * (see. https://developer.nvidia.com/gpugems/GPUGems3/gpugems3_ch40.html )
 * -> the first execution computes the horizontal pass
 * -> the second execution computes the vertical pass
 */

// uniform sampler2D adsk_results_pass1; // input
uniform float adsk_result_w, adsk_result_h; // size of the textures
uniform sampler2D adsk_results_pass2; // previous execution result
uniform sampler2D adsk_results_pass1;

// horizontal / vertical size of the blur in pixels
uniform vec2 maxBlurSize;
uniform float propMaxBlurSize;
uniform bool propBlur;

// current pass execution number (0 based)
// -> first (0) execution is for the horizontal pass
// -> second (1) execution is for the vertical pass
uniform int adsk_result_execution;

#define SQRT_2_PI 2.506628275

//-----------------------------------------------------------------------------
//
void main()
{
   bool firstExecution;
   
   if (adsk_result_execution == 0)
      firstExecution = true;
   else
      firstExecution = false;

   // inverse output size
   vec2 inv_out_size = vec2(1.0) / vec2(adsk_result_w, adsk_result_h);
   //vec2 inv_out_size = vec2(1.0) / vec2(kernelsize);

   // uv coords
   vec2 uv = gl_FragCoord.xy * inv_out_size;

   // delta for horizontal/vertical convolution
   vec2 uv_delta =  firstExecution ? vec2( inv_out_size.x, 0 ) : vec2( 0, inv_out_size.y );

   // convolution kernel parameter
   //float currMaxBlurSize = firstExecution ? maxBlurSize.x : maxBlurSize.y;
   //float currMaxBlurSize = propBlur ? propMaxBlurSize : firstExecution ? maxBlurSize.x : maxBlurSize.y;
   float currMaxBlurSize;
   if (propBlur)
      currMaxBlurSize = propMaxBlurSize;
   else
   {
      if (firstExecution)
         currMaxBlurSize = maxBlurSize.x;
      else
         currMaxBlurSize = maxBlurSize.y;
   }

   int support = int( ceil( currMaxBlurSize ) );
   float sigma = currMaxBlurSize * 0.4;

   // polynomial approximation (see. reference above)
   vec3 g;
   g.x = 1.0 / (SQRT_2_PI * sigma);
   g.y = exp( -0.5 / ( sigma * sigma ) );
   g.z = g.y * g.y;

   // initialize
   vec4  frag = firstExecution ?
         texture2D( adsk_results_pass1, uv ) : texture2D( adsk_results_pass2, uv );

   vec4  result = g.x * 1.0 * frag.rgba;
   vec2  norm = vec2(g.x, g.x * 1.0);
   g.xy *= g.yz;

   // convolution
   for( int off = 1; off < support; ++off )
   {
      vec2 uv_offset = uv_delta * vec2(off);

      vec4 frag_m = firstExecution ? 
         texture2D( adsk_results_pass1, uv - uv_offset ) : texture2D( adsk_results_pass2, uv - uv_offset );
      vec4 frag_p = firstExecution ? 
         texture2D( adsk_results_pass1, uv + uv_offset ) : texture2D( adsk_results_pass2, uv + uv_offset );

      result += g.x * ( frag_m.rgba * 1.0 + frag_p.rgba * 1.0 );
      norm += vec2( g.x, g.x * ( 1.0 + 1.0 ) );
      g.xy *= g.yz;
   }

   // normalize the convolution and set the output
   if ( (propBlur) && (propMaxBlurSize == 0.0) )
      gl_FragColor = texture2D(adsk_results_pass1, uv);
   //else if ( (propBlur == false) && (maxBlurSize == vec2(0.0)) )
   //   gl_FragColor = texture2D(adsk_results_pass1, uv);
   else if ( (propBlur == false) && (currMaxBlurSize == 0.0) && (firstExecution) )
      gl_FragColor = texture2D(adsk_results_pass1, uv);
   else if ( (propBlur == false) && (currMaxBlurSize == 0.0) && (firstExecution == false) )
      gl_FragColor = texture2D(adsk_results_pass2, uv);
   else
      gl_FragColor =  vec4( norm.y > 0.0 ? result / norm.y : vec4( 0.0, 0.0, 0.0, frag.a ) ) ;
}