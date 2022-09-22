#!/usr/bin/node

function factorial (number) {
  if (number === 0) {
    return 1;
  }
  return number * factorial(number - 1);
}

if (process.argv.length === 2) {
  console.log(factorial(0));
} else {
  console.log(factorial(process.argv[2]));
}
