#version 120
#extension GL_ARB_shader_texture_lod : enable
//based on www.shadertoy.com/view/tsVGRd by Suslik
// License Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
//credits for hex tiling goes to Shane (https://www.shadertoy.com/view/Xljczw)
//center, index

// --------[ Autodesk Uniforms start here ]---------- //
uniform float adsk_result_w, adsk_result_h, adsk_time;
uniform sampler2D front;
vec2 res = vec2(adsk_result_w, adsk_result_h);
// --------[ Autodesk Uniforms end here ]---------- //

uniform float speed;
uniform float offset;
uniform float texFreq; // = 10.0;
uniform float tileFreq; // = 20.0;

// --------[ Shadertoy Globals start here ]---------- //
#define iTime adsk_time *.05 * speed + offset
#define iResolution res
#define fragCoord gl_FragCoord.xy
#define fragColor gl_FragColor
#define textureLod texture2DLod
#define texture texture2D
#define iChannel0 front
// --------[ Shadertoy Globals end here ]---------- //

const float pi = 3.141592;
const vec2 hexRatio = vec2(1.0, sqrt(3.0));

vec4 GetHexGridInfo(vec2 uv)
{
 //vec4 hexIndex = round(vec4(uv, uv - vec2(0.5, 1.0)) / hexRatio.xyxy);
 //vec4 hexIndex = floor(a + 0.5);
  vec4 hex_num = vec4(uv, uv - vec2(0.5, 1.0)) / hexRatio.xyxy;
  vec4 hexIndex =sign(hex_num)*floor(abs(hex_num)+0.5);

 vec4 hexCenter = vec4(hexIndex.xy * hexRatio, (hexIndex.zw + 0.5) * hexRatio);
 vec4 offset = uv.xyxy - hexCenter;
 return dot(offset.xy, offset.xy) < dot(offset.zw, offset.zw) ?
   vec4(hexCenter.xy, hexIndex.xy) :
   vec4(hexCenter.zw, hexIndex.zw);
}

float GetHexSDF(in vec2 p)
{
 p = abs(p);
 return 0.5 - max(dot(p, hexRatio * 0.5), p.x);
}

//xy: node pos, z: weight
vec3 GetTriangleInterpNode(in vec2 pos, in float freq, in int nodeIndex)
{
 vec2 nodeOffsets[] = vec2[](
   vec2(0.0, 0.0),
   vec2(1.0, 1.0),
   vec2(1.0,-1.0));

 vec2 uv = pos * freq + nodeOffsets[nodeIndex] / hexRatio.xy * 0.5;
 vec4 hexInfo = GetHexGridInfo(uv);
 float dist = GetHexSDF(uv - hexInfo.xy) * 2.0;
 return vec3(hexInfo.xy / freq, dist);
}

vec3 hash33( vec3 p )
{
 p = vec3( dot(p,vec3(127.1,311.7, 74.7)),
       dot(p,vec3(269.5,183.3,246.1)),
       dot(p,vec3(113.5,271.9,124.6)));

 return fract(sin(p)*43758.5453123);
}

vec4 GetTextureSample(vec2 pos, float freq, vec2 nodePoint)
{
   vec3 hash = hash33(vec3(nodePoint.xy, 0));
   float ang = hash.x * 2.0 * pi;
   mat2 rotation = mat2(cos(ang), sin(ang), -sin(ang), cos(ang));

   vec2 uv = rotation * pos * freq + hash.yz;
   return texture(iChannel0, uv);
}

vec2 GetVelocity(vec2 pos)
{
   float aspect = iResolution.y / iResolution.x;
   vec2 diff0 = pos - vec2(0.2, 0.5 * aspect);
   vec2 diff1 = pos - vec2(0.8, 0.5 * aspect);

   float charge0 = -0.01;
   float charge1 =  0.01;

   float eps = 0.1;
   return
       normalize(diff0) * charge0 / (dot(diff0, diff0) + eps) +
       normalize(diff1) * charge1 / (dot(diff1, diff1) + eps);
}

//from Qizhi Yu, et al [2011]. Lagrangian Texture Advection: Preserving Both Spectrum and Velocity Field.
//IEEE Transactions on Visualization and Computer Graphics 17, 11 (2011), 1612–1623
vec3 PreserveVariance(vec3 linearColor, vec3 meanColor, float moment2)
{
   return (linearColor - meanColor) / sqrt(moment2) + meanColor;
}

void main( void )
{
  // Normalized pixel coordinates (from 0 to 1)
  vec2 normCoord = fragCoord / iResolution.xy;
  fragColor = vec4(0.0);

  float moment2 = 0.0;
  for(int i = 0; i < 3; i++)
  {
    vec3 interpNode = GetTriangleInterpNode(normCoord, tileFreq, i);
    fragColor += GetTextureSample(normCoord, texFreq, interpNode.xy) * interpNode.z;
    moment2 += interpNode.z * interpNode.z;
  }
  vec3 meanColor = textureLod(front, vec2(0.0), 10.0).rgb;
  fragColor.rgb = PreserveVariance(fragColor.rgb, meanColor, moment2);
}
