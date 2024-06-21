#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let start = 0;
    while (start < this.height) {
      console.log('X'.repeat(this.width));
      start++;
    }
  }
}

module.exports = Rectangle;
