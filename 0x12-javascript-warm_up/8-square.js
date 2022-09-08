#!/usr/bin/node
if (Number.isInteger(parseInt(process.argv[2]))) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
} else {
  console.log('Missing size');
}
