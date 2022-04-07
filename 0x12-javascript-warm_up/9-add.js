#!/usr/bin/node
// sum of two scrip
const sum1 = process.argv[2];
const sum2 = process.argv[3];
if (!sum1 || !sum2) {
  console.log('NaN');
} else {
  const add = parseInt(sum1) + parseInt(sum2);
  console.log(add);
}
