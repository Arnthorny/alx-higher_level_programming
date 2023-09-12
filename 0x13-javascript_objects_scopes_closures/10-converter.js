#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    return (Number(num).toString(base));
  };
};
