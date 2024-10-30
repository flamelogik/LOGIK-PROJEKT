#version 120

// concrete noise based on https://www.shadertoy.com/view/4lfGRs by S.Guillitte
// Simplex3D noise based on https://www.shadertoy.com/view/XtBGDG by Lallis
// FBM noise by iq
// Fractal Noise based on https://www.shadertoy.com/view/Msf3Wr by mu6k
// Value Noise based on https://www.shadertoy.com/view/lsf3WH by iq
// Worley Noise  based on https://www.shadertoy.com/view/ldB3zc by iq
// Ridged Noise based on https://www.shadertoy.com/view/ldj3Dw by nimitz
// Perlin Noise based on https://www.shadertoy.com/view/MllGzs by guil
// Perlin v2 Noise based on https://www.shadertoy.com/view/MlS3z1 byRenoM
// Crawling Noise based on https://www.shadertoy.com/view/lslXRS by nimitz
// Cells on Fire based on https://www.shadertoy.com/view/lsX3z4 by JoshP
// Water Noise based on https://www.shadertoy.com/view/llsGWl by guil
// Fluid Malone Noise based on https://www.shadertoy.com/view/4s23WK by Antonalog
// Slabrie Noise based on https://www.shadertoy.com/view/ldBSDd by FatumR
// Frederic Noise based on https://www.shadertoy.com/view/4tfXzl by clayjohn
// Flow Noise based on https://www.shadertoy.com/view/Md23Wc by Antonalog
// Francis Noise based on https://www.shadertoy.com/view/ldfGWj by morgan3d
// License Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

#define PI 3.14159265359
#define tau 6.2831853
#define r_iter 6.

uniform float a_gamma;
uniform float a_contrast;
uniform float a_offset;
uniform float a_gain;
uniform float a_pivot;

/* skew constants for 3d simplex functions */
const float F3 =  0.3333333;
const float G3 =  0.1666667;

// flow noise init
vec4 dnoise(vec3 p);
vec4 quat_rotation( float half_angr, vec3 unitVec );
vec4 quat;


uniform float adsk_result_w, adsk_result_h, adsk_time, adsk_result_frameratio;
vec2 resolution = vec2(adsk_result_w, adsk_result_h);

// global uniforms
uniform float speed;
uniform float offset;
uniform float scale;
uniform float aspect;
uniform float rot;
uniform vec2 pos;
uniform int noise_type;


float time = adsk_time *.05 * speed + offset;


// concrete uniforms
uniform float c_detail;
uniform int c_noise_itt;

// fractal noise uniforms
uniform float f_detail;

// value noise uniforms
uniform int v_noise_type;

// worley uniform
uniform float w_detail;
uniform int w_color_type;

// ridged noise uniforms
uniform int r_noise_type;
uniform float r_detail;

// perlin v1 uniforms
uniform int p1_itt;
uniform float perlinv1_v;

// Plasma uniforms
uniform int plasma_iter;
uniform float plasma_detail;

// Marble uniforms
uniform int marble_iter;
uniform float marble_detail;

// Wood uniforms
uniform int wood_iter;
uniform float wood_detail;

// Clouds uniforms
uniform int cloud_iter;
uniform float cloud_detail;

// Crawling uniforms
uniform int crawling_iter;
uniform float crawling_detail;
uniform float crawling_displace;

// Cells on Fire uniforms
uniform float cof_detail;
uniform int cof_noise_type;

// Water uniforms
uniform float water_detail;
uniform float w_noise;

// Malone uniforms
uniform float malone_size, malone_swirl;
uniform int malone_detail;

// Slabrie uniforms
uniform int slabrie_detail;
uniform float slabrie_amp;

// Frédéric uniforms
uniform float fred_detail;
uniform int fred_itt;
uniform float fred_density;

// Flow Noise uniforms
uniform float flow_detail;
uniform float flow_amp;

// Francis Noise
uniform int francis_detail;
uniform float francis_amp;

// start concrete noise
float hash ( in vec2 p )
{
    return fract(sin(p.x*15.32+p.y*35.78) * 43758.23);
}

vec2 hash2 ( vec2 p )
{
	return vec2(hash(p*.754),hash(1.5743*p.yx+4.5891))-.5;
}

vec2 noise(vec2 x)
{
	vec2 add = vec2(1.0, .0);
	vec2 p = floor(x);
    vec2 f = fract(x);
    f = f*f*(3.0-2.0*f);
    return mix(mix( hash2(p), hash2(p + add.xy),f.x), mix( hash2(p + add.yx), hash2(p + add.xx),f.x),f.y);
}

vec2 fbm(vec2 x)
{
    vec2 r = x;
    float a = 1.;
    for (int i = 0; i < c_noise_itt; i++)
    {
        r += noise(r*a)/a;
		r += noise((r*a - time*0.5)+a+time);
        a = c_detail;
    }
    return (r-x)*sqrt(a);
}
// end concrete noise

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
// end Simplex3D

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
// end FBM

float hash(float x)
{
	return fract(sin(cos(x*12.13)*19.123)*17.321);
}

// start Fractal Noise
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
// end Fractal Noise

// start Value Noise
float v_hash( vec2 p )
{
	float h = dot(p,vec2(127.1,311.7));

    return -1.0 + 2.0*fract(sin(h)*43758.5453123 + time);
}

float v_noise( in vec2 p )
{
    vec2 i = floor( p );
    vec2 f = fract( p );
	vec2 u = f*f*(3.0-2.0*f);
    return mix( mix( v_hash( i + vec2(0.0,0.0) ),
                     v_hash( i + vec2(1.0,0.0) ), u.x),
                mix( v_hash( i + vec2(0.0,1.0) ),
                     v_hash( i + vec2(1.0,1.0) ), u.x), u.y);
}
// end Value Noise

