// Write a JavaScript script that updates the text color of
// the <header> element to red (#FF0000):
// Script must be imported from <head> tag

document.addEventListener('DOMContentLoaded', (e) => {
  const headerT = document.querySelector('header');
  headerT.style.color = '#FF0000';
});
