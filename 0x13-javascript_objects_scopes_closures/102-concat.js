#!/usr/bin/node

const fs = require('fs/promises');

async function concat () {
  const data1 = await fs.readFile(process.argv[2], { encoding: 'utf-8' });
  const data2 = await fs.readFile(process.argv[3], { encoding: 'utf-8' });

  await fs.appendFile(process.argv[4], data1);
  await fs.appendFile(process.argv[4], data2);
}

concat();
