// Write a JavaScript script that adds a <li> element to a list when the
// user clicks on the tag DIV#add_item:
$('div#add_item').on('click', function () {
  const myL = $('ul.my_list');
  myL.append('<li>Item</li>');
});
