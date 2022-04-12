#!/usr/bin/node
// Write a function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let j = 0; j < list.length; j++) {
    if (list[j] === searchElement) {
      counter = counter + 1;
    }
  }
  return (counter);
};
