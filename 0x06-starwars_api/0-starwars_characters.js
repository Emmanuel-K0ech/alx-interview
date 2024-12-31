#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).chars;
    printChar(chars, 0);
  }
});

function printChar (chars, indx) {
  request(chars[indx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (indx + 1 < chars.length) {
        printChar(chars, indx + 1);
      }
    }
  });
}