/* 




*/

console.log('-------- VALORES PRIMITIVOS --------');

n = 10;
nObj = new Number(10);

console.log('n.constructor :>> ', n.constructor); // Number
console.log('nObj.constructor :>> ', nObj.constructor); // Number
console.log(
  'n instanceof Number || typeof n === "number" :>> ',
  n instanceof Number || typeof n === 'number'
);

console.log('n instanceof Number :>> ', n instanceof Number); // false
console.log('nObj instanceof Number :>> ', nObj instanceof Number); // true

console.log('-------- VALORES NÃO PRIMITIVOS --------');

const arr1 = [];
const arr2 = new Array();

console.log('arr1 instanceof Array :>> ', arr1 instanceof Array); // true
console.log('arr2 instanceof Array :>> ', arr2 instanceof Array); // true

console.log('-------- regex --------');

const regex1 = /a/g;
const regex2 = new RegExp();

console.log('regex1 instanceof RegExp :>> ', regex1 instanceof RegExp); // true
console.log('regex2 instanceof RegExp :>> ', regex2 instanceof RegExp); // true

console.log('-------- fn --------');
const fn = () => {};
console.log('typeof fn === "function" :>> ', typeof fn === 'function');
