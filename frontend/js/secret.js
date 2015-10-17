var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

username = getUrlParameter("username");

function append_fridge_content(name, quantity) {
    request_gif(name, function (imageurl) {
        var grid = document.querySelector('#columns');
        var item = document.createElement('div');
        var h = '<div class="col-xs-12 fridge-item">';
        h += '<div class="fridge-item-pad">';
        //h += '<img src="' + imageurl + '" class="giphy-image"></img>';
        h += '<div class="item-text-thing-outer">';
        h += '<div class="row item-text-thing">';
        h += '<div class="col-xs-6 item-name">';
        h += name;
        h += '</div>';
        h += '<div class="col-xs-6 item-count">';
        h += quantity;
        h += '</div>';
        h += '</div>';
        h += '</div>';
        h += '</div>';
        console.log(h);
        salvattore['append_elements'](grid, [item]);
        item.outerHTML = h;
    })

}

console.log("Hello!");
$.getJSON("/inventory/", function (data) {
    console.log(data);
    $(data.inventory).each(function (index, item) {
        console.log(item);
        append_fridge_content(item.name, item.quantity);
    });

});
function request_gif(query, callback) {
    $.getJSON("https://api.giphy.com/v1/gifs/search?q=" + query +"&api_key=dc6zaTOxFJmzC", function (data) {
        // console.log(data.data[0]);
        callback(data.data[0].images.downsized.url);
    })

}