// start Perlin Noise
float vnoise(vec2 x)//Value noise
{
    vec2 p = floor(x);
    vec2 f = fract(x);
    f = f*f*(3.0-2.0*f);

    return  2.*mix(mix( hash(p),hash(p + vec2(1.,0.)),f.x),
                  mix( hash(p+vec2(0.,1.)), hash(p+1.),f.x),f.y)-1.;

}
mat2 m2= mat2(.8,.6,-.6,.8);

float dvnoise(vec2 p)//Value noise + value noise with rotation
{
    return .5*(vnoise(p - time)+vnoise(m2*p + time));
}

float noise5( vec2 p)
{
    return dvnoise(p);
}

float fbm5( vec2 p ) {

	float f=5.0, a= perlinv1_v;

	float r = 0.0;
    for(int i = 0;i<p1_itt;i++)
	{
		r += a	* abs(noise5( p*f ) );
		a *= .5; f *= 2.0;
	}
	return r/2.;
}
// end Perlin Noise

vec2 g_hash( vec2 p )
{
	p = vec2( dot(p,vec2(127.1,311.7)),
			  dot(p,vec2(269.5,183.3)) );
	return -1.0 + 2.0*fract(sin(p)*43758.5453123);
}


// start Worley Noise
vec4 worley( in vec2 x, float w )
{
    vec2 n = floor( x );
    vec2 f = fract( x );

	vec4 m = vec4( 8.0, 0.0, 0.0, 0.0 );
    for( int j=-2; j<=2; j++ )
    for( int i=-2; i<=2; i++ )
    {
        vec2 g = vec2( float(i),float(j) );
        vec2 o = g_hash( n + g );

		// animate
        o = 0.5 + 0.5*sin( time + 6.2831*o );

        // distance to cell
		float d = length(g - f + o);

        // do the smoth min for colors and distances
		vec3 col = 0.5 + 0.5*sin( hash(dot(n+g,vec2(50.)))*3. + 2. + vec3(3.));
		float h = smoothstep( 0.0, 1.0, 0.5 + 0.5*(m.x-d)/w );

	    m.x   = mix( m.x,     d, h ) - h*(1.0-h)*w/(1.0+3.0*w); // distance
		m.yzw = mix( m.yzw, col, h ) - h*(1.0-h)*w/(1.0+3.0*w); // color
    }

	return m;
}
// end Worley noise

// start Ridged Noise
mat2 makem2(float theta)
{
	float c = cos(theta);
	float s = sin(theta);
	return mat2(c,-s,s,c);
}

// start Perlin v2 Noise
float p2_rand(vec2 uv)
{
    float dt = dot(uv, vec2(12.9898, 78.233));
	return fract(sin(mod(dt, PI / 2.0)) * 43758.5453);
}

float plasma_turbulence(vec2 uv, float octave, int id)
{
    float col = 0.0;
    vec2 xy;
    vec2 frac;
    vec2 tmp1;
    vec2 tmp2;
    float i2;
    float amp;
    float maxOct = octave;
    for (int i = 0; i < plasma_iter; i++)
    {
        amp = maxOct / octave;
        i2 = float(i);
        xy = id == 1 || id == 4? (uv + 50.0 * float(id) * time / (1.0 + i2)) / octave : uv / octave;
        frac = fract(xy);
        tmp1 = mod(floor(xy) + resolution.xy, resolution.xy);
        tmp2 = mod(tmp1 + resolution.xy - 1.0, resolution.xy);
        col += frac.x * frac.y * p2_rand(tmp1) / amp;
        col += frac.x * (1.0 - frac.y) * p2_rand(vec2(tmp1.x, tmp2.y)) / amp;
        col += (1.0 - frac.x) * frac.y * p2_rand(vec2(tmp2.x, tmp1.y)) / amp;
        col += (1.0 - frac.x) * (1.0 - frac.y) * p2_rand(tmp2) / amp;
        octave /= 2.0;
    }
    return (col);
}

float marble_turbulence(vec2 uv, float octave, int id)
{
    float col = 0.0;
    vec2 xy;
    vec2 frac;
    vec2 tmp1;
    vec2 tmp2;
    float i2;
    float amp;
    float maxOct = octave;
    for (int i = 0; i < marble_iter; i++)
    {
        amp = maxOct / octave;
        i2 = float(i);
        xy = id == 1 || id == 4? (uv + 50.0 * float(id) * time / (1.0 + i2)) / octave : uv / octave;
        frac = fract(xy);
        tmp1 = mod(floor(xy) + resolution.xy, resolution.xy);
        tmp2 = mod(tmp1 + resolution.xy - 1.0, resolution.xy);
        col += frac.x * frac.y * p2_rand(tmp1) / amp;
        col += frac.x * (1.0 - frac.y) * p2_rand(vec2(tmp1.x, tmp2.y)) / amp;
        col += (1.0 - frac.x) * frac.y * p2_rand(vec2(tmp2.x, tmp1.y)) / amp;
        col += (1.0 - frac.x) * (1.0 - frac.y) * p2_rand(tmp2) / amp;
        octave /= 2.0;
    }
    return (col);
}

float cloud_turbulence(vec2 uv, float octave, int id)
{
    float col = 0.0;
    vec2 xy;
    vec2 frac;
    vec2 tmp1;
    vec2 tmp2;
    float i2;
    float amp;
    float maxOct = octave;
    for (int i = 0; i < cloud_iter; i++)
    {
        amp = maxOct / octave;
        i2 = float(i);
        xy = id == 1 || id == 4? (uv + 50.0 * float(id) * time / (1.0 + i2)) / octave : uv / octave;
        frac = fract(xy);
        tmp1 = mod(floor(xy) + resolution.xy, resolution.xy);
        tmp2 = mod(tmp1 + resolution.xy - 1.0, resolution.xy);
        col += frac.x * frac.y * p2_rand(tmp1) / amp;
        col += frac.x * (1.0 - frac.y) * p2_rand(vec2(tmp1.x, tmp2.y)) / amp;
        col += (1.0 - frac.x) * frac.y * p2_rand(vec2(tmp2.x, tmp1.y)) / amp;
        col += (1.0 - frac.x) * (1.0 - frac.y) * p2_rand(tmp2) / amp;
        octave /= 2.0;
    }
    return (col);
}

