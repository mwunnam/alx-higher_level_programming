#!/usr/bin/node
if (isNaN(Number(process.argv[2])) | Number(process.argv[2] < 0)) {
  console.log('Missing size');
}
const x = Number(process.argv[2]);
let i, j;
for (i = 0; i < x; i++) {
  let row = '';
  for (j = 0; j < x; j++) {
    row += 'x';
  }
  console.log(row);
}
