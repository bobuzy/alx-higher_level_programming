#!/usr/bin/node

exports.callMeMoby = function (x, aFunction) {
  let start;
  for (start = 0; start < x; start++) {
    aFunction();
  }
};