float wood_turbulence(vec2 uv, float octave, int id)
{
    float col = 0.0;
    vec2 xy;
    vec2 frac;
    vec2 tmp1;
    vec2 tmp2;
    float i2;
    float amp;
    float maxOct = octave;
    for (int i = 0; i < wood_iter; i++)
    {
        amp = maxOct / octave;
        i2 = float(i);
        xy = id == 1 || id == 4? (uv + 50.0 * float(id) * time / (1.0 + i2)) / octave : uv / octave;
        frac = fract(xy);
        tmp1 = mod(floor(xy) + resolution.xy, resolution.xy);
        tmp2 = mod(tmp1 + resolution.xy - 1.0, resolution.xy);
        col += frac.x * frac.y * p2_rand(tmp1) / amp;
        col += frac.x * (1.0 - frac.y) * p2_rand(vec2(tmp1.x, tmp2.y)) / amp;
        col += (1.0 - frac.x) * frac.y * p2_rand(vec2(tmp2.x, tmp1.y)) / amp;
        col += (1.0 - frac.x) * (1.0 - frac.y) * p2_rand(tmp2) / amp;
        octave /= 2.0;
    }
    return (col);
}

vec3 p2_clouds(vec2 uv)
{
    float col = cloud_turbulence(uv, 128.0 * cloud_detail, 1) * 0.75;
    return (vec3(col - 0.1));
}

vec3 p2_marble(vec2 uv)
{
	vec2 period = vec2(3.0, 4.0);
    vec2 turb = vec2(4.0, 64.0 * marble_detail);
    float xy = uv.x * period.x / resolution.y + uv.y * period.y / resolution.x + turb.x * marble_turbulence(uv, turb.y, 2);
    float col = abs(sin(xy * PI)) * 0.75;
    return (vec3(col));
}

vec3 p2_wood(vec2 uv)
{
    vec2 iR = resolution.xy;
    float period = 3.5 * wood_detail;
    vec2 turb = vec2(0.04, 16.0);
    vec2 xy;
    xy.x = (uv.x - iR.x / 2.0) / iR.y;
    xy.y = (uv.y - iR.y / 2.0) / iR.y;
	xy.x += .88;
	xy.y += 0.5;
    float dist = length(xy) + turb.x * wood_turbulence(uv, turb.y, 3);
    float col = 0.5 * abs(sin(2.0 * period * dist * PI));
    return (vec3(col));
}

vec3 p2_plasma(vec2 uv)
{
	vec2 period = vec2(0.0, 0.0);
    vec2 turb = vec2(1.0, 128.0 * plasma_detail);
    float xy = uv.x * period.x / resolution.y + uv.y * period.y / resolution.x + turb.x * plasma_turbulence(uv, turb.y, 4);
    float col = abs(sin(xy * PI)) * 0.75;
    return (vec3(1. - col));
}

// start Crawling Noise
vec2 crawling_hash( vec2 p )
{
	p = vec2( dot(p,vec2(127.1,110.7)),
			  dot(p,vec2(269.5,45.34)) );
	return 2.0*fract(sin(p)*4378.5453123);
}

float crawling_noise( in vec2 p )
{
    vec2 i = floor( p );
    vec2 f = fract( p );
	vec2 u = f*f*(3.0-2.0*f);
    return mix( mix( dot( crawling_hash( i + vec2(0.0,0.0) ), f - vec2(0.0,0.0) ),
                     dot( crawling_hash( i + vec2(1.0,0.0) ), f - vec2(1.0,0.0) ), u.x),
                mix( dot( crawling_hash( i + vec2(0.0,1.0) ), f - vec2(0.0,1.0) ),
                     dot( crawling_hash( i + vec2(1.0,1.0) ), f - vec2(1.0,1.0) ), u.x), u.y);
}

vec2 crawling_gradn(vec2 p)
{
	float ep = 0.5 * crawling_detail;
	float gradx = crawling_noise(vec2(p.x+ep,p.y))-crawling_noise(vec2(p.x-ep,p.y));
	float grady = crawling_noise(vec2(p.x,p.y+ep))-crawling_noise(vec2(p.x,p.y-ep));
	return vec2(gradx,grady);
}

float crawling_flow(in vec2 p)
{
	time *= 0.05;
	float lava_z=2.;
	float rz = 0.;
	vec2 bp = p;
	for (float i= 1.;i < crawling_iter + 1;i++ )
	{
		//secondary flow speed (speed of the perceived flow)
		bp += time*1.9;

		//displacement field (try changing time multiplier)
		vec2 gr = crawling_gradn(i*p*.34+time);

		//rotation of the displacement field
		gr*=makem2(time*6.-(0.05*p.x+0.03*p.y)*40.);

		//displace the system
		p += gr*.5 * crawling_displace;

		//add noise octave
		rz+= (sin(crawling_noise(p)*7.)*0.5+0.5)/lava_z;

		//blend factor (blending displaced system with base system)
		//you could call this advection factor (.5 being low, .95 being high)
		p = mix(bp,p,.9);

		//intensity scaling
		lava_z *= 1.4;
		//octave scaling
		p *= 2.;
		bp *= 1.9;
	}
	return rz;
}
// end Crawling Noise

// start cells on fire
float cof_length(vec2 p) { return dot(p, p); }

float cof_noise(vec2 p){
	return fract(sin(fract(sin(p.x) * (4313.13311)) + p.y) * 3131.0011);
}

float cof_noise2(vec2 p)
{
    return fract(sin(p.x*15.32+p.y*35.78) * 43758.23);
}

float cof_worley(vec2 p)
{
	float d = 1e30;
	for (int xo = -1; xo <= 1; ++xo)
	for (int yo = -1; yo <= 1; ++yo)
	{
		vec2 tp = floor(p) + vec2(xo, yo);
		d = min(d, cof_length(p  - tp - vec2(cof_noise2(tp*time*0.00000000001))));
	}
	return 3.*exp(-4.*abs(4.*d - 1.));
}

