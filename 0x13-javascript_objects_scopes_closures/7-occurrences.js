#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;

  list.forEach(x => { i = x === searchElement ? i + 1 : i; });
  return i;
};
