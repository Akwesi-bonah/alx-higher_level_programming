#!/usr/bin/node
function add(a, b) {
  const result =  a + b;
  console.log(result)
}

let a = Number(process.argv[2]);
let b = Number(process.argv[3]);

add(a, b);
