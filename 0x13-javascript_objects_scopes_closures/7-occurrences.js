#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let start = 0; start < list.length; start++) {
    if (list[start] === searchElement) {
      count++;
    }
  }
  return count;
};
