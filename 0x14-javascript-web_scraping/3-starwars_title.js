#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], function (err, response, body) {
  console.log(err || JSON.parse(body).title);
});
