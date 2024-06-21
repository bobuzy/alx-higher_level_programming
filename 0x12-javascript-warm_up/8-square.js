#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = Number(process.argv[2]);
  let start = 0;
  while (start < size) {
    console.log('X'.repeat(size));
    start++;
  }
}
