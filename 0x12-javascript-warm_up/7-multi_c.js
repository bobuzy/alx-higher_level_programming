#!/usr/bin/node

if (!process.argv[2]) {
  console.log('Missing number of occurences');
} else {
  const argCount = parseInt(process.argv[2]);
  let start = 0;
  while (start < argCount) {
    console.log('C is fun');
    start++;
  }
}
