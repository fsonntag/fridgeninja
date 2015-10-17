function append_fridge_content(name, quantity) {
    var grid = document.querySelector('#columns');
    var item = document.createElement('div');
    var h = '<div class="col-sm-2 fridge-item">';
    h += '<div class="row item-text-thing">';
    h += '<div class="col-sm-6">';
    h += name;
    h += '</div>';
    h += '<div class="col-sm-6">';
    h += quantity;
    h += '</div>';
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
