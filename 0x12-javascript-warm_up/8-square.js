#!/usr/bin/node
const charSquare = 'X';
const message = 'Missing size';
const size = parseInt(process.argv[2]);
let i;
if (isNaN(size) || size == null) {
  console.log(message);
} else {
  for (i = 0; i < size; i++) {
    console.log(charSquare.repeat(size));
  }
}
