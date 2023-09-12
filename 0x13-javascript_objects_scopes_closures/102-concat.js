#!/usr/bin/node

const { readFile, writeFile } = require('node:fs/promises');
const path = require('path');
const files = process.argv.slice(2);

async function concat () {
  try {
    const data1 = await readFile(path.resolve(files[0]), { encoding: 'utf8' });
    const data2 = await readFile(path.resolve(files[1]), { encoding: 'utf8' });

    await writeFile(path.resolve(files[2]), data1, { flag: 'a' });
    await writeFile(path.resolve(files[2]), data2, { flag: 'a' });
  } catch (error) {
  }
}

concat();
