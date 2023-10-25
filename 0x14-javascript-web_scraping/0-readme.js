#!/usr/bin/node

const fs = require('fs/promises');

async function readFile () {
  const data = await fs.readFile(process.argv[2], { encoding: 'utf-8' });
  console.log(data);
}

readFile();
