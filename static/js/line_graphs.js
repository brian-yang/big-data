var state_frag = document.getElementById("line_state_frag");
var state_frag_ctx = state_frag.getContext("2d");
var state_frag_height = state_frag.height;
var state_frag_width = state_frag.width;
// Reverses the y-axis on the canvas
state_frag_ctx.transform(1, 0, 0, -1, 0, state_frag_height);

var glob_dev = document.getElementById("line_glob_dev");
var glob_dev_ctx = glob_dev.getContext("2d");
var glob_dev_height = glob_dev.height;
var glob_dev_width = glob_dev.width;
// Reverses the y-axis on the canvas
glob_dev_ctx.transform(1, 0, 0, -1, 0, glob_dev_height);

function drawAxes(ctx, height) {
    ctx.beginPath();
    ctx.moveTo(100, 100);
    ctx.lineTo(100, 150);
    ctx.moveTo(100, 100);
    ctx.lineTo(150, 100);
    // ctx.moveTo(30, ctx.height - 200);
    // ctx.lineTo(30, ctx.height - 150);
    // ctx.moveTo(30, ctx.height - 30);
    // ctx.lineTo(150, ctx.height - 30);
    ctx.fill();
    ctx.stroke();
    ctx.closePath();
    console.log(height);
}

drawAxes(state_frag_ctx, state_frag_height);
drawAxes(glob_dev_ctx, glob_dev_width);
