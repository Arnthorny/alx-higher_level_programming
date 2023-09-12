#!/usr/bin/node

let count = -1;
exports.logMe = function (item) {
  (function anon () {
    count++;
    console.log(`${count}: ${item}`);
  })();
};
