#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie ID>');
  process.exit(1);
}

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    if (!characters) {
      console.error('No characters found for this movie ID');
      return;
    }

    printChar(characters, 0);
  } catch (err) {
    console.error('Error parsing JSON:', err);
  }
});

function printChar (characters, index) {
  request(characters[index], function (error, response, body) {
    if (error) {
      console.error('Error:', error);
      return;
    }

    try {
      const characterData = JSON.parse(body);
      console.log(characterData.name);

      if (index + 1 < characters.length) {
        printChar(characters, index + 1);
      }
    } catch (err) {
      console.error('Error parsing JSON:', err);
    }
  });
}
