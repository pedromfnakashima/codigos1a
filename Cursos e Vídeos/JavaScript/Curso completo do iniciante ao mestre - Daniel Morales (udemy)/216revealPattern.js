/* 
216. Reveal pattern

Ex.1.

*/

// calcRevealPattern armazena objeto

// const calcRevealPattern = (function () {
//   let n = 0;

//   function somar(_n) {
//     n += _n;
//     return this; // <= permite o encadeamento
//   }

//   function subtrair(_n) {
//     n -= _n;
//     return this; // <= permite o encadeamento
//   }

//   function log() {
//     console.log('n :>> ', n);
//     return this; // <= permite o encadeamento
//   }

//   return {
//     somar,
//     subtrair,
//     log,
//   };
// })();

// calcRevealPattern.somar(5);
// console.log('calcRevealPattern :>> ', calcRevealPattern);
// calcRevealPattern.log();

// calcRevealPattern.somar(5).somar(7).subtrair(2).log();

/* ex. 2.
Colocando função (_checkNumber) sem acesso do lado de fora.
 */

// calcRevealPattern armazena objeto

const calcRevealPattern = (function () {
  let n = 0;

  function _checkNumber(n) {
    if (typeof n != 'number') {
      throw TypeError('precisa passar número');
    }
  }

  function somar(_n) {
    _checkNumber(_n);
    n += _n;
    return this; // <= permite o encadeamento
  }

  function subtrair(_n) {
    _checkNumber(_n);
    n -= _n;
    return this; // <= permite o encadeamento
  }

  function log() {
    console.log('n :>> ', n);
    return this; // <= permite o encadeamento
  }

  return {
    somar,
    subtrair,
    log,
  };
})();

// calcRevealPattern.somar(5);
calcRevealPattern.somar(5).somar(7).subtrair(2).log();
calcRevealPattern.somar(5).somar('7').subtrair(2).log(); //! erro definido.
// console.log('calcRevealPattern :>> ', calcRevealPattern);
// calcRevealPattern.log();
