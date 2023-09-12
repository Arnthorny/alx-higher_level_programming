#!/usr/bin/node

const numList = Array.from(process.argv.slice(2), x => Number(x)).sort().reverse();

if (numList.length < 2) {
  console.log(0);
} else {
  console.log(numList[1]);
}
