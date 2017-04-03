// Adds the svg canvas
var svg2 = d3.select("#line_graph_fragility")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
	  "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.json("/linegraphfragility/" + country + ".json", function(error, data) {

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    if (country === "Canada") {
	y.domain([-0.5, 0.5]);
    } else {
	y.domain([0, d3.max(data, function(d) { return d.index; })]);
    }
    // y.domain(d3.extent(data, function(d) { return d.index; }));

    // Add the valueline path.
    svg2.append("path")
	.attr("class", "line")
	.attr("d", valueline(data));

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
	.attr("y", -label_offset)
	.text("State Fragility Index");

    // x-axis label
    svg2.append("text")
	.attr("class", "x label")
	.attr("text-anchor", "middle")
	.attr("x", width / 2)
	.attr("y", height + label_offset)
	.text("Year");
});
