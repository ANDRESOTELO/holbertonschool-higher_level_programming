#!/usr/bin/node
const request = require('request');
const url = require('url');
const adr = process.argv;

request(adr[2], function(error, response, body) {
    console.log('code:', response && response.statusCode);
});
