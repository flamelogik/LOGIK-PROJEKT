#version 120
// pixel spread operation
uniform sampler2D adsk_results_pass1, adsk_results_pass2;
uniform float adsk_result_w, adsk_result_h;
uniform float pixelspread_amount;
uniform float blur_front;
uniform int stretch_amount;
uniform int spread_type;

int samples = 100;
int oversamples = 1;

vec2 res = vec2(adsk_result_w, adsk_result_h);

float radians_per_sample = 2.3999632;
float radius_per_sample = 2.0;

float g_matte(vec2 uv)
{
   return texture2D(adsk_results_pass1, uv).a;
}

float gamma(float src, float value)
{
  return pow( max( 0.0, src ), 1.0 / (value + 1.0));
}

void main()
{
  vec2 uv = gl_FragCoord.xy / res;
	vec2 size_inv=vec2(1.0 / adsk_result_w, 1.0 / adsk_result_h);
  float m = texture2D(adsk_results_pass1, uv).a;
  vec3 f = texture2D(adsk_results_pass1, uv).rgb;
  vec4 col = vec4(0.0);

  if ( spread_type == 0 )
  {
    // Parallax Spread
    float p_amount = -1.0 * pixelspread_amount * .1;
    float cr = cos(0.0);
    float sr = sin(0.0);
    mat3 g_trans = mat3( cr*p_amount*size_inv.x, sr*p_amount*size_inv.y, 0.0, -sr*p_amount*size_inv.x, cr*p_amount*size_inv.y, 0.0, 0.0, 0.0, 1.0 );
    vec4 disp_h = vec4(g_matte(uv+vec2(0.0,size_inv.y)),g_matte(uv+vec2(0.0,-size_inv.y)),g_matte(uv+vec2(-size_inv.x,0.0)),g_matte(uv+vec2(size_inv.x,0.0)));
    vec4 disp_d = vec4(g_matte(uv+size_inv),g_matte(uv-size_inv),g_matte(uv+vec2(-size_inv.x,size_inv.y)),g_matte(uv+vec2(size_inv.x,-size_inv.y)));
    disp_h = max( disp_h, 0.0);
    disp_d = max( disp_d, 0.0);
    vec4 levels = vec4(1.0);
    disp_h = pow( disp_h, levels );
    disp_d = pow(disp_d, levels );
    vec2 gradient = vec2(0.0);
    gradient.x = dot( disp_h, vec4(0.0, 0.0, 2.0, -2.0)) + dot( disp_d, vec4(-1.0, 1.0, 1.0, -1.0));
    gradient.y = dot( disp_h, vec4(-2.0, 2.0, 0.0, 0.0)) + dot( disp_d, vec4(-1.0, 1.0, -1.0, 1.0));
    gradient = ( g_trans * vec3( gradient, 1.0)).xy;

    gl_FragColor = vec4(texture2D(adsk_results_pass1, uv + gradient).rgb, g_matte(uv + gradient));
  }
  else if ( spread_type == 1 )
  {
    vec2 xy = gl_FragCoord.xy;
    // Factor to convert pixels to [0,1] texture coords
    vec2 px = vec2(1.0) / vec2(adsk_result_w, adsk_result_h);
    // Get vectors from previous pass
    vec2 d = texture2D(adsk_results_pass2, xy * px).xy;
    float sam = float(samples);
    for(int j = 0; j < oversamples; j++) {
      for(int k = 0; k < oversamples; k++) {
        // Starting point for this sample
        xy = gl_FragCoord.xy, float(k) / (float(oversamples) + 1.0);
        float dist = 0.0;
        // Walk along path by sampling vector image, moving, sampling, moving...
        for(float i = 0.0; i < sam; i++) {
          d = texture2D(adsk_results_pass2, xy * px).xy;
          if(length(d) == 0.0) {
            // No gradient at this point in the map, early out
            break;
          }
          xy += d * (blur_front * -0.01/sam) + (blur_front * -0.01/32.0);
          dist += length(d * (blur_front * -0.01/sam));
        }
        // Sample front image where our walk ended up
        col.rgb += texture2D(adsk_results_pass1, xy * px).rgb;
        // Length we've travelled to the matte output
        //col.a += dist * (blur_front * 0.01/32.0);
      }
    }
    gl_FragColor = col;
  }

  else if ( spread_type == 2 )
  {
    // Smear Spread
    for (int s = 0; s < stretch_amount; s++)
    {
      vec2 spiral = vec2(sin(float(s)*radians_per_sample), cos(float(s)*radians_per_sample));
      float dist = sqrt(radius_per_sample * float(s));
      float max_dist = sqrt(radius_per_sample * radius_per_sample);
      spiral *= dist;
      vec2 uv =( gl_FragCoord.xy + spiral) / res;
      vec4 sampled_pixel = texture2D(adsk_results_pass1, uv);
      sampled_pixel.rgb *= sampled_pixel.a;
      col += sampled_pixel * (1.0 / (1.0 + dist));
      if (col.a >= 1.0) break;
    }
    gl_FragColor = col;
  }
}
