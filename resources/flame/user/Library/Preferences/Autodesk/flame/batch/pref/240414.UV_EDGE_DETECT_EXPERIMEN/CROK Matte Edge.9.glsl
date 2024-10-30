#version 120

uniform sampler2D adsk_results_pass6, adsk_results_pass8;
uniform float adsk_result_w, adsk_result_h;
uniform float gamma_amount;
uniform float minInput;
uniform float maxInput;
uniform float shrink;
uniform bool enable_shrink;

vec2 res = vec2(adsk_result_w, adsk_result_h);

void main( void )
{
	vec2 uv = gl_FragCoord.xy / res;
  // matte before blur and shrink operation
  float tm = texture2D(adsk_results_pass6, uv).a;
  // blurred matte for shrink
  float m = texture2D(adsk_results_pass8, uv).a;
  // apply the shrink via histogram adjustments
  if ( enable_shrink )
  {
    float sh = 0.0;
    if ( shrink <= 0.0 )
    {
      sh = shrink * -1.0;
      m = min(max(m - sh, 0.0) / (1.0 - sh), 1.0);
    }
    else if ( shrink >= 0.0 )
    {
      sh = 1.0 - shrink;
      m = min(max(m - 0.0, 0.0) / (sh - 0.0), 1.0);
    }
  }
  else
    m = tm;
  gl_FragColor = vec4(m);
}
