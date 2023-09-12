#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};

for (const [key, val] of Object.entries(dict)) {
  if (newDict[val]) newDict[val].push(key);
  else { newDict[val] = Array(key); }
}
console.log(newDict);
