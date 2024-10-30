#version 120
// blur Comp Blurred Highpass Filter with cleaned up Skin
uniform float adsk_result_w, adsk_result_h;
// blurred cleaned face
uniform sampler2D adsk_results_pass14;
// cleaned face and Blurred Key
uniform sampler2D adsk_results_pass12;
uniform float o_amount;

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

void main()
{
   vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
	// cleaned face
	vec3 s = texture2D(adsk_results_pass12, uv).rgb;
	// blurred cleaned face
	vec3 d = texture2D(adsk_results_pass14, uv).rgb;
	// Blurred ChromaKey Matte
	float matte =  texture2D(adsk_results_pass12, uv).a;

	vec3 col = overlay(s, d);
	col = mix (s, col, o_amount * matte);

   gl_FragColor = vec4( col, matte );
}
