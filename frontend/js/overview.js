function append_fridge_content(name, quantity) {
    request_gif(name, function (imageurl) {
        var grid = document.querySelector('#columns');
        var item = document.createElement('div');
        var h = '<div class="col-xs-6 col-sm-4 col-md-2 fridge-item-pad">';
        h += '<div class="fridge-item">';
        h += '<div class="giphy-image-overlay" alt=""></div>'
        h += '<img src="' + imageurl + '" class="giphy-image"></img>';
        // h += '<div class="item-text-thing-outer row">';
        // h += '<div class="row item-text-thing">';
        h += '<div class="item-name">';
        h += name.charAt(0).toUpperCase() + name.slice(1);;
        h += '</div>';
        h += '<div class="item-count">';
        h += quantity;
        h += '</div>';
        // h += '</div>';
        // h += '</div>';
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
