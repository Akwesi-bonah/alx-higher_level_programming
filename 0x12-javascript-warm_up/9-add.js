#!/usr/bin/node
function add(a, b)
{
    return a + b;
}
if (typeof process.argv[2] === "undefined" || isNaN(process.argv[2])) {
    console.log("NaN")
}
else
{
    let a = parseInt(process.argv[2]);
    let b = parseInt(process.argv[3]);

    console.log(add(a, b));
}