#!/usr/bin/node
const x = Number(process.argv[2]);
for (let i = 0; i < x; i++) {
  let row = '';
  for (let j = 0; j < x; j++) {
    row += 'x ';
  }
  console.log(row);
}
