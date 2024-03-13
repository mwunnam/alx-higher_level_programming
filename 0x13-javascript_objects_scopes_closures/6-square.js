#!/usr/bin/node
const baseSquare = require('./5-square.js');

class Square extends baseSquare {
  /* constructor (size) {
    super(size);
  }
*/
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    } else {
      c = 'C';
    }

    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
