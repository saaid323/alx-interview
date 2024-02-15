#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) console.log(error);
  const content = JSON.parse(body);
  console.log(content.title);
  const characters = content.characters;
  names(characters);
});

function names (characters, index = 0) {
  request(characters[index], function (error, response, body) {
    if (error) console.log(error);
    const content = JSON.parse(body);
    console.log(content.name);
    if (characters.length - 1 > index) {
      return names(characters, index + 1);
    }
  });
}