float cof_worley2(vec2 p)
{
	float d = 1e30;
	for (int xo = -1; xo <= 1; ++xo)
	for (int yo = -1; yo <= 1; ++yo)
	{
		vec2 tp = floor(p) + vec2(xo, yo);
		d = min(d, cof_length(p  - tp - vec2(cof_noise(tp))));
	}
	return 3.*exp(-4.*abs(4.*d - 1.));
}

float cof_worley3(vec2 p)
{
	float d = 1e30;
	for (int xo = -1; xo <= 1; ++xo)
	for (int yo = -1; yo <= 1; ++yo)
	{
		vec2 tp = floor(p) + vec2(xo, yo);
		d = min(1., cof_length(p - tp - time * 0.000001 * cof_detail));
	}
	return 3.*exp(-3.*abs(4.*d - 1.));
}

float cof_fworley(vec2 p) {
	return sqrt(sqrt(sqrt(
		cof_worley(p*2. + 1.3 + time*.5) *
		cof_worley(p*4. + 2.3 - time*.25) *
		cof_worley(p*8. + 3.3 + time*.125) *
		cof_worley(p*16. + 4.3 - time*.125) *
		sqrt(cof_worley(p * 64. + 5.3 + time * .0625)) *
		sqrt(sqrt(cof_worley(p * 128. - 7.3))))));
}

float cof_fworley2(vec2 p) {
	return sqrt(sqrt(sqrt(
		cof_worley2(p*2. + 1.3 - time*.5) *
		cof_worley2(p*4. + 2.3 + time*.25) *
		cof_worley2(p*8. + 3.3 - time*.125) *
		cof_worley2(p*16. + 4.3 + time*.125) *
		sqrt(cof_worley2(p * 64. - 5.3 + time * .0625)) *
		sqrt(sqrt(cof_worley2(p * 128. + 7.3))))));
}

float cof_fworley3(vec2 p) {
	return sqrt(sqrt(sqrt(
        cof_worley3(p*2. + 1.1 + time*.5) *
		cof_worley3(p*4. + 1.1 - time*.25) *
		cof_worley3(p*8. + 1.1 + time*.125) *
		cof_worley3(p*32. + 1.1 - time*.125) *
		sqrt(cof_worley3(p * 64. + 1.1 + time * .0625)) *
		sqrt(sqrt(cof_worley3(p * 128. + 1.1))))));
}
// end cells on fire

// start water noise
vec2 m = vec2(.1,1.);

vec2 water_hash(vec2 p)
{
	return vec2(cof_noise2(p*.754),cof_noise2(1.5743*p.yx+4.5891))-.5;
}

// Gabor/Voronoi mix 4x4 kernel (clean but slower)
float water_gavoronoi4(in vec2 p)
{
    vec2 ip = floor(p);
    vec2 fp = fract(p);
    vec2 dir = m;// vec2(.9,.7);
	float f = PI * (0.5 + w_noise);
    float v = 1.;//cell variability <1.
    float dv = water_detail;//direction variability <1.
    float va = 0.0;
   	float wt = 0.0;
    for (int i=-2; i<=1; i++)
	for (int j=-2; j<=1; j++)
	{
        vec2 o = vec2(i, j);
        vec2 h = hash2(ip - o);
        vec2 pp = fp +o  -v*h;
        float d = dot(pp, pp);
        float w = exp(-d*2.);
        wt +=w;
      	h= dv*h+dir;//h=normalize(h+dir);
        va +=cos(dot(pp,h)*f)*w;
	}
    return va/wt;
}

float water_noise( vec2 p)
{
    return water_gavoronoi4(p);
}

float water_fbmabs( vec2 p ) {

	float f=1.;

	float r = 0.0;
    for(int i = 0;i<5;i++){
		r += abs(water_noise( p*f ))/f;
	    f *=2.2;
        p+=vec2(-.01,.07)*r+.2*m*time/(.1-f);
	}
	return r;
}

float water_map(vec2 p){

    return 1. - water_fbmabs(p);
}
// end water noise

// start malone noise
vec2 Rot(vec2 p, float t) {
	float c = cos(t); float s = sin(t);
	return vec2(p.x*c+p.y*s,
				-p.x*s+p.y*c);
}
vec2 RotCS(vec2 p, float c, float s) {
	return vec2( p.x*c+p.y*s,
				-p.x*s+p.y*c);
}

//iq 2d simplex noise
vec2 malone_hash( vec2 p )
{
	p = vec2( dot(p,vec2(127.1,311.7)),
			  dot(p,vec2(269.5,183.3)) );
	vec2 h = -1.0 + 2.0*fract(sin(p)*43758.5453123);
	//extra rotations for more flow!
	float t = -time*0.7;
	float co = cos(t); float si = sin(t);
	h = RotCS(h,co,si);
	return h;
}

float malone_noise( in vec2 p )
{
    const float K1 = 0.366025404; // (sqrt(3)-1)/2;
    const float K2 = 0.211324865; // (3-sqrt(3))/6;
	vec2 i = floor( p + (p.x+p.y)*K1 );
    vec2 a = p - i + (i.x+i.y)*K2;
    vec2 o = (a.x>a.y) ? vec2(1.0,0.0) : vec2(0.0,1.0);
    vec2 b = a - o + K2;
	vec2 c = a - 1.0 + 2.0*K2;
	float t = time*.5;
	float co = cos(t); float si = sin(t);
	a = RotCS(a,co,si);
	b = RotCS(b,co,si);
	c = RotCS(c,co,si);
    vec3 h = max( 0.5-vec3(dot(a,a), dot(b,b), dot(c,c) ), 0.0 );
	vec3 n = h*h*h*h*vec3( dot(a,malone_hash(i+0.0)), dot(b,malone_hash(i+o)), dot(c,malone_hash(i+1.0)));
    return dot( n, vec3(100.) );
}

