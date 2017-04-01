var svg = d3.select("#line_graph_development")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
	  "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.json("/linegraphdevelopment/" + country + ".json", function(error, data) {

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    // y.domain([0, d3.max(data, function(d) { return d.index; })]);
    y.domain(d3.extent(data, function(d) { return d.index; }));

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