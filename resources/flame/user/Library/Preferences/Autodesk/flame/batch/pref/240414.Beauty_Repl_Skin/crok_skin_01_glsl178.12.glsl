#version 120

uniform float adsk_result_w, adsk_result_h, adsk_result_frameratio;
uniform sampler2D adsk_results_pass6, adsk_results_pass9, adsk_results_pass11;
uniform float b_high, grunge_scale, s_bias_adj;

#define HASHSCALE1 .1031
#define HASHSCALE3 vec3(.1031, .1030, .0973)

float softLight( float s, float d )
{
	return (s < 0.5) ? d - (1.0 - 2.0 * s) * d * (1.0 - d)
		: (d < 0.25) ? d + (2.0 * s - 1.0) * d * ((16.0 * d - 12.0) * d + 3.0)
					 : d + (2.0 * s - 1.0) * (sqrt(d) - d);
}

vec3 softLight( vec3 s, vec3 d )
{
	vec3 c;
	c.x = softLight(s.x,d.x);
	c.y = softLight(s.y,d.y);
	c.z = softLight(s.z,d.z);
	return c;
}

float colorBurn( float s, float d )
{
	return 1.0 - (1.0 - d) / s;
}

float bias(float x, float b)
{
    b = -log2(1.0 - b);
    return 1.0 - pow(1.0 - pow(x, 1./b), b);
}
// start Fractal Noise

/*float hash(float x)
{
	return fract(sin(cos(x*12.13)*19.123)*17.321);
}*/
float hash(float p)
{
	vec3 p3  = fract(vec3(p) * HASHSCALE3);
    p3 += dot(p3, p3.yzx + 19.19);
    return fract((p3.x + p3.y) * p3.z);
}

float fn_noise(vec2 p)
{
	vec2 pm = mod(p,1.0);
	vec2 pd = p-pm;
	float v0=hash(pd.x+pd.y*41.0);
	float v1=hash(pd.x+1.0+pd.y*41.0);
	float v2=hash(pd.x+pd.y*41.0+41.0);
	float v3=hash(pd.x+pd.y*41.0+42.0);
	v0 = mix(v0,v1,smoothstep(0.0,1.0,pm.x));
	v2 = mix(v2,v3,smoothstep(0.0,1.0,pm.x));
	return mix(v0,v2,smoothstep(0.0,1.0,pm.y));
}

// start Simplex3D
float noise3D(vec3 p)
{
	return fract(sin(dot(p ,vec3(12.9898,78.233,128.852))) * 43758.5453)*2.0-1.0;
}

