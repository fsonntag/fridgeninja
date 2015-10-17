function append_event_content(timestamp, username, transactions) {
    var grid = document.querySelector('#event_columns');
    var item = document.createElement('div');
    var h = '<div class="col-md-3">';
    h += '<div class="">';
    h += username;
    h += '</div>';
    h += '<div class="">';
    h += timestamp;
    h += '</div>';
    h += '</div>';
    salvattore['append_elements'](grid, [item]);
    item.outerHTML = h;
}

$.getJSON("/events/", function (data) {
    console.log(data);
    $(data.events).each(function (index, event) {
        console.log(event);
        append_event_content(event.timestamp, event.user.username, event.transactions);
    })
});
