uniform float adsk_result_w, adsk_result_h, adsk_result_frameratio;
uniform sampler2D adsk_results_pass4, Source, Alpha;
uniform float blend, gamma, uv_scale, alan_aspect;
uniform vec3 levels;
uniform vec3 size;

uniform int stock, blend_mode, output_matte;
uniform bool grain_only;

float overlay( float s, float d )
{
	return (d < 0.5) ? 2.0 * s * d : 1.0 - 2.0 * (1.0 - s) * (1.0 - d);
}

vec3 overlay( vec3 s, vec3 d )
{
	vec3 c;
	c.x = overlay(s.x,d.x);
	c.y = overlay(s.y,d.y);
	c.z = overlay(s.z,d.z);
	return c;
}

vec3 spotlight( vec3 s, vec3 d )
{
	vec3 c = 2.0 * d * s;
	return c;
}

vec3 add( vec3 s, vec3 d )
{
	vec3 c = s - 0.5 + d;
	return c;
}

void main(void)
{
	vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);

	vec3 front = texture2D(Source, uv).rgb;
	vec3 col = vec3(0.0);
	vec2 uv_r = vec2(0.0);
	vec2 uv_g = vec2(0.0);
	vec2 uv_b = vec2(0.0);
  vec3 matte = texture2D(Source, uv).rgb;
	vec3 alpha = texture2D(Alpha, uv).rgb;
	vec3 p_level = vec3(0.0, 1.0, 1.0);
	vec4 fin_col = vec4(0.0);
	float p_aspect = 1.0;
	float p_scale = 1.0;

// Kodak 5245
	if ( stock == 0)
	{
		//p_level = vec3(5.08, 0.29, 5.36);
	    matte = min(max(matte - vec3(p_level.x), vec3(0.0)) / (vec3(p_level.z) - vec3(p_level.x)), vec3(1.0));
	    matte = pow(matte, vec3(p_level.y));
	}

// Kodak 5248
	else if ( stock == 1)
	{
		//p_level = vec3(5.08, 0.29, 5.36);
	    matte = min(max(matte - vec3(p_level.x), vec3(0.0)) / (vec3(p_level.z) - vec3(p_level.x)), vec3(1.0));
	    matte = pow(matte, vec3(p_level.y));
	}

// Kodak 5287
	else if ( stock == 2)
	{
		//p_level = vec3(5.08, 0.29, 5.36);
	    matte = min(max(matte - vec3(p_level.x), vec3(0.0)) / (vec3(p_level.z) - vec3(p_level.x)), vec3(1.0));
	    matte = pow(matte, vec3(p_level.y));
	}

// Kodak 5293
	else if ( stock == 3)
	{
		//p_level = vec3(5.08, 0.29, 5.36);
	    matte = min(max(matte - vec3(p_level.x), vec3(0.0)) / (vec3(p_level.z) - vec3(p_level.x)), vec3(1.0));
	    matte = pow(matte, vec3(p_level.y));
	}

// Kodak 5296
	else if ( stock == 4)
	{
		//p_level = vec3(5.08, 0.29, 5.36);
	    matte = min(max(matte - vec3(p_level.x), vec3(0.0)) / (vec3(p_level.z) - vec3(p_level.x)), vec3(1.0));
	    matte = pow(matte, vec3(p_level.y));
	}

// Kodak 5298
	else if ( stock == 5)
	{
		//p_level = vec3(0.0, .29, 1.00);
	    matte = min(max(matte - vec3(p_level.x), vec3(0.0)) / (vec3(p_level.z) - vec3(p_level.x)), vec3(1.0));
	    matte = pow(matte, vec3(p_level.y));
	}


// Kodak 5217
	if ( stock == 6)
	{
	    matte = min(max(matte - vec3(p_level.x), vec3(0.0)) / (vec3(p_level.z) - vec3(p_level.x)), vec3(1.0));
	    matte = pow(matte, vec3(p_level.y));
	}

// Kodak 5218
	if ( stock == 7)
	{
	    matte = min(max(matte - vec3(p_level.x), vec3(0.0)) / (vec3(p_level.z) - vec3(p_level.x)), vec3(1.0));
	    matte = pow(matte, vec3(p_level.y));
	}

// Kodak BW
	if ( stock == 8)
	{
		//p_level = vec3(2.0, 1.0, 1.0);
	  matte = min(max(matte - vec3(p_level.x), vec3(0.0)) / (vec3(p_level.z) - vec3(p_level.x)), vec3(1.0));
	  matte = pow(matte, vec3(p_level.y));
	}

// Custom grain stock
	if (stock == 9)
	{
	    //levels input range
	    matte = min(max(matte - vec3(levels.r), vec3(0.0)) / (vec3(levels.b) - vec3(levels.r)), vec3(1.0));
	    //gamma correction
	    matte = pow(abs(matte), vec3(levels.g));
	}

	// Custom grain stock
		if (stock == 12)
		{
		    //levels input range
		    matte = min(max(matte - vec3(levels.r), vec3(0.0)) / (vec3(levels.b) - vec3(levels.r)), vec3(1.0));
		    //gamma correction
		    matte = pow(abs(matte), vec3(levels.g));
		}

// Alan Skin BW
	if ( stock == 10 )
	{
		p_aspect = 0.18;
		p_scale = 2.6;
	}

// Kodak BW
	if ( stock == 11)
	{
		//p_level = vec3(2.0, 1.0, 1.0);
	    matte = min(max(matte - vec3(p_level.x), vec3(0.0)) / (vec3(p_level.z) - vec3(p_level.x)), vec3(1.0));
	    matte = pow(matte, vec3(p_level.y));
	}
	matte = clamp(matte, 0.0, 1.0);

	uv -= vec2(0.5);
	vec2 n_uv = uv / uv_scale * p_scale;
	n_uv.x *= alan_aspect * p_aspect;

	uv_r = n_uv / size.r;
	uv_g = n_uv / size.g;
	uv_b = n_uv / size.b;

	vec3 noise = vec3(0.0);

	noise.r = texture2D(adsk_results_pass4, uv_r).r;
	noise.g = texture2D(adsk_results_pass4, uv_g).g;
	noise.b = texture2D(adsk_results_pass4, uv_b).b;


	if ( blend_mode == 0)
		col = add(noise, front);
	if ( blend_mode == 1)
		col = overlay(noise, front);
	if ( blend_mode == 2)
		col = spotlight(noise, front);

	vec3 inv_matte = 1.0 - matte;

	if ( grain_only ){
		fin_col = vec4(noise , 1.0);
		gl_FragColor = vec4(fin_col.rgb, 1.0);
	}

	else	{
		fin_col = vec4(inv_matte * col + (matte) * front , matte);
		alpha = pow(abs(alpha), vec3(gamma));
		fin_col.rgb = vec3(alpha * fin_col.rgb + (1.0 - alpha) * front);
		float final_m = 1.0;
		if ( output_matte == 0 )
		final_m = alpha.r * matte.r;
		if ( output_matte == 1)
		final_m = alpha.r;
		if ( output_matte == 2)
		final_m = 1.0;
		gl_FragColor = vec4(fin_col.rgb, final_m);
	}
}
