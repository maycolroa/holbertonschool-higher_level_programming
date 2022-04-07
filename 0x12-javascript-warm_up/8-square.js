#!/usr/bin/node
// print x for arguments.
const counter = process.argv[2];
if (parseInt(counter)) {
  for (let i = 0; i < counter; i++) {
    console.log('X'.repeat(counter));
  }
} else {
  console.log('Missing size');
}
