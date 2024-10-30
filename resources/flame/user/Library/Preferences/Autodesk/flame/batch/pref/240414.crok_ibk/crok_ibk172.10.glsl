#version 120

// IBK Greenscreen Part
uniform sampler2D adsk_results_pass1, adsk_results_pass9, background, ext_clean;
uniform float adsk_result_w, adsk_result_h;
uniform float weight_red, weight_green, weight_blue;
uniform int out_option;
uniform float despill_amount;
uniform float edge_bright;
uniform float gamma_amount;
uniform bool unpremulitplied, use_external_clean_screen;
uniform int green_or_blue;

float adsk_getLuminance( in vec3 color );
vec4 adsk_getBlendedValue( int blendType, vec4 srcColor, vec4 dstColor );

vec3 saturation(vec3 rgb, float adjustment){
    // Algorithm from Chapter 16 of OpenGL Shading Language
    const vec3 W = vec3(0.2125, 0.7154, 0.0721);
    vec3 intensity = vec3(dot(rgb, W));
    return mix(intensity, rgb, adjustment);
}

float gamma( float source, float param )
{
   float invGamma = 1.0 / clamp(( param * param ), 1e-5, 100.0 );
   return pow( max( source, 0.0 ), invGamma );
}

  float ibk_green(vec4 c_org_f, vec4 c_clean_scr){
  // FG PART
  // mono red
  float red = c_org_f.r;
  // mono blue
  float blue = c_org_f.b;
  // mono green
  float green = c_org_f.g;
  // adjust weight
  red = red * weight_red;
  blue = blue * weight_blue;
  // add red and blue channel together
  float fg = red + blue;
  // subtract result of add red and blue - green
  fg = clamp(green - fg, 0.0, 99999999999.0);

  // CLEAN SCREEN PART
  // mono red
  float c_red = c_clean_scr.r;
  // mono blue
  float c_blue = c_clean_scr.b;
  // mono green
  float c_green = c_clean_scr.g;
  // adjust weight
  c_red = c_red * weight_red;
  c_blue = c_blue * weight_blue;
  // add red and blue channel together
  float c_screen = c_red + c_blue;
  // subtract result of add red and blue - green
  c_screen = c_green - c_screen;
  // divide org_fg by clean_screen
  return vec4(fg / c_screen).r;
}

float ibk_blue(vec4 c_org_f, vec4 c_clean_scr){
  // FG PART
  // mono red
  float red = c_org_f.r;
  // mono green
  float green = c_org_f.g;
  // mono blue
  float blue = c_org_f.b;
  // adjust weight
  red = red * weight_red;
  green = green * weight_green;
    // add red and green channel together
  float fg = red + green;
  // subtract result of add red and green - blue
  fg = clamp(blue - fg, 0.0, 99999999999.0);

  // CLEAN SCREEN PART
  // mono red
  float c_red = c_clean_scr.r;
  // mono green
  float c_green = c_clean_scr.g;
  // mono blue
  float c_blue = c_clean_scr.b;
  // adjust weight
  c_red = c_red * weight_red;
  c_green = c_green * weight_green;
  // add red and green channel together
  float c_screen = c_red + c_green;
  // subtract result of add red and green - blue
  c_screen = c_blue - c_screen;
  // divide org_fg by clean_screen
  return vec4(fg / c_screen).r;
}

vec3 substract_green_part(vec3 in1, vec3 in2){
  return in1 - in2;
}

vec2 additive_keying_part(vec3 clean_minus_org, vec3 org_minus_clean, vec3 bg){
  vec3 mono_bg = saturation(bg, 0.0);
  vec3 mono_bg1 = mono_bg * org_minus_clean;
  vec3 mono_bg2 = mono_bg * clean_minus_org;
  mono_bg1 = clamp(mono_bg1, 0.0, 1.0);
  mono_bg2 = clamp(mono_bg2, 0.0, 1.0);
  vec3 fin_mono_add = mono_bg1 + mono_bg2;
  return vec2(saturation(mono_bg2, 0.0).r, saturation(fin_mono_add, 0.0).r);
}

vec3 adjust_suppression(float ibk_matte, vec3 clean_screen)
{
  return ibk_matte * clean_screen;
}

