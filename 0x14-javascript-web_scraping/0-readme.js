#!/usr/bin/node
/* script that reads and prints the content of a file
The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object */
const arg = process.argv;
const fs = require('fs');

fs.readFile(arg[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
