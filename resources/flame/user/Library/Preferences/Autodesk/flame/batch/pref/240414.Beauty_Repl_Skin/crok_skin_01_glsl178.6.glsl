#version 120

uniform sampler2D adsk_results_pass1, adsk_results_pass2, adsk_results_pass5;
uniform float adsk_result_w, adsk_result_h, adsk_result_frameratio;
vec2 resolution = vec2(adsk_result_w, adsk_result_h);
uniform float sharpness, som_sharpness;
uniform float f_detail, bias_adj;
uniform float p_scale, p_bias_adj, p_gain, p_con, p_detail;
uniform float sun_scale;
uniform bool sommer;
uniform vec3 base_skin_col;

#define HASHSCALE1 .1031
#define HASHSCALE3 vec3(.1031, .1030, .0973)


vec4 normal( vec4 s, vec4 d )
{
	return s;
}

float bias(float x, float b)
{
    b = -log2(1.0 - b);
    return 1.0 - pow(1.0 - pow(x, 1./b), b);
}

vec3 colorBurn( vec3 s, vec3 d )
{
	return 1.0 - (1.0 - d) / s;
}

// start Fractal Noise
/*
float hash(float x)
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

// start Worley Noise
/*
vec2 g_hash( vec2 p )
{
	p = vec2( dot(p,vec2(127.1,311.7)),
			  dot(p,vec2(269.5,183.3)) );
	return -1.0 + 2.0*fract(sin(p)*43758.5453123);
}*/

vec2 g_hash(vec2 p)
{
	vec3 p3 = fract(vec3(p.xyx) * HASHSCALE3);
    p3 += dot(p3, p3.yzx+19.19);
    return fract((p3.xx+p3.yz)*p3.zy);

}

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
        o = 0.5 + 0.5*sin( 1.0 + 6.2831*o );

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

// Real contrast adjustments by  Miles
vec3 adjust_contrast(vec3 col, vec4 con)
{
	vec3 c = con.rgb * vec3(con.a);
	vec3 t = (vec3(1.0) - c) / vec3(2.0);
	t = vec3(.5);
	col = (1.0 - c.rgb) * t + c.rgb * col;
return col;
}

void main()
{
	vec2 uv = (gl_FragCoord.xy / resolution.xy);
	vec2 n_uv = uv - vec2(0.5);
	n_uv.x *= adsk_result_frameratio;
	vec2 p_uv = n_uv;
	vec2 sun_uv = n_uv;

	vec3 col = vec3(0.0);
	vec3 skin_c = texture2D( adsk_results_pass1, uv ).rgb;
	vec3 som_c = texture2D( adsk_results_pass2, uv ).rgb;
	vec3 matte = texture2D( adsk_results_pass5, uv ).rgb;
	skin_c -= texture2D( adsk_results_pass1, uv.xy+0.0001).rgb*sharpness*15.;
	skin_c += texture2D( adsk_results_pass1, uv.xy-0.0001).rgb*sharpness*15.;

	col = skin_c;


	if ( sommer )
	{
		som_c -= texture2D( adsk_results_pass2, uv.xy+0.0001).rgb * som_sharpness*15.;
		som_c += texture2D( adsk_results_pass2, uv.xy-0.0001).rgb * som_sharpness*15.;

		col = vec3(matte * som_c + (1.0 - matte) * skin_c);
	}

	// adding noise
	float n_time = 10.54350;
	float v =0.0;
	vec2 tuv = n_uv;
	n_uv.x = tuv.x-tuv.y;
	n_uv.y = tuv.x+tuv.y;
	for (float i = 0.0; i<12.0; i+=1.0)
	{
		float t = mod(n_time+i,12.0);
		float l = n_time-t;
		float e = pow(f_detail * 0.1, t);
		v+=fn_noise(n_uv*e+vec2(cos(l)*53.0,sin(l)*100.0))*(1.0-(t/12.0))*(t/12.0);
	}
	v-=0.5;
	float noise = bias(v, bias_adj);
	vec3 b_col = vec3(noise * col + (1.0 - noise) * base_skin_col);

	// pores
	vec4 c = worley(p_uv * p_scale, 1.0);
	vec3 p_noise = c.yzw;
	p_noise.rgb = c.xxx*0.8;
	p_noise = adjust_contrast(p_noise, vec4(0.95));
	p_noise = clamp(p_noise * 0.9, 0.0, 1.0);
	vec3 p_col = mix(b_col, colorBurn(p_noise, b_col), 0.1);
	// adding noise
	float p_time = 5.342;
	float p_v =0.0;
	vec2 p_tuv = p_uv;
	p_uv.x = p_tuv.x-p_tuv.y;
	p_uv.y = p_tuv.x+p_tuv.y;
	for (float i = 0.0; i<12.0; i+=1.0)
	{
		float t = mod(p_time+i,12.0);
		float l = p_time-t;
		float e = pow(p_detail * 0.1, t);
		p_v+=fn_noise(p_uv*e+vec2(cos(l)*53.0,sin(l)*100.0))*(1.0-(t/12.0))*(t/12.0);
	}
	p_v -= 0.5;
	float pp_noise = bias(p_v, p_bias_adj);
	col = vec3(pp_noise * p_col + (1.0 - pp_noise) * b_col);

	//adding sun spots
	vec4 sun_c = worley(sun_uv * sun_scale, 1.0);
	vec3 sun_noise = sun_c.yzw;
	sun_noise.rgb = sun_c.xxx;
	sun_noise = clamp(sun_noise, 0.0, 1.0);
	sun_noise = 1.0 - sun_noise;
	sun_noise = pow(sun_noise, vec3(3.0));
	sun_noise = adjust_contrast(sun_noise, vec4(2.0));


	col = clamp(col, 0.0, 1.0);
	gl_FragColor = vec4(col, sun_noise.r);
}