vec3 random3(vec3 c) {
	float j = 4096.0*sin(dot(c,vec3(17.0, 59.4, 15.0)));
	vec3 r;
	r.z = fract(512.0*j);
	j *= .125;
	r.x = fract(512.0*j);
	j *= .125;
	r.y = fract(512.0*j);
	r = r-0.5;
	//rotate for extra flow!
	float t = -time*.5;
	r.xy = Rot(r.xy,t);
	return r;
}

/* 3d simplex noise */
float malone_noise(vec3 p) {
	 /* 1. find current tetrahedron T and its four vertices */
	 /* s, s+i1, s+i2, s+1.0 - absolute skewed (integer) coordinates of T vertices */
	 /* x, x1, x2, x3 - unskewed coordinates of p relative to each of T vertices*/

	 /* calculate s and x */
	 vec3 s = floor(p + dot(p, vec3(F3)));
	 vec3 x = p - s + dot(s, vec3(G3));

	 /* calculate i1 and i2 */
	 vec3 e = step(vec3(0.0), x - x.yzx);
	 vec3 i1 = e*(1.0 - e.zxy);
	 vec3 i2 = 1.0 - e.zxy*(1.0 - e);

	 /* x1, x2, x3 */
	 vec3 x1 = x - i1 + G3;
	 vec3 x2 = x - i2 + 2.0*G3;
	 vec3 x3 = x - 1.0 + 3.0*G3;

	 /* 2. find four surflets and store them in d */
	 vec4 w, d;

	 /* calculate surflet weights */
	 w.x = dot(x, x);
	 w.y = dot(x1, x1);
	 w.z = dot(x2, x2);
	 w.w = dot(x3, x3);

	 /* w fades from 0.6 at the center of the surflet to 0.0 at the margin */
	 w = max(0.6 - w, 0.0);

	 /* calculate surflet components */
	 d.x = dot(random3(s), x);
	 d.y = dot(random3(s + i1), x1);
	 d.z = dot(random3(s + i2), x2);
	 d.w = dot(random3(s + 1.0), x3);

	 /* multiply d by w^4 */
	 w *= w;
	 w *= w;
	 d *= w;

	 /* 3. return the sum of the four surflets */
	 return dot(d, vec4(52.0));
}

float pot(vec2 pos)
{
	vec3 p = vec3(pos,1.0);
	float n = malone_noise(p);
	n += 0.5 *malone_noise(p*2.13);
	n += 3. * malone_noise(pos*0.333);
	return n;
}

vec2 field(vec2 pos)
{
	float s = 1.0 * malone_swirl;
	pos *= s;
	float n = pot(pos);
	float e = 0.1;
	float nx = pot(vec2(pos+vec2(e,0.)));
	float ny = pot(vec2(pos+vec2(0.,e)));
	return vec2(-(ny-n),nx-n)/e;
}
// end malone noise

// start slabrie noise
float slabrie_rand(vec2 co){
   return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}

// Rough Value noise implementation
float slabrie_valueNoiseSimple(vec2 vl) {
   float minStep = 1.0 ;

   vec2 grid = floor(vl);
   vec2 gridPnt1 = grid;
   vec2 gridPnt2 = vec2(grid.x, grid.y + minStep);
   vec2 gridPnt3 = vec2(grid.x + minStep, grid.y);
   vec2 gridPnt4 = vec2(gridPnt3.x, gridPnt2.y);

    float s = slabrie_rand(grid);
    float t = slabrie_rand(gridPnt3);
    float u = slabrie_rand(gridPnt2);
    float v = slabrie_rand(gridPnt4);

    float x1 = smoothstep(0., 1., fract(vl.x));
    float interpX1 = mix(s, t, x1);
    float interpX2 = mix(u, v, x1);

    float y = smoothstep(0., 1., fract(vl.y));
    float interpY = mix(interpX1, interpX2, y);

    return interpY;
}

float slabrie_fractalNoise(vec2 vl) {
    float persistance = 2.0;
    float amplitude = 0.58 * slabrie_amp;
    float rez = 0.0;
    vec2 p = vl;

    for (float i = 0; i < slabrie_detail; i++) {
        rez += amplitude * slabrie_valueNoiseSimple(p);
        amplitude /= persistance;
        p *= persistance;
    }
    return rez;
}

float slabrie_complexFBM(vec2 p) {
    float slow = time;
    float fast = time;
    vec2 offset1 = vec2(slow, 0.); // Main front
    vec2 offset2 = vec2(slabrie_valueNoiseSimple(p + fast) * 2., 0.); // sub fronts

    return slabrie_fractalNoise( p + offset1 + slabrie_fractalNoise(
        						p + slabrie_fractalNoise(
                        			p + 2. * slabrie_fractalNoise(p - offset2)
                                )
    						)
    					);
}
// end slabrie noise

// start frederic noise
float fred_hash( float n )
{
    return fract(sin(n)*43758.5453);
}

float fred_noise( vec2 x )
{
    vec2 p = floor(x);
    vec2 f = fract(x);
    f = f*f*(3.0-2.0*f);
    float n = p.x + p.y*57.0 + 113.0*p.y;
    float res = mix(mix(mix( fred_hash(n+  0.0), fred_hash(n+  1.0),f.x),
                        mix( fred_hash(n+ 57.0), fred_hash(n+ 58.0),f.x),f.y),
                    mix(mix( fred_hash(n+113.0), fred_hash(n+114.0),f.x),
                        mix( fred_hash(n+170.0), fred_hash(n+171.0),f.x),f.y),f.y);
    return res;
}

float fred_fbm( vec2 x) {
    float h = 0.0;

    for (float i=1;i<fred_itt;i++) {
        h+=fred_noise(x*pow(1.6, i))* 0.9 * fred_density * pow(0.6, i);
    }
    return h;
}

float fred_warp(vec2 p, float mm)
{
    float m = fred_detail;
    vec2 q = vec2(fred_fbm(vec2(p)), fred_fbm(p+vec2(5.12*time*0.01, 1.08)));
    vec2 r = vec2(fred_fbm((p+q*m)+vec2(0.1, 4.741)), fred_fbm((p+q*m)+vec2(1.952, 7.845)));
    m /= mm;
    return fred_fbm(p+r*m);
}

