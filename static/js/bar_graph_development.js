var margin3 = {top: 20, right: 20, bottom: 70, left: 80},
width3 = 600 - margin3.left - margin3.right - 20,
height3 = 300 - margin3.top - margin3.bottom - 20;

var x3 = d3.scale.ordinal().rangeRoundBands([0, width], .05);
var y3 = d3.scale.linear().range([height, 0]);

var xAxis3 = d3.svg.axis()
    .scale(x3)
    .orient("bottom")
    .ticks(5);

var yAxis3 = d3.svg.axis()
    .scale(y3)
    .orient("left")
    .ticks(10);

var svg3 = d3.select("#dev").append("svg")
    .attr("width", width3 + margin3.left + margin3.right)
    .attr("height", height3 + margin3.top + margin3.bottom)
    .append("g")
    .attr("transform",
	  "translate(" + margin3.left + "," + margin3.top + ")");

svg3.append("g")
    .attr("class", "load");

var load3 = svg3.append("text")
    .attr("class", "load")
    .attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
    .attr("x",  width3 / 2)
    .attr("y",  height3 / 2)
    .text("Loading...");

d3.json("/line/development/" + country + ".json", function(error, data) {
    load3.text("");

    if (data.length <= 0) {
	svg3.append("g")
	    .attr("class", "n/a");

	svg3.append("text")
	    .attr("class", "n/a")
	    .attr("text-anchor", "middle")
	    .attr("x", width3 / 2)
	    .attr("y", height3 / 2)
	    .text("Data not available");
    } else {
	x3.domain(data.map(function(d) { return d.date; }));
	y3.domain([0, d3.max(data, function(d) { return d.index; })]);

	svg3.selectAll("bar")
	    .data(data)
	    .enter().append("rect")
	    .style("fill", "steelblue")
	    .attr("x", function(d) { return x3(d.date); })
	    .attr("width", x3.rangeBand())
	    .attr("y", function(d) { return y3(d.index); })
	    .attr("height", function(d) { return height3 - y3(d.index); });
    }

    svg3.append("g")
	.attr("class", "x axis")
	.attr("transform", "translate(0," + height3 + ")")
	.call(xAxis3)
	.selectAll("text")
	.style("text-anchor", "end")
	.attr("dx", "-.8em")
	.attr("dy", "-.55em")
	.attr("transform", "rotate(-90)" )

    svg3.append("g")
    	.attr("class", "y axis")
    	.call(yAxis3)
    	.append("text")
    	.attr("transform", "rotate(-90)")
    	.attr("y", -50)
    	.attr("dy", ".71em")
        .attr("x", -35)
    	.style("text-anchor", "end")
    	.text("Global Development Score");
});
