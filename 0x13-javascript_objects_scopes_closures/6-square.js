#!/usr/bin/node
const oldclass = require("./5-square");

class Square extends oldclass {
  charPrint(C) {
    if (C === undefined) {
      C = "X";
    }
    for (let i = 0; i < this.height; i++) {
      let row = "";
      for (let j = 0; j < this.width; j++) {
        row += C;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