float simplex3D(vec3 p)
{

	float f3 = 1.0/3.0;
	float s = (p.x+p.y+p.z)*f3;
	int i = int(floor(p.x+s));
	int j = int(floor(p.y+s));
	int k = int(floor(p.z+s));

	float g3 = 1.0/6.0;
	float t = float((i+j+k))*g3;
	float x0 = float(i)-t;
	float y0 = float(j)-t;
	float z0 = float(k)-t;
	x0 = p.x-x0;
	y0 = p.y-y0;
	z0 = p.z-z0;

	int i1,j1,k1;
	int i2,j2,k2;

	if(x0>=y0)
	{
		if(y0>=z0){ i1=1; j1=0; k1=0; i2=1; j2=1; k2=0; } // X Y Z order
		else if(x0>=z0){ i1=1; j1=0; k1=0; i2=1; j2=0; k2=1; } // X Z Y order
		else { i1=0; j1=0; k1=1; i2=1; j2=0; k2=1; }  // Z X Z order
	}
	else
	{
		if(y0<z0) { i1=0; j1=0; k1=1; i2=0; j2=1; k2=1; } // Z Y X order
		else if(x0<z0) { i1=0; j1=1; k1=0; i2=0; j2=1; k2=1; } // Y Z X order
		else { i1=0; j1=1; k1=0; i2=1; j2=1; k2=0; } // Y X Z order
	}

	float x1 = x0 - float(i1) + g3;
	float y1 = y0 - float(j1) + g3;
	float z1 = z0 - float(k1) + g3;
	float x2 = x0 - float(i2) + 2.0*g3;
	float y2 = y0 - float(j2) + 2.0*g3;
	float z2 = z0 - float(k2) + 2.0*g3;
	float x3 = x0 - 1.0 + 3.0*g3;
	float y3 = y0 - 1.0 + 3.0*g3;
	float z3 = z0 - 1.0 + 3.0*g3;

	vec3 ijk0 = vec3(i,j,k);
	vec3 ijk1 = vec3(i+i1,j+j1,k+k1);
	vec3 ijk2 = vec3(i+i2,j+j2,k+k2);
	vec3 ijk3 = vec3(i+1,j+1,k+1);

	vec3 gr0 = normalize(vec3(noise3D(ijk0),noise3D(ijk0*2.01),noise3D(ijk0*2.02)));
	vec3 gr1 = normalize(vec3(noise3D(ijk1),noise3D(ijk1*2.01),noise3D(ijk1*2.02)));
	vec3 gr2 = normalize(vec3(noise3D(ijk2),noise3D(ijk2*2.01),noise3D(ijk2*2.02)));
	vec3 gr3 = normalize(vec3(noise3D(ijk3),noise3D(ijk3*2.01),noise3D(ijk3*2.02)));

	float n0 = 0.0;
	float n1 = 0.0;
	float n2 = 0.0;
	float n3 = 0.0;

	float t0 = 0.5 - x0*x0 - y0*y0 - z0*z0;
	if(t0>=0.0)
	{
		t0*=t0;
		n0 = t0 * t0 * dot(gr0, vec3(x0, y0, z0));
	}
	float t1 = 0.5 - x1*x1 - y1*y1 - z1*z1;
	if(t1>=0.0)
	{
		t1*=t1;
		n1 = t1 * t1 * dot(gr1, vec3(x1, y1, z1));
	}
	float t2 = 0.5 - x2*x2 - y2*y2 - z2*z2;
	if(t2>=0.0)
	{
		t2 *= t2;
		n2 = t2 * t2 * dot(gr2, vec3(x2, y2, z2));
	}
	float t3 = 0.5 - x3*x3 - y3*y3 - z3*z3;
	if(t3>=0.0)
	{
		t3 *= t3;
		n3 = t3 * t3 * dot(gr3, vec3(x3, y3, z3));
	}
	return 96.0*(n0+n1+n2+n3);

}

// stat FBM
float fbm(vec3 p)
{
	float f;
    f  = 0.50000*simplex3D( p ); p = p*2.01;
    f += 0.25000*simplex3D( p ); p = p*2.02; //from iq
    f += 0.12500*simplex3D( p ); p = p*2.03;
    f += 0.06250*simplex3D( p ); p = p*2.04;
    f += 0.03125*simplex3D( p );
	return f;
}

void main(void)
{
	vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);
	vec2 n_uv = uv - vec2(0.5);
	n_uv.x *= adsk_result_frameratio;
	n_uv *= grunge_scale;
	vec2 p_uv = n_uv;

	// unlit texture
	vec4 t = texture2D(adsk_results_pass6, uv);
  // lit texture
  vec3 l = texture2D(adsk_results_pass9, uv).rgb;
	// blurred sun spot matte
	vec4 sun_spot = texture2D(adsk_results_pass11, uv);

	// FBM noise
	float grunge = fbm(vec3(0.2,vec2(n_uv)))*0.5+0.5;
	grunge = clamp(colorBurn(grunge, sun_spot.a), 0.0, 1.0);

  vec3 col = softLight(l, t.rgb);
  col = mix(t.rgb, col, b_high);

	// add sun spots
	vec3 s_col = col *col;
	// adding noise
	float time = 1.0;
	float p_v =0.0;
	vec2 p_tuv = p_uv;
	p_uv.x = p_tuv.x-p_tuv.y;
	p_uv.y = p_tuv.x+p_tuv.y;
	for (float i = 0.0; i<12.0; i+=1.0)
	{
		float t = mod(time+i,12.0);
		float l = time-t;
		float e = pow(1.5, t);
		p_v+=fn_noise(p_uv*e+vec2(cos(l)*53.0,sin(l)*100.0))*(1.0-(t/12.0))*(t/12.0);
	}
	p_v -= 0.5;

	float sun_noise = bias(p_v * grunge, s_bias_adj);
	//col = vec3(pp_noise * p_col + (1.0 - pp_noise) * b_col);
	col = vec3(sun_noise * s_col + (1.0 - sun_noise) * col);

  gl_FragColor = vec4(col, 1.0);
}
