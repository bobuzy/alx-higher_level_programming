#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  let val = parseInt(process.argv[2]);
  
  function factorial (num) {
    if (num === 1) {
      return (1);
    }
    num = num * factorial(num - 1);
    return (num);
  }
  
  console.log(factorial(val));
}
