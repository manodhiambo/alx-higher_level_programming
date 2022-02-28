#!/usr/bin/node
// script that prints x times “C is fun”
const arg = process.argv.slice(2);
const argInt = parseInt(arg[0]);
if (isNaN(argInt)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argInt; i++) {
    console.log('C is fun');
  }
}
