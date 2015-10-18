// DOM element where the Timeline will be attached
var container = document.getElementById('visualization');
var items = new vis.DataSet();

$.getJSON("/events", function(data) {
  var timeline_data = [];
  $(data.events).each(function (index, event) {
    var color = intToRGB(hashCode(event.user.username));
    timeline_data.push({
      id: index,
      content: event.user.username,
      start: new Date(event.timestamp),
      style: "background-color: #" + color,
      subgroup: event.user.username
    });
  })
  items = new vis.DataSet(timeline_data);

  // Configuration for the Timeline
  var options = {
    width: '100%'
  };

  // Create a Timeline
  var timeline = new vis.Timeline(container, items, options);
});


function hashCode(str) { // java String#hashCode
    var hash = 0;
    for (var i = 0; i < str.length; i++) {
       hash = str.charCodeAt(i) + ((hash << 5) - hash);
    }
    return hash;
}

function intToRGB(i){
    var c = (i & 0x00FFFFFF)
        .toString(16)
        .toUpperCase();

    return "00000".substring(0, 6 - c.length) + c;
}
