/* 
215. Encadeamento de métodos (chain)
*/

/* ex. 1. (ver no console do chrome)
métodos nativos do JS
*/
// let doc = document.querySelector('a');
// console.log('doc :>> ', doc);

/* ex. 2. (ver no chrome)
Encadeando método style
*/

// document.querySelector('a').style.color = 'red';

/* ex. 3.
 */

// const calc = {
//   value: 0,
//   soma(n) {
//     this.value += n;
//   },
//   subtrai(n) {
//     this.value -= n;
//   },
//   log() {},
// };

// calc.soma(5);
// console.log('calc.value :>> ', calc.value); // 5

/* ex. 4 - COM ERRO
Encadeando no ex. 3.
*/

// const calc = {
//   value: 0,
//   soma(n) {
//     this.value += n;
//   },
//   subtrai(n) {
//     this.value -= n;
//   },
//   log() {},
// };

// // calc.soma(5).soma(2); //! COM Erro
// console.log('calc.soma(5) :>> ', calc.soma(5)); // undefined
// console.log('calc.value :>> ', calc.value); //

/* ex. 5 - SEM ERRO
Encadeando no ex. 3.
*/

const calc = {
  value: 0,
  soma(n) {
    this.value += n;
    return this; // <= permite o encadeamento
  },
  subtrai(n) {
    this.value -= n;
    return this; // <= permite o encadeamento
  },
  log() {
    console.log('this.value :>> ', this.value);
    return this; // <= permite o encadeamento
  },
};

// calc.soma(5).soma(2); //! 7; SEM Erro
// calc.soma(5).soma(2).subtrai(3).soma(2); //! 6; SEM Erro
calc.soma(5).soma(2).subtrai(3).soma(2).log().soma(4).log(); //! 6,10; SEM Erro
// console.log('calc.soma(5) :>> ', calc.soma(5)); // objeto
// console.log('calc.value :>> ', calc.value); //
