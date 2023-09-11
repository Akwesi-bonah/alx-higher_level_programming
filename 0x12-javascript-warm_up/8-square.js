#!/usr/bin/node

if (typeof process.argv[2] === "undefined" || isNaN(process.argv[2])) {
  console.log("Missing size");
} else {
  let num = parseInt(process.argv[2]);
  for (let i = 0; i < num; i++) {
    let row = "";
    for (let j = 0; j < num; j++) {
      row += "X";
    }
    console.log(row);
  }
}
