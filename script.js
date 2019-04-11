var newData;
var table = document.getElementById("fulltable");
var allvalues = table.getElementsByTagName("td");
var array = Array.prototype.slice.call(allvalues, 0)

window.setInterval(function(){
$.getJSON('url_of_json_file?format=json',
function(data){
    newData = data.data;
    return newData;
    console.log("data fetched")
  },function(error){
    console.log(error);
});
},500);

function changeValues(){
  
for (var i = 0; i < array.length; i++) {
  
  allvalues[i].innerHTML = newData[i].symbol+"<br>" + newData[i].per +"%"; 
    }
}
window.setInterval(function(){
  changeValues();
  }, 50);