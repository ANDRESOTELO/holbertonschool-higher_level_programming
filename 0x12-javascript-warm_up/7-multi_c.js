#!/usr/bin/node
const cFun = 'C is fun';
const x = parseInt(process.argv[2]);
let i;
if (isNaN(x) || x == null) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log(cFun);
  }
}
