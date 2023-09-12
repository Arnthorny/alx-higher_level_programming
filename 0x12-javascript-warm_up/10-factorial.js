#!/usr/bin/node
function factorial (num) {
  if (!num) return 1;

  return (num * factorial(num - 1));
}
console.log(factorial(Number(process.argv[2])));
