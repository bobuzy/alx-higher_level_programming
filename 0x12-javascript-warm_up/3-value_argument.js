#!/usr/bin/node

const argCount = process.argv.slice(2).length;
if (argCount === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
