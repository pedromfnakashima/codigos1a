/* 
214. closures
Capacidade de uma função enxergar as variáveis que estavam ao redor dela no momento em que ela foi declarada.
*/

/* ex. 1.
retorna string
*/

// const teste = (function () {
//   return 'meu retorno';
// })();

// console.log('teste :>> ', teste);

/* ex. 2.
retorna outra function
*/

// const teste = (function () {
//   return function testeInterno() {
//     console.log('testeInterno chamado');
//     return 'retorno de testeInterno';
//   };
// })();

// console.log('teste :>> ', teste);
// console.log('teste() :>> ', teste());
// let str = teste();
// console.log('str :>> ', str);

/* ex. 3.

*/

// const teste = (function () {
//   let n = 0;
//   return function testeInterno() {
//     // console.log('testeInterno chamado', n);
//     console.log('testeInterno chamado', ++n);
//     return 'retorno de testeInterno' + n;
//   };
// })();

// let str = teste();
// console.log('str :>> ', str);
// teste();
// teste();
// let str2 = teste();
// console.log('str2 :>> ', str2);

/* ex. 4.

*/

const teste = (function (n) {
  // n = 10
  return function testeInterno() {
    // console.log('testeInterno chamado', n);
    console.log('testeInterno chamado', ++n);
    return 'retorno de testeInterno' + n;
  };
})(10);

let str = teste();
console.log('str :>> ', str);
teste();
teste();
let str2 = teste();
console.log('str2 :>> ', str2);
