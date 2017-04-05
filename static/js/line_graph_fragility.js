// Adds the svg canvas
var svg2 = d3.select("#line_graph_fragility")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
	  "translate(" + margin.left + "," + margin.top + ")");

svg2.append("g")
    .attr("class", "load");

var load2 = svg2.append("text")
    .attr("class", "load")
    .attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
    .attr("x",  width / 2)
    .attr("y",  height / 2)
    .text("Loading...");

// Get the data
d3.json("/line/fragility/" + country + ".json", function(error, data) {
    load2.text("");

    if (data.length <= 0) {
	svg2.append("g")
	    .attr("class", "n/a");

	svg2.append("text")
	    .attr("class", "n/a")
	    .attr("text-anchor", "middle")
	    .attr("x", width / 2)
	    .attr("y", height / 2)
	    .text("Data not available");

	// Scale the range of the data
	x.domain([0, 1]);
	y.domain([0, 1]);
    } else {
	// Scale the range of the data
	x.domain(d3.extent(data, function(d) { return d.date; }));
	y.domain([-0.5, d3.max(data, function(d) { return d.index; })]);

	// Add the valueline path.
	svg2.append("path")
	    .attr("class", "line")
	    .attr("d", valueline(data));
    }

    // Add the title
    svg2.append("g")
	.attr("class", "title");

    // Add the X Axis
    svg2.append("g")
	.attr("class", "x axis")
	.attr("transform", "translate(0," + height + ")")
	.call(xAxis);

    // Add the Y Axis
    svg2.append("g")
	.attr("class", "y axis")
	.call(yAxis);

    // Title
    svg2.append("text")
	.attr("class", "title")
	.attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
	.attr("x",  width / 2)
        .attr("y", -10)
	.text("State Fragility");

    // y-axis label
    svg2.append("text")
	.attr("class", "y label")
	.attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
	.attr("transform", "rotate(-90)")  // text is drawn off the screen top left, move down and out and rotate
	.attr("x", -(height / 2))
	.attr("y", -50)
	.text("State Fragility Score");

    // x-axis label
    svg2.append("text")
	.attr("class", "x label")
	.attr("text-anchor", "middle")
	.attr("x", width / 2)
	.attr("y", height + 50)
	.text("Year");
});