vec3 control_edge_brightness(vec3 org_fg, vec3 green_supp, float ibk_matte)
{
  float m = 1.0 - ibk_matte;
  vec3 result_without_color_substract = org_fg * m;
  vec3 edge_brightness = result_without_color_substract - green_supp;
  vec3 suppressed = edge_brightness;
  suppressed.g = min((edge_brightness.r+edge_brightness.b)*0.5, edge_brightness.g);
  edge_brightness = mix( edge_brightness, suppressed, 1.0 );
  edge_brightness = mix(green_supp, green_supp + edge_brightness, edge_bright );
  return edge_brightness;
}

void main()
{
   vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   vec4 org_fg = texture2D(adsk_results_pass1, uv);
   vec4 clean_screen = texture2D(adsk_results_pass9, uv);
   vec4 ext_clean_screen = texture2D(ext_clean, uv);
   vec4 bg = texture2D(background, uv);

   if ( use_external_clean_screen )
   clean_screen = ext_clean_screen;

   vec3 clean_minus_org = substract_green_part( clean_screen.rgb, org_fg.rgb);
   vec3 org_minus_clean = substract_green_part( org_fg.rgb, clean_screen.rgb);

  float mono_fg1 = additive_keying_part(clean_minus_org, org_minus_clean, bg.rgb).r;
  float mono_fg2 = additive_keying_part(clean_minus_org, org_minus_clean, bg.rgb).g;

  float ibk_matte = 0.0;

  if ( green_or_blue ==0)
   ibk_matte = ibk_green(org_fg, clean_screen);

  else if ( green_or_blue == 1)
   ibk_matte = ibk_blue(org_fg, clean_screen);

  // adjust suppression
  vec3 adjust_yellow_sup = adjust_suppression(ibk_matte, clean_screen.rgb);

   // clamp negatives from adjust_yellow_sup
   vec3 clamp_neg = clamp(adjust_yellow_sup, 0.0, 99999999.0);
   // invert clamp negatives
   vec3 clamp_neg_negative = 1.0 - clamp_neg;
   clamp_neg_negative = clamp(clamp_neg_negative, 0.0, 99999999.0);

   //desat clamp negatives
   vec3 desat_clamp_neg = saturation(clamp_neg_negative, 0.0);

   // TODO add CC to adjust to compensate to much suppress

   //subtract clean screen from org Greenscreen
   vec3 green_supp = clamp(org_fg.rgb - clamp_neg, 0.0, 999999999.0);

   // Control_Edge_Brightness
   vec3 edge_brigthness = control_edge_brightness(org_fg.rgb, green_supp.rgb, ibk_matte );

  //divide green_supp by desat_clamp_neg
  vec3 green_sup_divide_by_desat_clamp_neg = edge_brigthness / desat_clamp_neg;

   // max / lighten desat FG from IBK matte
   ibk_matte = 1.0 - ibk_matte;
   vec3 desat_org_fg = saturation(green_supp.rgb, 0.0);
   vec4 final_ibk_matte = adsk_getBlendedValue( 29, vec4(ibk_matte), vec4(desat_org_fg.rgb, 1.0) );
   final_ibk_matte.rgb = final_ibk_matte.rgb + mono_fg1;
   final_ibk_matte = clamp(final_ibk_matte , 0.0, 1.0);

   // comp final FG over BG by matte
   // add the additive key ontop of the bg
   vec3 final_comp = mono_fg2 + bg.rgb;

   // unpremultiply FG
   if (unpremulitplied)
   green_sup_divide_by_desat_clamp_neg = green_sup_divide_by_desat_clamp_neg / final_ibk_matte.rgb;

   // gamma correctring the final matte
   final_ibk_matte = vec4(gamma (final_ibk_matte.r, gamma_amount));

   final_comp = vec3(final_ibk_matte.r * green_sup_divide_by_desat_clamp_neg + (1.0 - final_ibk_matte.r) * final_comp.rgb);

   if (out_option == 0)
   final_comp = clean_screen.rgb;
   else if (out_option == 1)
   final_comp = final_comp;
   else if (out_option == 2)
   final_comp = green_sup_divide_by_desat_clamp_neg * final_ibk_matte.rgb;
   else if (out_option == 3)
   final_comp = green_supp;

   gl_FragColor = vec4(final_comp, final_ibk_matte);
}
