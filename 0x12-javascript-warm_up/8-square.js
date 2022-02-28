#!/usr/bin/node
// script that prints a square
const arg = process.argv.slice(2);
const argInt = parseInt(arg[0]);
if (isNaN(argInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argInt; i++) {
    console.log('X'.repeat(argInt));
  }
}
