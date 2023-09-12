#!/usr/bin/node

// Script that prints My number: <first argument converted in integer>

if (
  typeof process.argv[2] === "undefined" ||
  isNaN(parseInt(process.argv[2], 10)) === true
) {
  console.log("Not a number");
} else {
  console.log("My number: " + parseInt(process.argv[2], 10));
}

