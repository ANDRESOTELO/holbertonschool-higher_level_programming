#!/usr/bin/node
const request = require('request');
const adr = process.argv;

request(adr[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  console.log('code:', response && response.statusCode);
});
