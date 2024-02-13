#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) console.log(error);
  const content = JSON.parse(body);
  console.log(content.title);
  const characters = content.characters;
  characters.map((name) => request(name, function (error, response, body) {
    if (error) console.log(error);
    console.log(JSON.parse(body).name);
  }));
});
