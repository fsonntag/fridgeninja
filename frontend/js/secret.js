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

    return "Bene";
};

var currentuser = getUrlParameter("username");


function makeChoice(title, callback) {
    var htmlstr = '<div class="row itemrow">' +
        '<div class="col-xs-8 big"><span class="vcenter">' + title + '</span></div>' +
        '<div class="col-xs-4">' +
        '<div class="input-group counter-spinner">' +
        '<span class="input-group-btn">' +
        '<button class="btn btn-lg btn-default down" type="button">-</button>' +
        '</span>' +
        '<input disabled type="text" class="form-control input-lg centered-text" placeholder="How much" value="0">' +
        '<span class="input-group-btn">' +
        '<button class="btn btn-lg btn-default up" type="button">+</button>' +
        '</span>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '<div class="sep"></div>';
    var element = $(htmlstr);
    $('#choicehost').append(element);
    callback(element);
}

var choices = {};
var newcount = 0;

$(document).ready(function() {
    $.getJSON('/inventory/choices', function(data) {
        $(data.suggestions).each(function(index, ttl) {
            makeChoice(ttl, function(element) {
                $(element).find('.up').click(function(e) {
                    var cter = $(this).parent().siblings('input');
                    var asint = parseInt(cter.val());
                    choices[ttl] = asint + 1;
                    cter.val(asint + 1);
                });
                $(element).find('.down').click(function(e) {
                    var cter = $(this).parent().siblings('input');
                    var asint = parseInt(cter.val());
                    choices[ttl] = asint - 1;
                    cter.val(asint - 1);
                });
            });
        });
    })
    .fail(function() {
        console.log("fu");
    });
    $.getJSON('/users', function(data) {
        $(data.users).each(function(index, user) {
            if(user.username == currentuser) {
                $('#activeuser').html(currentuser);
            } else {
                var htmlstr = '<li><a href="#" class="otheruser">' + user.username + '</a></li>';
                $('#userhost').append($(htmlstr));
            }
        });

        // todo on-users
        $('.otheruser').on('click', function(event) {
            event.preventDefault();
            console.log("wowza");
            var newguy = $(this).html();
            var oldguy = $('#activeuser').html();
            $(this).html(oldguy);
            $('#activeuser').html(newguy);
        }); 
    });

    $('#submitbattn').click(function(e) {
        var newthing = $('#newkram').val();
        if(newthing !== '' && newcount > 0) {
            choices[newthing] = newcount;
        }

        // transactions work upside down
        $(Object.keys(choices)).each(function(index, k) {
            choices[k] = -choices[k];
        });

        var data = {
            username: $('#activeuser').html(),
            transactions: choices
        };
        console.log(data);
        $.ajax({
            type: "POST",
            url: '/events/',
            dataType: 'json',
            data: JSON.stringify(data),
            success: function () {
                $('#submitbattn').text("YO GEIL!");
                window.location.replace('/');
            },
            fail: function() {
                alert("Schade schokolade");
            }
        });
    });
    
    $('#philippcheckts').find('.up').click(function(e) {
        var cter = $(this).parent().siblings('input');
        var asint = parseInt(cter.val());
        newcount++;
        cter.val(asint + 1);
    });
    $('#philippcheckts').find('.down').click(function(e) {
        var cter = $(this).parent().siblings('input');
        var asint = parseInt(cter.val());
        newcount--;
        cter.val(asint - 1);
    });
});