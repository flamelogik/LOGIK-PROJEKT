// Croptastic (C)2017 Bob Maple
// bobm-matchbox [at] idolum.com

uniform sampler2D  in_front, in_matte;
uniform	    float  crop_l, crop_r, crop_t, crop_b;
uniform      vec2  crop_tl, crop_br, offset_xy;
uniform     float  adsk_result_w, adsk_result_h;
uniform      bool  invert, border, border_overadv;
uniform      vec3  border_color;
uniform     float  border_size, border_trans;
uniform      bool  aborder_l, aborder_r, aborder_t, aborder_b;
uniform     float  aborder_lsize, aborder_rsize, aborder_tsize, aborder_bsize;
uniform     float  aborder_ltrans, aborder_rtrans, aborder_ttrans, aborder_btrans;
uniform      vec3  aborder_lcolor, aborder_rcolor, aborder_tcolor, aborder_bcolor;

// Global variables

vec4 npx;


//

void do_border(void) {

    if( (gl_FragCoord.x >= crop_l && gl_FragCoord.x <= crop_l + border_size) || (gl_FragCoord.x <= (adsk_result_w - crop_r) && gl_FragCoord.x >= (adsk_result_w - crop_r) - border_size) )
        if( gl_FragCoord.y >= crop_b && gl_FragCoord.y <= adsk_result_h - crop_t )
            npx = vec4( mix( npx, vec4( border_color, 1.0 ), (border_trans / 100.0) ) );

    if( (gl_FragCoord.y >= crop_b && gl_FragCoord.y <= crop_b + border_size) || (gl_FragCoord.y <= (adsk_result_h - crop_t) && gl_FragCoord.y >= (adsk_result_h - crop_t) - border_size) )
        if( gl_FragCoord.x >= crop_l + border_size && gl_FragCoord.x <= (adsk_result_w - crop_r) - border_size )
            npx = vec4( mix( npx, vec4( border_color, 1.0 ), (border_trans / 100.0) ) );
}

//

void main(void) {

    // Convert pixel coords to UV position for texture2D,
    // fetch the fill and matte pixels and combine them into px

    vec2 uv  = (gl_FragCoord.xy - offset_xy) / vec2( adsk_result_w, adsk_result_h );
    vec4 px  = vec4( texture2D( in_front, uv ).rgb, texture2D( in_matte, uv ).g );

    vec4 blk = vec4( 0.0, 0.0, 0.0, 0.0 );

    // Initialize this pixel to either the input pixel or black

    npx = invert ? blk : px;

    // Do the cropping

    if( gl_FragCoord.x < crop_l )
        npx = invert ? px : blk;
    if( gl_FragCoord.x > adsk_result_w - crop_r )
        npx = invert ? px : blk;

    if( gl_FragCoord.y > adsk_result_h - crop_t )
        npx = invert ? px : blk;
    if( gl_FragCoord.y < crop_b )
        npx = invert ? px : blk;

    // Draw standard border if it's supposed to be underneath

    if( border && !border_overadv )
        do_border();


    // Draw Advanced Borders

    if( aborder_l ) {

        if( (gl_FragCoord.x >= crop_l && gl_FragCoord.x <= crop_l + aborder_lsize) && (gl_FragCoord.y >= crop_b && gl_FragCoord.y <= adsk_result_h - crop_t) )
            npx = vec4( mix( npx, vec4( aborder_lcolor, 1.0 ), (aborder_ltrans / 100.0) ) );
    }

    if( aborder_r ) {

        if( (gl_FragCoord.x <= (adsk_result_w - crop_r) && gl_FragCoord.x >= (adsk_result_w - crop_r) - aborder_rsize) && (gl_FragCoord.y >= crop_b && gl_FragCoord.y <= adsk_result_h - crop_t) )
            npx = vec4( mix( npx, vec4( aborder_rcolor, 1.0 ), (aborder_rtrans / 100.0) ) );
    }

    if( aborder_t ) {

        if( (gl_FragCoord.y <= (adsk_result_h - crop_t) && gl_FragCoord.y >= (adsk_result_h - crop_t) - aborder_tsize) && (gl_FragCoord.x >= crop_l && gl_FragCoord.x <= adsk_result_w - crop_r) )
            npx = vec4( mix( npx, vec4( aborder_tcolor, 1.0 ), (aborder_ttrans / 100.0) ) );
    }

    if( aborder_b ) {

        if( (gl_FragCoord.y >= crop_b && gl_FragCoord.y <= crop_b + aborder_bsize) && (gl_FragCoord.x >= crop_l && gl_FragCoord.x <= adsk_result_w - crop_r) )
            npx = vec4( mix( npx, vec4( aborder_bcolor, 1.0 ), (aborder_btrans / 100.0) ) );
    }


    // Draw standard border if it's supposed to be on top

    if( border && border_overadv )
        do_border();

    gl_FragColor = npx;
}
