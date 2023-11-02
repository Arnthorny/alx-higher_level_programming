// Write a JavaScript script that toggles the class of the <header> element
// when the user clicks on the tag DIV#toggle_header:
$('div#toggle_header').on('click', function () {
  $('header').toggleClass('red');
  $('header').toggleClass('green');
});
