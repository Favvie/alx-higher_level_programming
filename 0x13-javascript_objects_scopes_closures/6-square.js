#!/usr/bin/node

const Squares = require('./5-square');
module.exports = class Square extends Squares {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) {
        if (c) {
          square = square + c;
        } else {
          square = square + 'X';
        }
      }
      console.log(square);
    }
  }
};
