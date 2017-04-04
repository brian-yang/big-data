// Adds the svg canvas
// Get the data
d3.json("/line/development/" + country + ".json", function(error, data) {
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.index; })]);
  var svg2 = d3.select("#bar_graph_fragility");
  var svg3 = svg2.append('svg')    
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
	  "translate(" + margin.left + "," + margin.top + ")");
   svg3.append("g")
	.attr("class", "title");
  
    
    // Add the X Axis
    svg3.append("g")
	.attr("class", "x axis")
	.attr("transform", "translate(0," + height + ")")
	.call(xAxis);

    // Add the Y Axis
    svg3.append("g")
	.attr("class", "y axis")
	.call(yAxis);

    // Title
    svg3.append("text")
	.attr("class", "title")
	.attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
	.attr("x",  width / 2)
        .attr("y", -10)
	.text("Global Development");

    // y-axis label
    svg3.append("text")
	.attr("class", "y label")
	.attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
	.attr("transform", "rotate(-90)")  // text is drawn off the screen top left, move down and out and rotate
	.attr("x", -(height / 2))
	.attr("y", -label_offset)
	.text("Global Development Score");

    // x-axis label
    svg3.append("text")
	.attr("class", "x label")
	.attr("text-anchor", "middle")
	.attr("x", width / 2)
	.attr("y", height + label_offset)
	.text("Year");


  var bar = svg3.selectAll('rect');
  var barUpdate = bar.data(data);
  //var barText = barUpdate.enter().append('div');
  //barEnter.text(function(d) { return d.year; });
  var barEnter = barUpdate.enter().append('rect');
    barEnter.attr("x", function(d, i) {
    return i * 21;  //Bar width of 20 plus 1 for padding
});

    
    barEnter.attr("y", 0);
    barEnter.attr("width",20);
    //barEnter.attr("transform", "rotate(180)")
   barEnter.attr("height", function(d) { return d.index*5 + "px"})
   // .attr("transform", "rotate(180)")
   //.attr("transform", "translate(0," + (svg3.style.height - barEnter.style.height) + ")");
   barEnter.text(function(d) { return d.index; });
    alert('hei');
    console.log(svg3.style.height);
    
    
});
