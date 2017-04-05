var margin4 = {top: 20, right: 20, bottom: 70, left: 80},
width4 = 600 - margin4.left - margin4.right - 20,
height4 = 300 - margin4.top - margin4.bottom - 20;

var x4 = d3.scale.ordinal().rangeRoundBands([0, width], .05);
var y4 = d3.scale.linear().range([height, 0]);

var xAxis4 = d3.svg.axis()
    .scale(x4)
    .orient("bottom")
    .ticks(5);

var yAxis4 = d3.svg.axis()
    .scale(y4)
    .orient("left")
    .ticks(10);

var svg4 = d3.select("#frag").append("svg")
    .attr("width", width4 + margin4.left + margin4.right)
    .attr("height", height4 + margin4.top + margin4.bottom)
    .append("g")
    .attr("transform",
	  "translate(" + margin4.left + "," + margin4.top + ")");

svg4.append("g")
    .attr("class", "load");

var load4 = svg4.append("text")
    .attr("class", "load")
    .attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
    .attr("x",  width4 / 2)
    .attr("y",  height4 / 2)
    .text("Loading...");

d3.json("/line/fragility/" + country + ".json", function(error, data) {
    load4.text("");

    if (data.length <= 0) {
	svg4.append("g")
	    .attr("class", "n/a");

	svg4.append("text")
	    .attr("class", "n/a")
	    .attr("text-anchor", "middle")
	    .attr("x", width4 / 2)
	    .attr("y", height4 / 2)
	    .text("Data not available");
    } else {
	x4.domain(data.map(function(d) { return d.date; }));
	y4.domain([-0.5, d3.max(data, function(d) { return d.index; })]);

	svg4.selectAll("bar")
	    .data(data)
	    .enter().append("rect")
	    .style("fill", "steelblue")
	    .attr("x", function(d) { return x4(d.date); })
	    .attr("width", x4.rangeBand())
	    .attr("y", function(d) { return y4(d.index); })
	    .attr("height", function(d) { return height4 - y4(d.index); });
    }


    svg4.append("g")
	.attr("class", "x axis")
	.attr("transform", "translate(0," + height4 + ")")
	.call(xAxis4)
	.selectAll("text")
	.style("text-anchor", "end")
	.attr("dx", "-.8em")
	.attr("dy", "-.55em")
	.attr("transform", "rotate(-90)" )

    svg4.append("g")
    	.attr("class", "y axis")
    	.call(yAxis4)
    	.append("text")
    	.attr("transform", "rotate(-90)")
    	.attr("y", -50)
    	.attr("dy", ".71em")
        .attr("x", -35)
    	.style("text-anchor", "end")
    	.text("State Fragility Score");
});
