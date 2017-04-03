// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 20, bottom: 50, left: 100},
width = 600 - margin.left - margin.right,
height = 270 - margin.top - margin.bottom;

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
