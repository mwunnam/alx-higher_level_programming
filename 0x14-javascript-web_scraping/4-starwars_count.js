#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if (response.statusCode !== 200) {
    return;
  }
  const films = JSON.parse(body).results;
  const wedgeAntillesMovies = films.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/' + characterId + '/'));
  console.log(wedgeAntillesMovies.length);
});
