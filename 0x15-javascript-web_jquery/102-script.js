// Write a JavaScript script that fetches and
// prints how to say “Hello” depending on the language

function docReady () {
  const helloTag = $('div#hello');
  $('input#btn_translate').on('click', () => {
    const lCode = $('input#language_code').val();
    // const apiURL = `https://www.fourtonfish.com/hellosalut/hello/`
    const apiURL = 'https://hellosalut.stefanbohacek.dev/';

    $.get(apiURL, { lang: lCode }, function (data, _) {
      helloTag.text(`${data.hello}`);
    });
  });
}
$(document).ready(docReady);
