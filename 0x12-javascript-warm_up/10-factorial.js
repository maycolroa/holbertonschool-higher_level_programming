#!/usr/bin/node
// fact scrip
const Factorial = process.argv[2];
function factorial (Factorial) {
  if (isNaN(Factorial) || Factorial === 1) {
    return (1);
  } else {
    return (Factorial * factorial(Factorial - 1));
  }
}
console.log(factorial(parseInt(Factorial)));
