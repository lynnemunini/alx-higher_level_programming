#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const myArray = [];
  for (let i = 2; i < process.argv.length; i++) {
    myArray.push(parseInt(process.argv[i]));
  }
  myArray.sort().reverse();
  console.log(myArray[1]);
}
