#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numList = process.argv.slice(2);
  numList.sort((a, b) => b - a);
  console.log(numList[1]);
}
