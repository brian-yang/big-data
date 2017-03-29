var state_frag = document.getElementById("line_state_frag");
var glob_dev = document.getElementById("line_glob_dev");

var state_frag_ctx = state_frag.getContext("2d");
var glob_dev_ctx = glob_dev.getContext("2d");

function drawAxes(ctx) {
    ctx.beginPath();
    ctx.moveTo(30, 30);
    ctx.lineTo(30, 150);
    ctx.moveTo(30, 30);
    ctx.lineTo(150, 30);
    ctx.fill();
    ctx.stroke();
    ctx.closePath();
}

drawAxes(state_frag_ctx);
drawAxes(glob_dev_ctx);
