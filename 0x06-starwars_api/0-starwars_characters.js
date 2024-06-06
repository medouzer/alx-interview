#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

const getCharacters = (url) => {
  request(url, async (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const characters = JSON.parse(body).characters;
      for (const character of characters) {
        const name = await getName(character);
        console.log(name);
      }
    }
  });
};

const getName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

getCharacters(url);
