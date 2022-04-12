#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
const auxsquare = require('./5-square');
module.exports = class Square extends auxsquare {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
