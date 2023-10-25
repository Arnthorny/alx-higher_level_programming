#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const wedgeAntillesUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (_, response, body) => {
  // Parse JSON string
  const resJson = JSON.parse(body);
  let count = 0;
  for (const result of resJson.results) {
    if (result.characters.includes(wedgeAntillesUrl)) count++;
  }
  console.log(count);
});
