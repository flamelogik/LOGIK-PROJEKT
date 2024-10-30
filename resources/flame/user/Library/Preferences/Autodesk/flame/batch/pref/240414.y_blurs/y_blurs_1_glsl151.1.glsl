#version 120

uniform sampler2D Front, Matte;
uniform float adsk_result_w, adsk_result_h;
vec2 res = vec2(adsk_result_w, adsk_result_h);
vec2 texel  = vec2(1.0) / res;

uniform int i_colorspace;
uniform bool invert_matte;

vec3 from_sRGB(vec3 col)
{
    if (col.r >= 0.0) {
        col.r = pow((col.r +.055)/ 1.055, 2.4);
    }

    if (col.g >= 0.0) {
        col.g = pow((col.g +.055)/ 1.055, 2.4);
    }

    if (col.b >= 0.0) {
        col.b = pow((col.b +.055)/ 1.055, 2.4);
    }

    return col;
}

vec3 from_rec709(vec3 col)
{
    if (col.r < .081) {
        col.r /= 4.5;
    } else {
        col.r = pow((col.r +.099)/ 1.099, 1 / .45);
    }

    if (col.g < .081) {
        col.g /= 4.5;
    } else {
        col.g = pow((col.g +.099)/ 1.099, 1 / .45);
    }

    if (col.b < .081) {
        col.b /= 4.5;
    } else {
        col.b = pow((col.b +.099)/ 1.099, 1 / .45);
    }

    return col;
}

vec3 adjust_gamma(vec3 col, float gamma)
{
    col.r = pow(col.r, gamma);
    col.g = pow(col.g, gamma);
    col.b = pow(col.b, gamma);

    return col;
}


void main(void)
{
    vec2 st = gl_FragCoord.xy / res;
   	vec3 front = texture2D(Front, st).rgb;
    float matte = texture2D(Matte, st).r;

    if (invert_matte)
    {
        matte = 1.0 - matte;
    }

    if (i_colorspace == 0) {
        front = from_rec709(front);
    } else if (i_colorspace == 1) {
        front = from_sRGB(front);
    } else if (i_colorspace == 2) {
        //linear
    } else if (i_colorspace == 3) {
        front = adjust_gamma(front, 2.2);
    } else if (i_colorspace == 4) {
        front = adjust_gamma(front, 1.8);
    }

    gl_FragColor = vec4(front, matte);
}
