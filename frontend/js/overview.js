function append_fridge_content(name, quantity) {
    var grid = document.querySelector('#columns');
    var item = document.createElement('div');
    var h = '<div class="col-md-3">';
    h += '<div class="">';
    h += name;
    h += '</div>';
    h += '<div class="">';
    h += quantity;
    h += '</div>';
    h += '</div>';
    salvattore['append_elements'](grid, [item]);
    item.outerHTML = h;
}

console.log("Hello!");
$.getJSON("/inventory/", function (data) {
    console.log(data);
    $(data.inventory).each(function (index, item) {
        console.log(item);
        append_fridge_content(item.name, item.quantity);
    })
});
