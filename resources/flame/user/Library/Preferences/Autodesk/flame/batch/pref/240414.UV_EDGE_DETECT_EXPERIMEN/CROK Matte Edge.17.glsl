#version 120
uniform sampler2D adsk_results_pass5, adsk_results_pass14, adsk_results_pass16;
uniform float adsk_result_w, adsk_result_h;
uniform bool show_matte;
vec2 res = vec2(adsk_result_w, adsk_result_h);
uniform vec3 hue_shift;
uniform float edge_gamma, edge_gain;
uniform bool enable_clamp;
uniform bool enable_invert_m;

vec3  adsk_hsv2rgb( vec3 hsv );
float adsk_getLuminance( vec3 );

// We are using this function to map the Hue and Gain of the Colour Wheel in HSV to an RGB value
vec3 getRGB( float hue )
{
 return adsk_hsv2rgb( vec3( hue, hue_shift.z * 0.01, 1.0 ) );
}

vec3 gamma(vec3 src, float value)
{
  return pow( max( vec3 (0.0), src ), vec3(1.0 / value) );
}

vec3 gain( vec3 src, float value )
{
   return src * value * 0.01;
}

void main( void )
{
	vec2 uv = ( gl_FragCoord.xy / res);
  vec3 c = texture2D(adsk_results_pass5, uv).rgb;
  float m = texture2D(adsk_results_pass14, uv).r;
	float edge_m = texture2D(adsk_results_pass16, uv).r;

	// invert edge matte
	edge_m = 1.0 - edge_m;

	// We used the function detailed above to get our RGB Offset value
	vec3 offset = getRGB( hue_shift.x / 360.0 ) * vec3( hue_shift.y * 0.01);

	// Here we are applying the Offset to the Source
	vec3 edge_c = c + offset;

	// Here we insure that we preserve the Luminance of the image
	edge_c = edge_c * vec3(adsk_getLuminance( c ) / max(adsk_getLuminance( edge_c ), 0.001));

	// adjust forground edge gamma
	edge_c = gamma(edge_c, edge_gamma);

	// adjust gain
	edge_c = gain(edge_c, edge_gain);

	edge_c = vec3(edge_m * edge_c + (1.0 - edge_m) * c);
/*
	if ( show_matte )
		c = vec3( m ); */
  // clamp matte
  if ( enable_clamp )
    m = clamp(m, 0.0, 1.0);
  if ( enable_invert_m )
    m = 1.0 - m;

	gl_FragColor = vec4(edge_c,m);
}
