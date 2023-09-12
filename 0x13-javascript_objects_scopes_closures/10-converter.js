#!/usr/bin/node

exports.converter = function (base) {
  const main = function (num) {
    return (Number(num).toString(base));
  };
  return main;
};
