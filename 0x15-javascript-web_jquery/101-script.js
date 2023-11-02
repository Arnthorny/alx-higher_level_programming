// Write a JavaScript script that adds a <li> element to a list when the
// user clicks on the tag DIV#add_item:

function listAddRem () {
  const myL = $('ul.my_list');

  $('div#add_item').on('click', function () {
    myL.append('<li>Item</li>');
  });

  $('div#remove_item').on('click', function () {
    myL.children().last().remove();
  });

  $('div#clear_list').on('click', function () {
    myL.empty();
  });
}

$(document).ready(listAddRem);
