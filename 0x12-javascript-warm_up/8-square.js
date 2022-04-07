#!/usr/bin/node
// print x for arguments
const counter = process.argv[2];
if (parseInt(!counter)) {
  for (let j = 0; j < counter; j++) {
    console.log('X'.repeat(counter));
  }
} else {
  console.log('Missing size');
}
