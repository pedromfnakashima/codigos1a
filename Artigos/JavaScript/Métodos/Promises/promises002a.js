/* 
Artigo.
JavaScript async and await in loops
https://zellwk.com/blog/async-await-in-loops/

Pesquisa no google (async await loops): https://www.google.com/search?q=async+await+loops&rlz=1C1SQJL_enBR879BR879&oq=async+await+loops&aqs=chrome..69i57j69i60l2.5410j0j7&sourceid=chrome&ie=UTF-8

*/

/* Parte 1a */

// console.log('início do código');

// const fruitBasket = {
//   apple: 27,
//   grape: 0,
//   pear: 14,
// };

// const getNumFruit = (fruit) => {
//   return fruitBasket[fruit];
// };

// const numApples = getNumFruit('apple');
// console.log(numApples); // 27

/* Parte 2a */

// console.log('início do código');

const fruitBasket = {
  apple: 27,
  grape: 0,
  pear: 14,
};

const sleep = (ms) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};

const getNumFruit = (fruit) => {
  return sleep(2000).then((v) => fruitBasket[fruit]);
};

// getNumFruit('apple').then((num) => console.log(num)); // 27

/* Parte 2b */

// console.log('início do código');

// const fruitBasket = {
//   apple: 27,
//   grape: 0,
//   pear: 14,
// };

// const sleep = (ms) => {
//   return new Promise((resolve) => setTimeout(resolve, ms));
// };

// const getNumFruit = (fruit) => {
//   return sleep(2000).then((v) => fruitBasket[fruit]);
// };

// const control = async (_) => {
//   console.log('Start');

//   const numApples = await getNumFruit('apple');
//   console.log(numApples);

//   const numGrapes = await getNumFruit('grape');
//   console.log(numGrapes);

//   const numPears = await getNumFruit('pear');
//   console.log(numPears);

//   console.log('End');
// };

// control();

/* Parte 3a
Await in a for loop
*/

console.log('início do código');

const fruitsToGet = ['apple', 'grape', 'pear'];

const forEachLoop = (_) => {
  console.log('Start');

  fruitsToGet.forEach(async (fruit) => {
    const numFruit = await getNumFruit(fruit);
    console.log(numFruit);
  });

  console.log('End');
};

forEachLoop();
