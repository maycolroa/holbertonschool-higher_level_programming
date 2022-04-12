#!/usr/bin/node
// Write a script that display the status code of a GET request.
const request = require('request');
const test = process.argv[2];
request(test, function (err, response) {
  if (err) throw err;
  console.log('code:', response && response.statusCode);
});
