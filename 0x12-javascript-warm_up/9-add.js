#!/usr/bin/node
//  script that prints the addition of 2 integers
function add(a, b) {
  const result =  a + b;
  console.log(result)
}

let a = Number(process.argv[2]);
let b = Number(process.argv[3]);
add(a, b);

