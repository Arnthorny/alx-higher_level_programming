// Write a JavaScript script that fetches the character name from this URL:
// https://swapi-api.alx-tools.com/api/people/5/?format=json
const charaTag = $('div#character');

function getFn (data, textStatus) {
  charaTag.text(`${data.name}`);
}

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', getFn);
