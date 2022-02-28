#!/usr/bin/node
// script that computes and prints a factorial recursively
const arg = process.argv.slice(2);
const argInt = parseInt(arg[0]);
function factorial (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(argInt));