// end frederic noise

// start Flow Noise
vec4 FlowNoise(vec3 uvw, vec2 uv)
{
	vec4 n = vec4(0.);
	float f = 1.;
	float a = 1.;

	vec3 ax = normalize(vec3(1,1,1));
	float e = 0.1;//*f;
	float ang;
	vec4 dn;
		ang = time*.4+uv.y*0.5;
		quat = quat_rotation( ang*2.*f, normalize(ax) );
		dn = dnoise(uvw);
		uvw -= 0.01 * flow_amp *dn.xyz;
		n += abs(a*dn);
		uvw *= flow_detail;
		f *= flow_detail;
		a *= (1./flow_detail);

		ang = time*.4+uv.y*0.5;
		quat = quat_rotation( ang*2.*f, normalize(ax) );
		dn = dnoise(uvw);
		uvw -= 0.01 * flow_amp *dn.xyz;
		n += abs(a*dn);
		uvw *= flow_detail;
		f *= flow_detail;
		a *= (1./flow_detail);

		ang = time*.4+uv.y*0.5;
		quat = quat_rotation( ang*2.*f, normalize(ax) );
		dn = dnoise(uvw);
		uvw -= 0.01 * flow_amp *dn.xyz;
		n += abs(a*dn);
		uvw *= flow_detail;
		f *= flow_detail;
		a *= (1./flow_detail);

		ang = time*.4+uv.y*0.5;
		quat = quat_rotation( ang*2.*f, normalize(ax) );
		dn = dnoise(uvw);
		uvw -= 0.01 * flow_amp *dn.xyz;
		n += abs(a*dn);
		uvw *= flow_detail;
		f *= flow_detail;
		a *= (1./flow_detail);

		ang = time*.4+uv.y*0.5;
		quat = quat_rotation( ang*2.*f, normalize(ax) );
		dn = dnoise(uvw);
		uvw -= 0.01 * flow_amp *dn.xyz;
		n += abs(a*dn);
		uvw *= flow_detail;
		f *= flow_detail;
		a *= (1./flow_detail);

	return n;
}

//thanks iq..
// Smooth HSV to RGB conversion
vec3 hsv2rgb_smooth( in vec3 c )
{
    vec3 rgb = clamp( abs(mod(c.x*1.0+vec3(0.0,1.0,1.0),1.0)-1.0)-1.0, 0.0, 1.0 );

	rgb = rgb*rgb*(3.0-2.0*rgb); // cubic smoothing

	return vec3((c.y -.4) * 1.05);
}

vec3 FlameColour(float f)
{
	return hsv2rgb_smooth(vec3((f-(2.25/6.))*(1.25/6.),f*1.25+.2,f*.95));
}

vec4 quat_rotation( float half_angr, vec3 unitVec )
{
    float s, c;
    s = sin( half_angr );
    c = cos( half_angr );
    return vec4( unitVec*s, c );
}

vec3 quat_times_vec(vec4 q, vec3 v)
{
	//http://molecularmusings.wordpress.com/2013/05/24/a-faster-quaternion-vector-multiplication/
	vec3 t = 2. * cross(q.xyz, v);
	return v + q.w * t + cross(q.xyz, t);
}

/* Created by Nikita Miropolskiy, nikat/2013
 * This work is licensed under a
 * Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
 * http://creativecommons.org/licenses/by-nc-sa/3.0/
 *  - You must attribute the work in the source code
 *    (link to https://www.shadertoy.com/view/XsX3zB).
 *  - You may not use this work for commercial purposes.
 *  - You may distribute a derivative work only under the same license.
 */

/* discontinuous pseudorandom uniformly distributed in [-0.5, +0.5]^3 */
vec3 random4(vec3 c)
{
	float j = 4096.0*sin(dot(c,vec3(17.0, 59.4, 15.0)));
	vec3 r;
	r.z = fract(512.0*j);
	j *= .125;
	r.x = fract(512.0*j);
	j *= .25;
	r.y = fract(512.0*j);
	r = r-0.5;

	//rotate for extra flow!
	r=quat_times_vec(quat,r);

	return r;
}

vec4 dnoise(vec3 p)
{
	 /* 1. find current tetrahedron T and its four vertices */
	 /* s, s+i1, s+i2, s+1.0 - absolute skewed (integer) coordinates of T vertices */
	 /* x, x1, x2, x3 - unskewed coordinates of p relative to each of T vertices*/

	 vec3 s = floor(p + (p.x+p.y+p.z)*F3);
	 vec3 x = p - s + (s.x+s.y+s.z)*G3;

	 vec3 e = step(vec3(0.0), x - x.yzx);
	 vec3 i1 = e*(1.0 - e.zxy);
	 vec3 i2 = 1.0 - e.zxy*(1.0 - e);

	 vec3 x1 = x - i1 + G3;
	 vec3 x2 = x - i2 + 2.0*G3;
	 vec3 x3 = x - 1.0 + 3.0*G3;

	 /* calculate surflet weights */
	 vec4 w;
	 w.x = dot(x, x);
	 w.y = dot(x1, x1);
	 w.z = dot(x2, x2);
	 w.w = dot(x3, x3);

	 /* w fades from 0.6 at the center of the surflet to 0.0 at the margin */
	 w = max(0.6 - w, 0.0);		//aka t0,t1,t2,t3
	 vec4 w2 = w*w;				//aka t20,t21,t22,t23
	 vec4 w4 = w2*w2;			//aka t40,t41,t42,t43

	 /* 2. find four surflets and store them in d */
	 vec3 g0 = random4(s);
	 vec3 g1 = random4(s + i1);
	 vec3 g2 = random4(s + i2);
	 vec3 g3 = random4(s + 1.0);

	 vec4 d;
	 /* calculate surflet components */
	 d.x = dot(g0, x);		//aka graddotp3( gx0, gy0, gz0, x0, y0, z0 )
	 d.y = dot(g1, x1);
	 d.z = dot(g2, x2);
	 d.w = dot(g3, x3);

	 //derivatives as per
	 //http://webstaff.itn.liu.se/~stegu/aqsis/flownoisedemo/srdnoise23.c
	 vec4 w3 = w*w2;
	 vec4 temp = w3*d;
	 vec3 dnoise = temp[0]*x;
	     dnoise += temp[1]*x1;
	     dnoise += temp[2]*x2;
		 dnoise += temp[3]*x3;
		 dnoise *= -8.;
		 dnoise += w4[0]*g0+w4[1]*g1+w4[2]*g2+w4[3]*g3;
		 dnoise *= 52.; //???

	 d *= w4;	//aka n0,n1,n2,n3

	float n = (d.x+d.y+d.z+d.w)*52.;

	return vec4(dnoise,n);
}
// end Flow Noise


