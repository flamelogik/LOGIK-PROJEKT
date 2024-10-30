#version 120
#extension GL_ARB_shader_texture_lod : enable

#define INPUT adsk_results_pass6

vec2 center = vec2(.5);

uniform float adsk_time, adsk_result_w, adsk_result_h, adsk_result_frameratio;
vec2 res = vec2(adsk_result_w, adsk_result_h);
float time = adsk_time *.05;

uniform sampler2D INPUT;

uniform float filterwidth, filtersharpness;
float lin4mag = 0.0;
float emult = 0.0;
bool flin = false;
bool outputdfdx = false;
int texellimit = 128;
uniform vec2 offset;

//lewis@lewissaunders.com

vec4 texture2DEWA(vec2 p0) {
    vec2 du = dFdx(p0);
    vec2 dv = dFdy(p0);
    float scale = adsk_result_w;

    p0 -=vec2(0.5,0.5)/scale;
    vec2 p = scale * p0;

    float ux = filterwidth * du.s * scale;
    float vx = filterwidth * du.t * scale;
    float uy = filterwidth * dv.s * scale;
    float vy = filterwidth * dv.t * scale;

    // compute ellipse coefficients 
    // A*x*x + B*x*y + C*y*y = F.
    float A = vx*vx+vy*vy+1.0;
    float B = -2.0*(ux*vx+uy*vy);
    float C = ux*ux+uy*uy+1.0;
    float F = A*C-B*B/4.0;

    // Compute the ellipse's (u,v) bounding box in texture space
    float bbox_du = 2.0 / (-B*B+4.0*C*A) * sqrt((-B*B+4.0*C*A)*C*F);
    float bbox_dv = 2.0 / (-B*B+4.0*C*A) * sqrt(A*(-B*B+4.0*C*A)*F);

    // Clamp the ellipse so that the bbox includes at most TEXEL_LIMIT texels.
    // This is necessary in order to bound the run-time, since the ellipse can be arbitrarily large
    // Note that here we are actually clamping the bbox directly instead of the ellipse.
    if(bbox_du*bbox_dv>float(texellimit)) {
        float ll = sqrt(bbox_du*bbox_dv / float(texellimit));
        bbox_du/=ll;
        bbox_dv/ll;
    }

    // The ellipse bbox             
    int u0 = int(floor(p.s - bbox_du));
    int u1 = int(ceil (p.s + bbox_du));
    int v0 = int(floor(p.t - bbox_dv));
    int v1 = int(ceil (p.t + bbox_dv));

    // Heckbert MS thesis, p. 59; scan over the bounding box of the ellipse
    // and incrementally update the value of Ax^2+Bxy*Cy^2; when this
    // value, q, is less than F, we're inside the ellipse so we filter
    // away...
    vec4 num= vec4(0.0, 0.0, 0.0, 1.0);
    float den = 0.0;
    float ddq = 2.0 * A;
    float U = float(u0) - p.s;

    for (int v = v0; v <= v1; ++v) {
        float V = float(v) - p.t;
        float dq = A*(2.0*U+1.0) + B*V;
        float q = (C*V + B*U)*V + A*U*U;
        for (int u = u0; u <= u1; ++u) {
            if (q < F) {
                float r2 = q / F;
                // Gaussian filter weights
                float weight = exp(-filtersharpness * r2);

                num += weight * texture2D(INPUT, vec2(float(u)+0.5,float(v)+0.5)/scale);
                den += weight;
            }
            q += dq;
            dq += ddq;
        }
    }
    vec4 color = num*(1./den);
    return color;
}

void main(void)
{
	vec2 st = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);
	//vec2 coords = gl_FragCoord.xy / vec2(adsk_result_w, adsk_result_h);
    //vec2 uvcoords = mix(coords, texture2D(uv, coords).rg + offset, emult);

	gl_FragColor = texture2DEWA(st);
}
