#!/usr/bin/node
const argv1 = process.argv;
if (argv1[2] === undefined) {
    console.log('No argument');
  } else {
    console.log(process.argv[2]);
  }
