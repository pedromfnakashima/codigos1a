/* 

*/

/* 
178. min, max, pow, round, sqrt, cbrt, random
O objeto Math não é uma função construtora.


*/

// // console.log('Math :>> ', Math); // objeto com vários atributos e métodos

// console.log('Math.PI :>> ', Math.PI);
// console.log('Math.SQRT2 :>> ', Math.SQRT2);

// console.log('Math.min(1,2,3,4,5) :>> ', Math.min(1, 2, 3, 4, 5));
// console.log('Math.max(1,2,10,4,5) :>> ', Math.max(1, 2, 10, 4, 5));

// let arr = [1, 2, 10, 4, 5];
// console.log('Math.max(...arr) :>> ', Math.max(...arr));

// console.log('Math.round(45.5) :>> ', Math.round(45.5));
// console.log('Math.round(45.49) :>> ', Math.round(45.49));

// console.log('Math.floor(49.99999) :>> ', Math.floor(49.99999));
// console.log('Math.ceil(49.99999) :>> ', Math.ceil(49.99999));

// console.log('Math.pow(2,3) :>> ', Math.pow(2, 3));
// console.log('2**3 :>> ', 2 ** 3);

// console.log('Math.sqrt(49) :>> ', Math.sqrt(49));
// console.log('Math.cbrt(8) :>> ', Math.cbrt(8));

// console.log('Math.random() :>> ', Math.random());
// console.log('Math.random() * 10 :>> ', Math.random() * 10);
// console.log('Math.random() * 100 :>> ', Math.random() * 100);

// console.log(
//   'Math.floor(Math.random() * 10 ):>> ',
//   Math.floor(Math.random() * 10)
// );

/* 
179 sorteia.js
*/

function getRandomNumber(inicio = 0, fim = 10, integer = true) {
  // inicio = inicio || 0;
  // fim = fim || 1;

  let r = Math.random() * (fim - inicio + 1) + inicio;
  // console.log(inicio, fim);
  return integer ? parseInt(r) : r;
}

console.log(getRandomNumber(2, 3));
console.log(getRandomNumber(2, 3, false));
