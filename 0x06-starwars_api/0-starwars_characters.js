#!/usr/bin/node
// Star Wars Characters of a particular Film
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <movie ID');
  process.exit(1);
}

const movieId = process.argv[2];
const baseURL = 'https://swapi-api.alx-tools.com/api/films/';
const url = `${baseURL}${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }
        const person = JSON.parse(body);
        const name = person.name;
        console.log(name);
      });
    });
  } catch (error) {
    console.error('Error parsing JSON', error);
  }
});
