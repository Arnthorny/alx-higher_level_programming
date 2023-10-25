#!/usr/bin/node
const request = require('request');
const util = require('util');

const ep = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${ep}`;

const req = util.promisify(request);

async function printCharacters (url) {
  const res = await req(url);
  const allFilms = JSON.parse(res.body);
  for (const characUrl of allFilms.characters) {
    const res = await req(characUrl);
    const chara = JSON.parse(res.body);
    console.log(chara.name);
  }
}

printCharacters(filmUrl);
