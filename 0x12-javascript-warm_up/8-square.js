#!/usr/bin/node
if (isNaN(Number(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing size');
}
const x = Number(process.argv[2]);
for (let i = 0; i < x; i++) {
  let row = '';
  for (let j = 0; j < x; j++) {
    row += 'X';
  }
  console.log(row);
}
