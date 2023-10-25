#!/usr/bin/node

const fs = require('fs/promises');

async function writeFile () {
  try {
    const content = process.argv[3];
    await fs.writeFile(process.argv[2], content, { encoding: 'utf-8' });
  } catch (err) {
    console.log(err);
  }
}

writeFile();
