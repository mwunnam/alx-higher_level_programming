#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const message = process.argv[3];

fs.writeFile(filePath, message, 'utf-8', (err) => {
  if (err) {
    console.log(err);
    return;
  }
})


