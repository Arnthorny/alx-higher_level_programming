// Write a JavaScript script that fetches and
// prints how to say “Hello” depending on the language

function setHello (e) {
  if ($(this).prop('id') === 'language_code' && !(e.which === 13)) return;

  const helloTag = $('div#hello');
  const lCode = $('input#language_code').val();
  // const apiURL = `https://www.fourtonfish.com/hellosalut/hello/`
  const apiURL = 'https://hellosalut.stefanbohacek.dev/';

  $.get(apiURL, { lang: lCode }, function (data, _) {
    helloTag.text(`${data.hello}`);
  });
}

function docReady () {
  $('input#btn_translate').on('click', setHello);
  $('input#language_code').on('keydown', setHello);
}
$(document).ready(docReady);
