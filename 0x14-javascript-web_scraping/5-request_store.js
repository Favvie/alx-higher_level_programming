#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request({ url: process.argv[2], json: true }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
      if (err) {
        return console.error('error from file: ' + err);
      }
    });
  } else {
    return console.error('error from request: ' + error);
  }
});
