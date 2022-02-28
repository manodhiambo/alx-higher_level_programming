#!/usr/bin/node
/* script that prints My number: <first argument converted in integer> if
the first argument can be converted to an integer */
const arg = process.argv.slice(2);
const argInt = parseInt(arg[0]);
if (isNaN(argInt)) {
  console.log('Not a number');
} else if (typeof argInt === 'number') {
  console.log('My number: ' + argInt);
}
