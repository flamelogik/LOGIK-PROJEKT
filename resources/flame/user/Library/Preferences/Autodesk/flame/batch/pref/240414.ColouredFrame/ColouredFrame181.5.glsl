#version 120

uniform float adsk_time, adsk_result_w, adsk_result_h, adsk_result_frameratio;
vec2 res = vec2(adsk_result_w, adsk_result_h);


vec3 rgb2hsv(vec3 c)
{
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}

vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

vec3 make_palette(vec2 st)
{
	vec3 col = vec3(0.0);
	float v;

	col.r = st.y;

	if (st.x > .75) {
		col.g = 1.0;
		v = 1.0 - ((st.x - .75) * 4);
		col.b = v;
	} else if (st.x > .25) {
		col.g = (st.x - .25) * 2.0;
		col.b = 1.0;
	} else {
		col.r = 0.0;
		col.b = st.x * 4.0 * st.y;
	}

	col = hsv2rgb(col);


	return col;
}

void main(void)
{
	vec2 st = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);
	vec3 col = make_palette(st);


	gl_FragColor = vec4(col, 1.0);
}
