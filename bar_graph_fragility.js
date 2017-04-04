// Adds the svg canvas
var svg2 = d3.select("#bar_graph_fragility")
// Get the data
d3.json("/linegraphfragility/" + country + ".json", function(error, data) {
        
  .selectAll("div")
    .data(data)
  .enter().append("div")
    .style("width", function(d) { return d.index + "px"; })
    .text(function(d) { return d; });
        
});
