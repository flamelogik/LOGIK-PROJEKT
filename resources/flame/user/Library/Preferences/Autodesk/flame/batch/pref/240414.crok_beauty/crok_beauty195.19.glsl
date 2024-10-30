#version 120
// Colour correct cleaned Skin

uniform sampler2D adsk_results_pass15, adsk_results_pass18;
uniform float adsk_result_w, adsk_result_h;
uniform float hue_amount, sat_amount;

vec3  adsk_yuv2rgb( vec3 );
vec3  adsk_rgb2yuv( vec3 );

vec3 hueshift( vec3 source, float hue_amount, float sat )
{
   vec3 yuv = adsk_rgb2yuv( source );
   float co = cos( radians( hue_amount ) );
   float si = sin( radians( hue_amount ) );

   float s = ( sat  * 0.01 );

   mat3 r = mat3( 1.0, 0.0, 0.0,
                   0.0, s*co,   si,
                   0.0,-si,   s*co );

   return adsk_yuv2rgb( r * yuv );
}

void main()
{
   vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   vec3 c = texture2D(adsk_results_pass18, uv).rgb;
   float m = texture2D(adsk_results_pass15, uv).a;

   // apply hue hueShift
   //c = hueshift(c, hue_amount, sat_amount);
   c = m * hueshift(c, hue_amount, sat_amount) + (1.0 - m) * c;

   //c = vec3(matte * c + (1.0 - matte) * original);

   gl_FragColor = vec4(c, m);
}
