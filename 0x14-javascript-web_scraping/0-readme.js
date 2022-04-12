#!/usr/bin/node
// Write a script that reads and prints the content of a file.
const fs = require('fs');
const test = process.argv[2];
fs.readFile(test, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
