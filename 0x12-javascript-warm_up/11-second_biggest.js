#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numList = process.argv.slice(2).sort().reverse();
  console.log(numList[1]);
}
