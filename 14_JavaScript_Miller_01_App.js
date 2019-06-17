//from data.js
//var tableData = data;
var tbody = d3.select("tbody"); 


function populateTable(array){
array.forEach(function(UFO) {
 
  var row = tbody.append("tr");
  Object.entries(UFO).forEach(function([key, value]) {
  
    var cell = row.append("td");
    cell.text(value);
  });
})};
populateTable(data)

d3.select("#filter-btn")
  .on("click", function(){
    d3.event.preventDefault();
    var userInput = d3.select("#datetime").property("value")
    tbody.text("")
    populateTable(data.filter(function(obj){
      return obj.datetime==userInput
    }))
  })