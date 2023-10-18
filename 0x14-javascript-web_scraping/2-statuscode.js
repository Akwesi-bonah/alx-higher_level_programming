#!/usr/bin/node
// (_8^(|) displays the status code of a GET request
let request = require('request');
request(process.argv[2], function (error, response) {
  if (error) throw error;
  console.log('code:', response.statusCode);
});
