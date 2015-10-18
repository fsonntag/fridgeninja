function append_event_content(timestamp, username, transactions) {
    var grid = document.querySelector('#event_columns');
    var item = document.createElement('div');
    var date = new Date(timestamp);
    var transaction_string = build_transaction_string(username, transactions);
    var h = '<div class="event-row">';
    h += '<hr class="seperator">';
    h += '<div class="time-string">';
    h += moment(date).format('MMM D YYYY, hh:mm a');
    h += '</div>';
    h += '<div class="transaction-string">';
    h += transaction_string;
    h += '</div>';
    h += '</div>';
    salvattore['append_elements'](grid, [item]);
    item.outerHTML = h;
}

function build_transaction_string(username, transactions) {
  var s = username + " ";
  var plus_transactions = {};
  var minus_transactions = {};
  for (var key in transactions) {
    if (transactions[key] >= 0) {
      plus_transactions[key] = transactions[key];
    } else {
      minus_transactions[key] = transactions[key];
    }
  }

  var plus_s = "";
  var minus_s = "";
  var plus_keys = Object.keys(plus_transactions);
  var minus_keys = Object.keys(minus_transactions);

  for (i = 0; i < plus_keys.length; i++) {
    if (i == plus_keys.length - 1 && plus_keys.length != 1) {
      plus_s = plus_s.substring(0, plus_s.length - 2) + " and ";
    }

    plus_s += plus_transactions[plus_keys[i]] + " " + plus_keys[i];
    if (plus_transactions[plus_keys[i]] == 1) {
      plus_s += ", ";
    } else {
      plus_s += "s, ";
    }
  }

  for (i = 0; i < minus_keys.length; i++) {
    if (i == minus_keys.length - 1 && minus_keys.length != 1) {
      minus_s = minus_s.substring(0, plus_s.length - 2) + " and ";
    }

    minus_s += Math.abs(minus_transactions[minus_keys[i]]) + " " + minus_keys[i];
    if (minus_transactions[minus_keys[i]] == -1) {
      minus_s += ", ";
    } else {
      minus_s += "s, ";
    }
  }

  if (plus_keys.length > 0 && minus_keys.length > 0) {
    s += "put in " + plus_s.substring(0, plus_s.length - 2) + " and took " + minus_s.substring(0, minus_s.length - 2) + ".";
  } else if (plus_keys.length > 0 && minus_keys.length == 0) {
    s += "put in " + plus_s.substring(0, plus_s.length - 2) + ".";
  } else {
    s += "took " + minus_s.substring(0, minus_s.length - 2) + ".";
  }
  return s;
}

var page = 0;
function getPage(pageNumber) {
  $.ajax({
    url: "/events?page=" + pageNumber,
    type: "GET",
    beforeSend: function(){
      $('#spinner').show();
    },
    complete: function(){
      $('#spinner').hide();
    },
    success: function (data) {
      $(data.events).each(function (index, event) {
      append_event_content(event.timestamp, event.user.username, event.transactions);
      })
    }
  });
}
getPage(page);

$(window).scroll(function() {
  if($(window).scrollTop() == $(document).height() - $(window).height()) {
      // ajax call get data from server and append to the div
      page++;
      getPage(page);
  }
});