// start Francis Noise
float f_hash(float n)
{
    return fract(sin(n) * 43758.5453123);
}

// Value noise generator. Returns
// three values on [-1, +1]
vec3 noised(vec2 x) {
    vec2 p = floor(x);
    vec2 f = fract(x);

	// The constant for tileWidth doesn't matter much unless it is too small
    const float tileWidth = 1024.0;
    float n = p.x + p.y * tileWidth;

    // Grab noise values at four corners of a square
    float a = f_hash(n +  0.0);
    float b = f_hash(n +  1.0);
    float c = f_hash(n + tileWidth);
    float d = f_hash(n + tileWidth + 1.0);

    // use smoothstep-filtered lerp for one component and compute the derivatives for the others
	// See http://www.iquilezles.org/www/articles/morenoise/morenoise.htm

    // The (negative) smoothstep weight
    vec2 u = f * f * (3.0 - 2.0 * f);
	return vec3(a+(b-a)*u.x+(c-a)*u.y+(a-b-c+d)*u.x*u.y,
				60.0*f*f*(f*(f-2.0)+1.0)*(vec2(b-a,c-a)+(a-b-c+d)*u.yx));
}

// On the range [0, 1].  This is the sum
// of a convergent series http://en.wikipedia.org/wiki/Series_(mathematics)#Convergent_series,
// where each term has a pseudorandom weight on [-1, 1].  The largest sum is therefore
// 2 (the smallest is -2), and the final line of code rescales this to the unit interval.
//
float heightfieldFcn(vec2 P) {
    const mat2 M2 = mat2( 0.5, 1.0, -1.0, .5);
    float height = 0.0;
	vec2 d = vec2(0.0);

    // Magnitude at this octave
    float magnitude = 0.5;

    // Add multiple octaves of noise, chosen from points that spiral outward
    // to avoid hitting the tiling period of the noise function.
    for (int i = 0; i < francis_detail; ++i) {
        vec3 n = noised(P+time);
        d += n.yz;

        // The 1 + |d|^2 denominator creates the mountainous lumpiness.
        // Without it, this is a standard value noise function.
        height += magnitude * n.x / (1.0 + dot(d, d));
        P = M2 * P;
		magnitude *= 0.5 * francis_amp;
    }

	// iq's original had 0.5 here, but that doesn't fit the range
    return height * 0.5 + 0.2;
}

float gam( float front, float val )
{
   float igam = 1.0 / clamp( val, 1e-5, 100.0 );
   return pow( max( front, 0.0 ), igam );
}

float gain( float front, float val )
{
   return front * val * 0.01;
}

float off( float front, float val )
{
   return front + val;
}

float con( float front, float val )
{
   return (front - 0.5 ) * val * 0.01 + 0.5;
}


