#version 120

uniform sampler2D adsk_results_pass1, adsk_results_pass4, adsk_results_pass5;
uniform float adsk_result_w, adsk_result_h;
uniform float gamma_amount;
uniform bool enable_clamp;
uniform float minInput;
uniform float maxInput;

float adskEvalDynCurves( int curve, float x );
float adsk_getLuminance ( vec3 rgb );
uniform int lumaCurve;

vec2 res = vec2(adsk_result_w, adsk_result_h);

float gamma(float src, float value)
{
  return pow( max( 0.0, src ), 1.0 / (value + 1.0));
}

void main( void )
{
	vec2 uv = ( gl_FragCoord.xy / res);
  vec4 pixelsp_c = texture2D(adsk_results_pass5, uv);
  // original matte
  float om = texture2D(adsk_results_pass1, uv).a;
  // blurred matte for erode
  float m = texture2D(adsk_results_pass4, uv).a;
  // multiply inv matte with original matte
  m *= om;
  // Extract Luminance from source using API function
  float lum = adsk_getLuminance(vec3(m));
  // Here I'm evluating the single Luma curve widget
  float newLum = adskEvalDynCurves(lumaCurve,lum);
  // Here we are applying the curve result
  m *= lum > 0.0 ? newLum / lum : 0.0;
  // adjust matte gamma
  m = gamma(m, gamma_amount);
  gl_FragColor = vec4(pixelsp_c.rgb, m);
}
