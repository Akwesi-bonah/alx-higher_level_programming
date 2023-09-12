#!/usr/bin/node
//  script that prints a square
if (typeof process.argv[2] === 'undefined' ||
 isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const num = Number(process.argv[2]);
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
