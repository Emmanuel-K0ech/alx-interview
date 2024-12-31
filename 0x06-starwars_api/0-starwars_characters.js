#!/usr/bin/node
// Star Wars Characters of a particulars Film using Async/Await
const axios = require('axios');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const baseURL = 'https://swapi-api.alx-tools.com/api/films/';

(async () => {
  try {
    const { data } = await axios.get(`${baseURL}${movieId}`);
    const characters = data.characters;

    for (const characterUrl of characters) {
      const { data: characterData } = await axios.get(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
})();
