#!/usr/bin/node
/* import list from a module or file  */
const list = require('./100-data').list;

console.log(list);
/* The map() method creates a new array populated with the results of calling a provided function on every element in the calling array */
console.log(list.map((value, index) => value * index));
