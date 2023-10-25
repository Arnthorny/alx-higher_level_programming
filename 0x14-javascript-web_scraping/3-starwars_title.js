#!/usr/bin/node
const request = require('request');

const ep = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ep}`;

request(url, (_, response, body) => {
  // Parse JSON string
  const resJson = JSON.parse(body);
  console.log(resJson.title);
});
