/* 
210. Arrow functions
*/

// Function expression

// function teste(str) {
//   console.log('function expression teste', str);
//   return 'fn expression - ' + str
// }

// const t1 = teste();
// console.log(t1);

/* Arrow function */

// const testeArrow = (str) => {
//   console.log('arrow function testeArrow', str);
//   return 'fn arrow - ' + str
// };

// const t1 = testeArrow('parâmetro para arrow fn');
// console.log(t1);

/* Arrow function com 1 parâmetro - parênteses opcional */

// const testeArrow = (str) => {
//   console.log('arrow function testeArrow', str);
//   return 'fn arrow - ' + str;
// };

// const t1 = testeArrow('parâmetro para arrow fn');
// console.log(t1);

/* Arrow function com 1 parâmetro - parênteses opcional - se simplesmente retornar algo (único valor), não precisa de chaves, não precisa da palavra return */

// // const testeArrow = (str) => 'fn arrow - ' + str;
// const testeArrow = (str, n) => 'fn arrow - ' + str + n;

// // const t1 = testeArrow('parâmetro para arrow fn');
// const t1 = testeArrow('parâmetro para arrow fn', 10);
// console.log(t1);

/* para retornar objeto */

// const testeArrow2 = () => {
//   console.log('testeArrow2 chamado');
//   return {
//     foo: 'bar',
//   };
// };

// const t2 = testeArrow2();
// console.log('t2 :>> ', t2);
// console.log('t2["foo"] :>> ', t2['foo']);

/* abaixo, dá erro - o interpretador do JS não sabe que eu quero retornar um objeto porque, para ele, as chaves abaixo são as chaves do corpo da função */

/* const testeArrow2 = () => {
    foo: 'bar',
} */

/* a não ser que seja colocado um return */

// const testeArrow2 = () => {
//   return { foo: 'bar' };
// };

// const t2 = testeArrow2();
// console.log('t2 :>> ', t2);
// console.log('t2["foo"] :>> ', t2['foo']);

/* ou, sem colocar um return, mas colocando um parênteses */

// const testeArrow2 = () => ({
//   foo: 'bar',
// });

// const t2 = testeArrow2();
// console.log('t2 :>> ', t2);
// console.log('t2["foo"] :>> ', t2['foo']);

/* Importante: as arrow functions não são hoistiadas, ao contrário das function expressions */

/* 
211. Escopo léxico vs. escopo dinâmico
*/

/* this em function expression */

// const str = 'global string';
// function teste(str) {
//   console.log('---------');
//   console.log('--function expression--');
//   // const str = 'local string';
//   console.log('this :>> ', this);
//   console.log(str);
//   setTimeout(function () {
//     console.log('--------');
//     console.log('this :>> ', this);
//   }, 2000);
// }
// // // teste('parametro');
// // const obj = {
// //   foo: 'bar',
// //   teste,
// // };
// // obj.teste();

// /*  */
// const teste2 = () => {
//   console.log('--arrow function--');
//   console.log('this :>> ', this);
// };
// // teste2();
// const obj = {
//   foo: 'bar',
//   teste,
//   teste2,
// };
// obj.teste();
// // obj.teste2();

//! o segundo this (do setTimeOut) sofreu alteração, tanto no node quanto no browser. Para não sofrer alteração, basta trocar a function expression do setTimeout por uma arrow function. Nesse caso, os dois this fazem referência ao próprio objeto
//-- conclusão 1: sempre que você tiver trabalhando com o this, e não quiser que ela sofra alteração, use a arrow function. A mesma coisa quano estivermos falando de eventos (ver o button de 211escopo.html). Na arrow function, o this continua sendo o objeto global, por isso não sofre alteração. Ver exemplo no 211escopo.html.

function teste(str) {
  console.log('---------');
  console.log('--function expression--');
  console.log('this :>> ', this);
  console.log(str);
  setTimeout(() => {
    console.log('--------');
    console.log('this :>> ', this);
  }, 2000);
}
const obj = {
  foo: 'bar',
  teste,
};
obj.teste();
