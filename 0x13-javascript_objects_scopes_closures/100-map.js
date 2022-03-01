#!/usr/bin/node
// a script that imports an array and computes a new array
const list = require('./100-data').list;
const multiIdx = (value, index) => value * index;
const newlist = list.map(multiIdx);
console.log(list);
console.log(newlist);
