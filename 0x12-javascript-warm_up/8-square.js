#!/usr/bin/node
if (Number.isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('X'.repeat(Number(process.argv[2])));
  }
}
