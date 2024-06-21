#!/usr/bin/node

let numList = process.argv.slice(2).map(Number);

if (numList.length === 0 || numList.length === 1) {
  console.log(0);
} else {
  numList.sort((a, b) => b - a);
  console.log(numList[1]);
}
