#version 120
uniform sampler2D source, matte;
uniform float adsk_result_w, adsk_result_h;
uniform int spread_type;
uniform int soften;
uniform float matte_gamma;


vec2 res = vec2(adsk_result_w, adsk_result_h);

float gamma(float src, float value)
{
  return pow( max( 0.0, src ), 1.0 / value );
}

void main( void )
{
	vec2 uv = ( gl_FragCoord.xy / res);
  vec3 c = texture2D(source, uv).rgb;
  float m = texture2D(matte, uv).r;

  if ( spread_type == 2 )
  {
    float avg = 0.0;
    for (int i=-soften; i <= soften; ++i) {
        for (int j = -soften; j <= soften; ++j) {
            avg = avg + texture2D(matte, (gl_FragCoord.xy + vec2(float(i), float(j)))/res.xy).r;
        }
    }
    int area = (2*soften + 1) * (2*soften + 1);
    m = avg / area;
    m = gamma(m, matte_gamma);
  }

	gl_FragColor = vec4(c,m);
}
