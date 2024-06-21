#!/usr/bin/node

if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  let start = 0;
  for (let col = 0; col < size; col++) {
    let line = '';
    for (let row = 0; row < size; row++) {
      line += 'X';
    }
    console.log(line);
  }
}
