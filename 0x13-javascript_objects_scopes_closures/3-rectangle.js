#!/usr/bin/node
// class Rectangle..
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 & h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }
};
