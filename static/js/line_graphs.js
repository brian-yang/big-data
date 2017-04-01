// var state_frag = document.getElementById("line_state_frag");
// var state_frag_ctx = state_frag.getContext("2d");
// var state_frag_height = state_frag.height;
// var state_frag_width = state_frag.width;
// // Reverses the y-axis on the canvas
// state_frag_ctx.transform(1, 0, 0, -1, 0, state_frag_height);

// var glob_dev = document.getElementById("line_glob_dev");
// var glob_dev_ctx = glob_dev.getContext("2d");
// var glob_dev_height = glob_dev.height;
// var glob_dev_width = glob_dev.width;
// // Reverses the y-axis on the canvas
// glob_dev_ctx.transform(1, 0, 0, -1, 0, glob_dev_height);

// function drawAxes(ctx, height) {
//     ctx.beginPath();
//     ctx.moveTo(30, 30);
//     ctx.lineTo(30, 450);
//     ctx.moveTo(30, 30);
//     ctx.lineTo(450, 30);
//     // ctx.moveTo(30, ctx.height - 200);
//     // ctx.lineTo(30, ctx.height - 150);
//     // ctx.moveTo(30, ctx.height - 30);
//     // ctx.lineTo(150, ctx.height - 30);
//     ctx.fill();
//     ctx.stroke();
//     ctx.closePath();
//     console.log(height);
// }

// drawAxes(state_frag_ctx, state_frag_height);
// drawAxes(glob_dev_ctx, glob_dev_width);

var country = "United States";

// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 20, bottom: 50, left: 60},
width = 600 - margin.left - margin.right,
height = 270 - margin.top - margin.bottom;

// Set the graph labels offsets
var label_offset = 50;

// Set the ranges
var x = d3.scale.linear().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(9).tickFormat(d3.format("d"));

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

// Define the line
var valueline = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.index); });

var modes = ["development", "fragility"];

for (var i = 0; i < modes.length; i++) {
    // Adds the svg canvas
    var svg = d3.select("#line_graph_" + modes[i])
	.append("svg")
	.attr("width", width + margin.left + margin.right)
	.attr("height", height + margin.top + margin.bottom)
	.append("g")
	.attr("transform",
	      "translate(" + margin.left + "," + margin.top + ")");

    // Get the data
    d3.json("/linegraph" + modes[i] + "/" + country + ".json", function(error, data) {

	// Scale the range of the data
	x.domain(d3.extent(data, function(d) { return d.date; }));
	y.domain([0, d3.max(data, function(d) { return d.index; })]);

	console.log(svg);

	// Add the valueline path.
	svg.append("path")
	    .attr("class", "line")
	    .attr("d", valueline(data));

	// Add the X Axis
	svg.append("g")
	    .attr("class", "x axis")
	    .attr("transform", "translate(0," + height + ")")
	    .call(xAxis);

	// Add the Y Axis
	svg.append("g")
	    .attr("class", "y axis")
	    .call(yAxis);

	// y-axis label
	svg.append("text")
	    .attr("class", "y label")
	    .attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
	    .attr("transform", "rotate(-90)")  // text is drawn off the screen top left, move down and out and rotate
	    .attr("x", -(height / 2))
	    .attr("y", -label_offset)
	    .text("Value");

	// x-axis label
	svg.append("text")
	    .attr("class", "x label")
	    .attr("text-anchor", "middle")
	    .attr("x", width / 2)
	    .attr("y", height + label_offset)
	    .text("Year");
    });
}
