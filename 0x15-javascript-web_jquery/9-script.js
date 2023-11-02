// Write a JavaScript script that fetches from https://hellosalut.stef... and displays
// the value of hello from that fetch in the HTML tag DIV#hello.
function docReady () {
  const helloTag = $('div#hello');
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, _) {
    helloTag.text(`${data.hello}`);
  });
}
$(document).ready(docReady);
