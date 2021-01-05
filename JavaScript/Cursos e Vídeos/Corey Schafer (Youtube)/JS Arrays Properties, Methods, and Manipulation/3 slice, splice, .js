// https://www.youtube.com/watch?v=nAWVYFEzoY8&list=PL-osiE80TeTucQUM10Ezv4S7SVoFozLMK&index=3

// ----------------------------- slice()

/* var array11 = [0,1,2,3,4,5,6,7,8,9];

console.log('Original: ' + array11.join(', '));

var sliced = array11.slice(0,3);
console.log('Sliced: ' + sliced.join(', '));

// últimos 3 elementos
var sliced = array11.slice(array11.length-3);
console.log('Sliced: ' + sliced.join(', '));

// ou:
var sliced = array11.slice(-3,);
console.log('Sliced: ' + sliced.join(', '));

var sliced = array11.slice(-3,-1);
console.log('Sliced: ' + sliced.join(', ')); */

// ----------------------------- splice(): deleta

/* var array12 = ['Corey','Jack','Jill','John','Jane'];

console.log('Original: ' + array12.join(', '));

// Deletando elementos
var deleted = array12.splice(2,1);

console.log('Spliced: ' + array12.join(', '));
console.log('Deleted: ' + deleted.join(', ')); */

// ----------------------------- splice(): adiciona elemento

/* var array12 = ['Corey','Jack','Jill','John','Jane'];

console.log('Original: ' + array12.join(', '));

// Deletando elementos
var deleted = array12.splice(2,0,'Joey');

console.log('Spliced: ' + array12.join(', '));
console.log('Deleted: ' + deleted.join(', ')); */

// ----------------------------- splice(): adiciona array

/* var array12 = ['Corey','Jack','Jill','John','Jane'];

console.log('Original: ' + array12.join(', '));

// Deletando elementos
var deleted = array12.splice(2,0,['Sue','Tim','Pete']);

console.log('Spliced: ' + array12.join(', '));
console.log('Deleted: ' + deleted.join(', '));
 */
// ----------------------------- splice(): deleta  1 e adiciona 1 elemento (substitui 1 elemento)

/* var array12 = ['Corey','Jack','Jill','John','Jane'];

console.log('Original: ' + array12.join(', '));

// Deletando elementos
var deleted = array12.splice(2,1,'Joey');

console.log('Spliced: ' + array12.join(', '));
console.log('Deleted: ' + deleted.join(', ')); */

// ----------------------------- splice(): deleta 3 e adiciona 3 elementos (substitui 3 elementos)

var array12 = ['Corey','Jack','Jill','John','Jane'];

console.log('Original: ' + array12.join(', '));

// Deletando elementos
var deleted = array12.splice(0,3,['Sue','Tim','Pete']);

console.log('Spliced: ' + array12.join(', '));
console.log('Deleted: ' + deleted.join(', '));




