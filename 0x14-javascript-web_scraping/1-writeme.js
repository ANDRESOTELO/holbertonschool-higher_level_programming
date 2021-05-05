#!/usr/bin/node
// The Node.js file system module allows you to work with the file system
const fs = require('fs');
const path = process.argv;

fs.appendFile(path[2], path[3], 'utf8', function (err, data) {
  if (err) {
    return console.error(err);
  }

  console.log(data);
});
