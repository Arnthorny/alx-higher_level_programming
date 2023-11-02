// Write a JavaScript script that fetches and lists the title for all movies by using
// this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const mList = $('ul#list_movies');

function getTitleFn (data, textStatus) {
  for (const res of data.results) {
    mList.append(`<li>${res.title}</li>`);
  }
}

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', getTitleFn);
