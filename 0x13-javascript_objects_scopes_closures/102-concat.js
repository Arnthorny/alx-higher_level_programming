#!/usr/bin/node

const { readFile, writeFile } = require('node:fs/promises');
const files = process.argv.slice(2);

async function concat () {
  try {
    const data1 = await readFile(files[0]);
    const data2 = await readFile(files[1]);
    const fileDataString = `${data1.toString()}${data2.toString()}`;
    await writeFile(files[2], fileDataString);
  } catch (error) {
    console.log(`Error occured: ${error.message}`);
  }
}

concat();
