#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (_, response, body) => {
  // Parse JSON string
  const resJson = JSON.parse(body);
  const completed = {};
  for (const res of resJson) {
    if (res.completed) {
      completed[res.userId] = completed[res.userId] ? ++completed[res.userId] : 1;
    }
  }
  console.log(completed);
});
