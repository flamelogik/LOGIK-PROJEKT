#version 120
// edge detection based on https://www.shadertoy.com/view/Mdf3zr
uniform float adsk_result_w, adsk_result_h, adsk_time;
vec2 res = vec2(adsk_result_w, adsk_result_h);
uniform sampler2D adsk_results_pass9, adsk_results_pass11;
uniform float edge;
uniform bool edge_detect_enable;

float lookup(vec2 p, float dx, float dy)
{
    vec2 uv = (p.xy + vec2(dx * edge, dy * edge)) / res.xy;
    vec4 e_matte = texture2D(adsk_results_pass11, uv.xy);
    return 0.2126*e_matte.r + 0.7152*e_matte.g + 0.0722*e_matte.b;
}

void main(void)
{
  vec2 p = gl_FragCoord.xy;
  vec2 uv = gl_FragCoord.xy / res;
  float c = 0.0;

  if ( edge_detect_enable )
  {
    float gx = 0.0;
    gx += -1.0 * lookup(p, -1.0, -1.0);
    gx += -2.0 * lookup(p, -1.0,  0.0);
    gx += -1.0 * lookup(p, -1.0,  1.0);
    gx +=  1.0 * lookup(p,  1.0, -1.0);
    gx +=  2.0 * lookup(p,  1.0,  0.0);
    gx +=  1.0 * lookup(p,  1.0,  1.0);
    float gy = 0.0;
    gy += -1.0 * lookup(p, -1.0, -1.0);
    gy += -2.0 * lookup(p,  0.0, -1.0);
    gy += -1.0 * lookup(p,  1.0, -1.0);
    gy +=  1.0 * lookup(p, -1.0,  1.0);
    gy +=  2.0 * lookup(p,  0.0,  1.0);
    gy +=  1.0 * lookup(p,  1.0,  1.0);
    c = gx*gx + gy*gy;
  }
  else
  {
    c = texture2D(adsk_results_pass9, uv).a;
  }
  
	gl_FragColor = vec4(c);
}