void main()
{
	vec2 uv = (gl_FragCoord.xy / resolution.xy) - pos;
    vec4 col = vec4(0.0);
	uv.x *= adsk_result_frameratio;
	float rad_rot = (rot+180.0) * PI / 180.0;
	mat2 rotation = mat2( cos(-rad_rot), -sin(-rad_rot), sin(-rad_rot), cos(-rad_rot));
	uv *= rotation;
	uv.x *= aspect;
	uv *= scale;

	if ( noise_type == 1 )
	{
		// concrete noise
	    vec2 p = fbm(uv)+2.;
	    float c = length(p);
	    col.rgb = vec3(p.y)*c/15.;
	}

	else if ( noise_type == 2 )
	{
		// FBM noise
   		float n = fbm(vec3(time * 0.2,vec2(uv)))*0.5+0.5;
		col.rgb = vec3(n);
	}

	else if ( noise_type == 3 )
	{
		// Simplex3D noise
		float n = simplex3D(vec3(time,vec2(uv)))*0.5+0.5;
		col.rgb = vec3(n);
	}

	else if ( noise_type == 4 )
	{
		float v =0.0;
		vec2 tuv = uv / 10.;
		uv.x = tuv.x-tuv.y;
		uv.y = tuv.x+tuv.y;
		for (float i = 0.0; i<12.0; i+=1.0)
		{
			float t = mod(time+i,12.0);
			float l = time-t;
			float e = pow(1.4 * f_detail, t);
			v+=fn_noise(uv*e+vec2(cos(l)*53.0,sin(l)*100.0))*(1.0-(t/12.0))*(t/12.0);
		}
		v-=0.5;
		col = vec4(v);
	}

	else if ( noise_type == 5 )
	{
		float f = 0.0;

		if ( v_noise_type == 0 )
		{
			f = v_noise( uv * 4.);
			f = 0.5 + 0.5*f;
		}

		else if ( v_noise_type == 1 )
		{
			uv *= 3.0;
	        mat2 m = mat2( 1.6,  1.2, -1.2,  1.6 );
			f  = 0.5000*v_noise( uv ); uv = m*uv;
			f += 0.2500*v_noise( uv ); uv = m*uv;
			f += 0.1250*v_noise( uv ); uv = m*uv;
			f += 0.0625*v_noise( uv ); uv = m*uv;
			f = 0.5 + 0.5*f;
		}
		col.rgb = vec3(f);

	}

	else if ( noise_type == 8 )
	{
	    uv *= scale * 0.1;
	    vec4 c = worley( uv, w_detail);
		col.rgb = c.yzw;

		if ( w_color_type == 0 )
			col.rgb;
		else if ( w_color_type == 1 )
		   	col.rgb *= 1.0 - 0.8*c.x;
	   	else if ( w_color_type == 2 )
			col.rgb *= mix(c.x,1.0,0.0);
	   	else if ( w_color_type == 3 )
			col.rgb = c.xxx*0.8;
	}

	else if ( noise_type == 9 )
	{
		uv *= scale;
		vec2 rz;
		mat2 m2 = makem2(tau/(6.+3.));
		float z=2.;

		if ( r_noise_type == 0 )
		{
			//base fbm noise
			for (float i= 1.;i < r_iter;i++ )
			{
				rz+= noise(uv)/z;
				z = z*.7;
				uv = uv*m2*r_detail;
			}
		}

		else if ( r_noise_type == 1 )
		{
			//sinus+fbm noise
			for (float i= 1.;i < r_iter;i++ )
			{
				rz+= (sin(noise(uv)*7.)*0.5+0.5) /z;
				z = z*2.;
				uv = uv*m2*r_detail;
			}
		}
		else if ( r_noise_type == 2 )
		{
			//ridged/turbulent noise (triangle wave + fbm)
			for (float i= 1.;i < r_iter;i++ )
			{
				rz+= abs((noise(uv)-0.5)*2.)/z;
				z *= 7.;
				uv = uv*r_detail*m2;
			}
		}
		else if ( r_noise_type == 3 )
		{
			//high frenquency sinus
			for (float i= 1.;i < r_iter;i++ )
			{
				rz+= (sin(noise(uv)*25.)*0.5+0.5) /z;
				z = z*2.;
				uv = uv*m2*r_detail;
			}
		}
		col.rgb = vec3(rz.x);
	}

	else if ( noise_type == 10 )
	{
		float r;
	    r = fbm5(uv* 0.3);
	    r = 4.5*r-1.;
		col.rgb = clamp(vec3(r*r),0.,1.);
	}

	else if ( noise_type == 11 )
	{
		uv *= 200.0;
		col.rgb = vec3(p2_plasma(uv));
	}

	else if ( noise_type == 12 )
	{
		uv *= 200.0;
		col.rgb = vec3(p2_marble(uv / 2.0));
	}

	else if ( noise_type == 13 )
	{
		uv *= 200.0;
		col.rgb = vec3(p2_wood(uv));
	}

	else if ( noise_type == 14 )
	{
		uv *= 200.0;
		col.rgb = vec3(p2_clouds(uv));
	}

	else if ( noise_type == 15 )
	{
		uv*= -.2;
		uv.y += 17.0;
		float rz = crawling_flow(uv);
		col.rgb = vec3(rz*.68);
	}

	else if ( noise_type == 16 )
	{
		float t = 0.0;
		if ( cof_noise_type == 0 )
			t = cof_fworley2(uv * .1);
		else if ( cof_noise_type == 1 )
			t = cof_fworley(uv * .05);
		else if ( cof_noise_type == 2 )
			t = cof_fworley3(uv * .01);
		col.rgb = vec3(t);
	}

	else if ( noise_type == 17 )
	{
		uv *= -0.3;
	   	uv += m * time * .1;
	    float k = water_map(uv)*.8+.25;
		col.rgb = vec3(clamp(k, 0.0, 1.0));
	}

	else if ( noise_type == 18 )
	{
		uv.x += 50.5;
		uv *= 0.25;
		vec2 src_uv = uv;
		vec3 d = vec3(0.);
		for (int i=0; i<malone_detail; i++)
		{
			vec2 new_uv = field(uv)*.00825*.5;
			uv += new_uv;
		}
		col.rgb = vec3(malone_noise(uv*malone_size));
		col.rgb = 0.5 + 0.5 * col.rgb;
		col.rgb = clamp(col.rgb, 0.0, 1.0);
	}

	else if ( noise_type == 19 )
	{
		uv.x += 50.5;
		uv *= 0.25;
		float slabrie_rot = 70. * PI / 180.0;
		mat2 rotation = mat2( cos(-slabrie_rot), -sin(-slabrie_rot), sin(-slabrie_rot), cos(-slabrie_rot));
		uv *= rotation;
		col.rgb = mix(vec3(1.0), vec3(.0), slabrie_complexFBM(uv));
	}

	else if ( noise_type == 20 )
	{
		uv.x += 50.5;
		float fred_rot = 90. * PI / 180.0;
		mat2 rotation = mat2( cos(-fred_rot), -sin(-fred_rot), sin(-fred_rot), cos(-fred_rot));
		uv *= rotation;
		vec2 f_uv = uv * resolution.xy * 0.4 ;
		f_uv += vec2(time* 150., 0.0);
	    float f_col = fred_warp(f_uv*0.0004, 12.0+fred_fbm(f_uv*0.0005)*16.0);
		col.rgb = vec3((f_col-0.3)*1.46);
	}

	else if ( noise_type == 21 )
	{
		uv *=0.25;
		float t = 20.74+offset;
		vec3 uvw = vec3(uv*1.15+vec2(0.,t),t*0.5);
		vec4 d = FlowNoise(uvw,uv);
		float de = d.w;
		de = length(d.xyz)*.15+.2-d.w*.2;
		vec3 n = FlameColour(de);
		col.rgb = vec3(n);
	}

	else if ( noise_type == 22 )
	{
		col.rgb = vec3(heightfieldFcn(uv * 0.5));
	}

  col.r = gam( col.r, a_gamma );
  col.r = gain( col.r, a_gain );
  col.r = off( col.r, a_offset );
  col.r = con( col.r, a_contrast );

	col.rgb = clamp(col.rrr, 0.0, 1.0);
	gl_FragColor = col;
}
