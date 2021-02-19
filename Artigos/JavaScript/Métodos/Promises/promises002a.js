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
Problema:
Extremamente lento
*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// const forLoop = async (_) => {
//   console.log('Start');

//   for (let index = 0; index < fruitsToGet.length; index++) {
//     const fruit = fruitsToGet[index];
//     const numFruit = await getNumFruit(fruit);
//     console.log(numFruit);
//   }

//   console.log('End');
// };

// forLoop();

/* Parte 3b
Await in a forEach loop
Problema: diferente do esperado, que era:

'Start'
'27'
'0'
'14'
'End'

Obtido:
'Start'
'End'
'27'
'0'
'14'

"JavaScript does this because forEach is not promise-aware. It cannot support async and await. You cannot use await in forEach."

*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// const forEachLoop = (_) => {
//   console.log('Start');

//   fruitsToGet.forEach(async (fruit) => {
//     const numFruit = await getNumFruit(fruit);
//     console.log(numFruit);
//   });

//   console.log('End');
// };

// forEachLoop();

/* Parte 3c1
If you use await in a map, map will always return an array of promises. This is because asynchronous functions always return promises. 


*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// const mapLoop = async (_) => {
//   console.log('Start');

//   const numFruits = await fruitsToGet.map(async (fruit) => {
//     const numFruit = await getNumFruit(fruit);
//     return numFruit;
//   });

//   console.log(numFruits);

//   console.log('End');
// };

// mapLoop();

/* Parte 3c2
Since map always return promises (if you use await), you have to wait for the array of promises to get resolved. You can do this with await Promise.all(arrayOfPromises).
*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// const mapLoop = async (_) => {
//   console.log('Start');

//   const promises = fruitsToGet.map(async (fruit) => {
//     const numFruit = await getNumFruit(fruit);
//     return numFruit;
//   });

//   const numFruits = await Promise.all(promises);
//   console.log(numFruits);

//   console.log('End');
// };

// mapLoop();

/* Parte 3c3
You can manipulate the value you return in your promises if you wish to. The resolved values will be the values you return.
*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// const mapLoop = async (_) => {
//   console.log('Start');

//   const promises = fruitsToGet.map(async (fruit) => {
//     const numFruit = await getNumFruit(fruit);
//     // Adds onn fruits before returning
//     return numFruit + 100;
//   });

//   const numFruits = await Promise.all(promises);
//   console.log(numFruits);

//   console.log('End');
// };

// mapLoop();

/* Parte 4a - AWAIT WITH FILTER

When you use filter, you want to filter an array with a specific result. Let’s say you want to create an array with more than 20 fruits.

You would expect moreThan20 to contain only apples because there are 27 apples, but there are 0 grapes and 14 pears.

*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// // Filter if there's no await
// const filterLoop = (_) => {
//   console.log('Start');

//   const moreThan20 = fruitsToGet.filter((fruit) => {
//     const numFruit = fruitBasket[fruit];
//     return numFruit > 20;
//   });

//   console.log(moreThan20);
//   console.log('End');
// };

// filterLoop();

/* Parte 4b

await in filter doesn’t work the same way. In fact, it doesn’t work at all. You get the unfiltered array back…


Here’s why it happens.

When you use await in a filter callback, the callback always returns a promise. Since promises are always truthy, everything item in the array passes the filter. Writing await in a filter is like writing this code:
// Everything passes the filter...
const filtered = array.filter(() => true)

*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// const filterLoop = async (_) => {
//   console.log('Start');

//   const moreThan20 = await fruitsToGet.filter(async (fruit) => {
//     const numFruit = await getNumFruit(fruit);
//     return numFruit > 20;
//   });

//   console.log(moreThan20);
//   console.log('End');
// };

// filterLoop();

/* Parte 4c

There are three steps to use await and filter properly:

Use map to return an array promises
await the array of promises
filter the resolved values


*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// const filterLoop = async (_) => {
//   console.log('Start');

//   const promises = await fruitsToGet.map((fruit) => getNumFruit(fruit));
//   const numFruits = await Promise.all(promises);

//   const moreThan20 = fruitsToGet.filter((fruit, index) => {
//     const numFruit = numFruits[index];
//     return numFruit > 20;
//   });

//   console.log(moreThan20);
//   console.log('End');
// };

// filterLoop();

/* Parte 5a - AWAIT WITH REDUCE

For this case, let’s say you want to find out the total number of fruits in the fruitBasket. Normally, you can use reduce to loop through an array and sum the number up.
You’ll get a total of 41 fruits. (27 + 0 + 14 = 41).

*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// // Reduce if there's no await
// const reduceLoop = (_) => {
//   console.log('Start');

//   const sum = fruitsToGet.reduce((sum, fruit) => {
//     const numFruit = fruitBasket[fruit];
//     return sum + numFruit;
//   }, 0);

//   console.log(sum);
//   console.log('End');
// };

// reduceLoop();

/* Parte 5b
When you use await with reduce, the results get extremely messy.

What?! [object Promise]14?!

Dissecting this is interesting.

. In the first iteration, sum is 0. numFruit is 27 (the resolved value from getNumFruit('apple')). 0 + 27 is 27.
. In the second iteration, sum is a promise. (Why? Because asynchronous functions always return promises!) numFruit is 0. A promise cannot be added to an object normally, so the JavaScript converts it to [object Promise] string. [object Promise] + 0 is [object Promise]0
. In the third iteration, sum is also a promise. numFruit is 14. [object Promise] + 14 is [object Promise]14.
Mystery solved!

*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// // Reduce if we await getNumFruit
// const reduceLoop = async (_) => {
//   console.log('Start');

//   const sum = await fruitsToGet.reduce(async (sum, fruit) => {
//     const numFruit = await getNumFruit(fruit);
//     return sum + numFruit;
//   }, 0);

//   console.log(sum);
//   console.log('End');
// };

// reduceLoop();

/* Parte 5c

This means, you can use await in a reduce callback, but you have to remember to await the accumulator first!

But… as you can see from the gif, it takes pretty long to await everything. This happens because reduceLoop needs to wait for the promisedSum to be completed for each iteration.

*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// const reduceLoop = async (_) => {
//   console.log('Start');

//   const sum = await fruitsToGet.reduce(async (promisedSum, fruit) => {
//     const sum = await promisedSum;
//     const numFruit = await getNumFruit(fruit);
//     return sum + numFruit;
//   }, 0);

//   console.log(sum);
//   console.log('End');
// };

// reduceLoop();

/* Parte 5d

There’s a way to speed up the reduce loop. (I found out about this thanks to Tim Oxley). If you await getNumFruits() first before await promisedSum, the reduceLoop takes only one second to complete:

This works because reduce can fire all three getNumFruit promises before waiting for the next iteration of the loop. However, this method is slightly confusing since you have to be careful of the order you await things.

*/

