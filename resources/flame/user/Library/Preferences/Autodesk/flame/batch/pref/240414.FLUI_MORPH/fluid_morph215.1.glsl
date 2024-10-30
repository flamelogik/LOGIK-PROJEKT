//*****************************************************************************/
// 
// Filename: Variables.glsl
//
// Copyright (c) 2013 Autodesk, Inc.
// All rights reserved.
// 
// This computer source code and related instructions and comments are the
// unpublished confidential and proprietary information of Autodesk, Inc.
// and are protected under applicable copyright and trade secret law.
// They may not be disclosed to, copied or used by any third party without
// the prior written consent of Autodesk, Inc.
//*****************************************************************************/

uniform sampler2D bg;
uniform bool useBG;
uniform float adsk_result_w, adsk_result_h;
uniform float Var01, Var02, Var03, Var04, Var05, Var06, Var07, Var08, Var09, Var10;
uniform vec3 Position01, Position02;
uniform vec3 Colour01, Colour02, Colour03, Colour04, Colour05;


void main(void)
{

	vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );

	vec3 col;
	
	if (coords.x < 0.1) {
		col	= coords.y < Var01 ? Colour01 : vec3(0.0);
	}

   if (coords.x > 0.1 && coords.x < 0.2) {
      col   = (coords.y < Var02) ? vec3(Colour02) : vec3(0.0);
   }

   if (coords.x > 0.2 && coords.x < 0.3) {
      col   = (coords.y < Var03) ? Colour03 : vec3(0.0);
   }

   if (coords.x > 0.3 && coords.x < 0.4) {
      col   = (coords.y < Var04) ? Colour04 : vec3(0.0);
   }

   if (coords.x > 0.4 && coords.x < 0.5) {
      col   = (coords.y < Var05) ? Colour05 : vec3(0.0);
   }

   if (coords.x > 0.5 && coords.x < 0.6) {
      col   = (coords.y < Var06) ? Colour01 : vec3(0.0);
   }

   if (coords.x > 0.6 && coords.x < 0.7) {
      col   = (coords.y < Var07) ? Colour02 : vec3(0.0);
   }

   if (coords.x > 0.7 && coords.x < 0.8) {
      col   = (coords.y < Var08) ? Colour03 : vec3(0.0);
   }

   if (coords.x > 0.8 && coords.x < 0.9) {
      col   = (coords.y < Var09) ? Colour04 : vec3(0.0);
   }

   if (coords.x > 0.9) {
      col   = (coords.y < Var10) ? Colour05 : vec3(0.0);
   }

	if (Position01 != vec3(0.0)) {
		if (distance(coords * vec2(adsk_result_w, adsk_result_h ), Position01.xy*vec2(adsk_result_w, adsk_result_h )) < 10.0) {
			col		= vec3(1.0) - col;
		}
	}

   if (Position02 != vec3(0.0)) {
      if (distance(coords * vec2(adsk_result_w, adsk_result_h ), Position02.xy*vec2(adsk_result_w, adsk_result_h )) < 10.0) {
         col      = vec3(1.0, 0.0, 0.0);
      }
   }

   vec3 img	= texture2D(bg, coords).rgb;

   col		= useBG ? img : col;

   gl_FragColor.rgba = vec4( col, 0.0 );
}
