#!/usr/bin/node
const counter = process.argv[2];
if (!counter) {
  console.log('Not a number');
} else if (parseInt(counter)) {
  console.log('My number: ' + Math.floor(counter));
} else {
  console.log('Not a number');
}
