#!/usr/bin/node
// Prints "C is fun"
const counter = process.argv[2];
if (!counter) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < counter; j++) {
    console.log('C is fun');
  }
}
