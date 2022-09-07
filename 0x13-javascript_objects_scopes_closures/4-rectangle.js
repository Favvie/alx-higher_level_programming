#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) {
        square = square + 'X';
      }
      console.log(square);
    }
  }

  rotate () {
    const height = this.height;
    const width = this.width;
    this.width = height;
    this.height = width;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
