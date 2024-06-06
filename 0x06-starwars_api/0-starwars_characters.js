#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request')

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2]

request(url, function (error, response, body) {
  if (error) {
    console.error(error)
  } else {
    const characters = JSON.parse(body).characters
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error) {
          console.error(error)
        } else {
          console.log(JSON.parse(body).name)
        }
      })
    }
  }
})
