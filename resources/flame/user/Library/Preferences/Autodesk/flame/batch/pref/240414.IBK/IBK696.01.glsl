uniform float adsk_result_w, adsk_result_h;
uniform sampler2D input1;
uniform sampler2D input2;

//Int to define green or blue key
uniform int color;
//Floats to define reg/green/blue weights
uniform float rweight;
uniform float gbweight;

//rec709 desaturation
float desaturate(vec3 rgb) {
	float desat = rgb.r * 0.2125 + rgb.g * 0.7154 + rgb.b * 0.0721;
	return desat;
}

//Green IBK
vec4 ibkGreen(vec3 front, vec3 back) {
	float baseAlpha = max((back.g -(back.r * rweight + back.b * gbweight)) / (front.g -(front.r * rweight + front.b * gbweight)),0.0);
	vec3 premult = front * baseAlpha;
	vec3 colorSub = max(back - premult, 0.0);
	float desat = desaturate(colorSub);
	float finalMatte = clamp( max(desat, 1.0-baseAlpha), 0.0, 1.0);
	vec4 result = vec4(colorSub, finalMatte);

	return result;
}

//Blue IBK
vec4 ibkBlue(vec3 front, vec3 back) {
	float baseAlpha = max((back.b -(back.r * rweight + back.g * gbweight)) / (front.b -(front.r * rweight + front.g * gbweight)),0.0);
	vec3 premult = front * baseAlpha;
	vec3 colorSub = max(back - premult, 0.0);
	float desat = desaturate(colorSub);
	float finalMatte = clamp( max(desat, 1.0-baseAlpha), 0.0, 1.0);
	vec4 result = vec4(colorSub, finalMatte);

	return result;
}

//Red IBK
vec4 ibkRed(vec3 front, vec3 back) {
	float baseAlpha = max((back.r -(back.g * rweight + back.b * gbweight)) / (front.r -(front.g * rweight + front.b * gbweight)),0.0);
	vec3 premult = front * baseAlpha;
	vec3 colorSub = max(back - premult, 0.0);
	float desat = desaturate(colorSub);
	float finalMatte = clamp( max(desat, 1.0-baseAlpha), 0.0, 1.0);
	vec4 result = vec4(colorSub, finalMatte);

	return result;
}

void main(void)
{
	vec2 st = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h);

	vec3 front = texture2D(input1, st).rgb;
	vec3 back = texture2D(input2, st).rgb;
	vec4 comp = (0.0,0.0,0.0,0.0);

	if (color == 1) {
		comp = ibkGreen(front, back);
	} else if (color == 2) {
		comp = ibkBlue(front, back);
	} else if (color == 3) {
		comp = ibkRed(front, back);
	}

	
	gl_FragColor = comp;
}

