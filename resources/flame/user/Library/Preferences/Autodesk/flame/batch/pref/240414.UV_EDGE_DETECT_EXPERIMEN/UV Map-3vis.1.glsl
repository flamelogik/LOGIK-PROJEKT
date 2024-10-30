//*****************************************************************************/
// 
// Filename: uvmap_3vis.glsl
// Author: Eric Pouliot
//
// Copyright (c) 2013 3vis, Inc.
//*****************************************************************************/

uniform sampler2D iChannel0,iChannel1;
uniform float adsk_result_w, adsk_result_h;

uniform bool	PickObj;
uniform int	selectObj;

void main(void)
{

vec4 ResultPixel;

vec2 uv = gl_FragCoord.xy / vec2(adsk_result_w, adsk_result_h );

vec4 MapPixel = texture2D(iChannel0, uv);

vec2 SrcCoord = MapPixel.rg;

	if(PickObj && MapPixel.b != float(selectObj))
	{
		ResultPixel = vec4(0.0);
	}

	else
		ResultPixel = texture2D(iChannel1, SrcCoord);


ResultPixel.a = MapPixel.a;

gl_FragColor= ResultPixel;

}