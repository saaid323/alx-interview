#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) console.log(error);
  const content = JSON.parse(body);
  console.log(content.title);
  const characters = content.characters;
  const names = characters.map((name) => {
    return new Promise((resolve, reject) => {
      request(name, function (error, response, body) {
        if (error) {
          console.log(error);
          reject(error);
        }
        resolve(JSON.parse(body).name);
      });
    });
  });
  Promise.all(names).then((values) =>
    console.log(values.join('\n'))
  ).catch((error) => console.log(error));
});
