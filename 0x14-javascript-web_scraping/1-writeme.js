#!/usr/bin/node
/* script that writes a string to a file
The first argument is the file path
The second argument is the string to write
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object */
const args = process.argv;
const fs = require('fs');

fs.writeFile(args[2], args[3], 'utf8', function (err, data) {
  if (err) console.log(err);
});
