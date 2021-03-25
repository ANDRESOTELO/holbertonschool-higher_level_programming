#!/usr/bin/node
/* The fs module of Node.js implements the File I/O operation */
/* fs.readFileSync() method */
/* inbuilt application programming interface of fs module which is used to read the file and return its content */

/* Include fs module */
const fs = require('fs');

/* Calling the readFileSync() method to read file that is passed in argv */
const data1 = fs.readFileSync(process.argv[2], { encoding: 'utf8', flag: 'r' });
const data2 = fs.readFileSync(process.argv[3], { encoding: 'utf8', flag: 'r' });

fs.writeFileSync(process.argv[4], data1 + data2);
