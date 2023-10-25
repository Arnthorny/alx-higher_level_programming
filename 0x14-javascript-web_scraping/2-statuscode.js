#!/usr/bin/node
const request = require('request');

// Request URL
const url = process.argv[2];

request(url, (_, response, body) => {
  // Printing status code
  console.log(`code: ${response && response.statusCode}`);
});
