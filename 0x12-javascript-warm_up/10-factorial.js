#!/usr/bin/node
// script that computes and prints a factorial
function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (
  typeof process.argv[2] === 'undefined' ||
  isNaN(parseInt(process.argv[2], 10)) === true ||
  parseInt(process.argv[2], 10) < 0
) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2], 10)));
}
