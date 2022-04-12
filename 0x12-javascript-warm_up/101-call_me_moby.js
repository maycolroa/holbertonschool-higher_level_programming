#!/usr/bin/node
// Write a function that executes x times a function.
exports.callMeMoby = function (x, theFunction) {
  for (let j = 0; j < x; j++) {
    theFunction();
  }
};
