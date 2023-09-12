#!/usr/bin/node

const callMeMoby = function (x, theFunction) {
  for (let i = x; i > 0; i--) { theFunction(); }
};
exports.callMeMoby = callMeMoby;