// console.log('início do código');
// const fruitsToGet = ['apple', 'grape', 'pear'];

// const reduceLoop = async (_) => {
//   console.log('Start');

//   const sum = await fruitsToGet.reduce(async (promisedSum, fruit) => {
//     // Heavy-lifting comes first.
//     // This triggers all three `getNumFruit` promises before waiting for the next interation of the loop.
//     const numFruit = await getNumFruit(fruit);
//     const sum = await promisedSum;
//     return sum + numFruit;
//   }, 0);

//   console.log(sum);
//   console.log('End');
// };

// reduceLoop();

/* Parte 5e

The simplest (and most efficient way) to use await in reduce is to:

1. Use map to return an array promises
2. await the array of promises
3. reduce the resolved values

This version is simple to read and understand, and takes one second to calculate the total number of fruits.


*/

console.log('início do código');
const fruitsToGet = ['apple', 'grape', 'pear'];

const reduceLoop = async (_) => {
  console.log('Start');

  const promises = fruitsToGet.map(getNumFruit);
  const numFruits = await Promise.all(promises);
  const sum = numFruits.reduce((sum, fruit) => sum + fruit);

  console.log(sum);
  console.log('End');
};

reduceLoop();

/* 

Key Takeaways
1. If you want to execute await calls in series, use a for-loop (or any loop without a callback).
2. Don’t ever use await with forEach. Use a for-loop (or any loop without a callback) instead.
3. Don’t await inside filter and reduce. Always await an array of promises with map, then filter or reduce accordingly.


*/
