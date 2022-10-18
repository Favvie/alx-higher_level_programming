#!/usr/bin/node

const request = require('request');

request({ url: process.argv[2], json: true }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const dataArray = body.results;
    let count = 0;
    for (const film of dataArray) {
      if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count = count + 1;
      }
    }
    console.log(count);
  } else {
    console.error(error);
  }
});
