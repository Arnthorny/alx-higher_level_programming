#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (_, response, body) => {
  // Parse JSON string
  const resJson = JSON.parse(body);
  let count = 0;
  for (const result of resJson.results) {
    result.characters.forEach((cha) => {
      count = cha.includes(18) ? ++count : count;
    });
  }
  console.log(count);
});
