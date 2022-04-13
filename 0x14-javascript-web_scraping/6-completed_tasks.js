#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
const request = require('request');
const DEMO = process.argv[2];
request(DEMO, function (error, response, body) {
  if (!error) {
    const aux = JSON.parse(body);
    const resl = {};
    aux.forEach((all) => {
      if (all.resl && resl[all.userId] === undefined) {
        resl[all.userId] = 1;
      } else if (all.resl) {
        resl[all.userId] += 1;
      }
    });
    console.log(resl);
  }
});
