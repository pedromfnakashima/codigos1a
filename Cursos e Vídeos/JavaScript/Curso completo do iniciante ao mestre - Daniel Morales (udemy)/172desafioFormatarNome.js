/* 
sem o .split()

*/

// function formatarNome(nomeCompleto) {
//   nomeCompleto = nomeCompleto.trim();

//   let primeiroEspaço = nomeCompleto.indexOf(' ');
//   if (primeiroEspaço < 0) {
//     return nomeCompleto;
//   }

//   let primeiroNome = nomeCompleto.slice(0, primeiroEspaço);
//   let sobreNome = nomeCompleto.slice(primeiroEspaço + 1);

//   return sobreNome + ', ' + primeiroNome;
// }

/* 
com o .split
*/

// console.log('abc def gh'.split(' '));

function formatarNome(nomeCompleto) {
  nomeCompleto = nomeCompleto.trim();

  let nomeAsArray = nomeCompleto.split(' ');
  if (nomeAsArray.length === 1) {
    return nomeCompleto;
  }
  let primeiroNome = nomeAsArray.shift();
  return nomeAsArray.join(' ') + ', ' + primeiroNome;
}

console.log('formatarNome("Pedro") :>> ', formatarNome('Pedro')); // Pedro
console.log(
  'formatarNome("Pedro Nakashima") :>> ',
  formatarNome('Pedro Nakashima')
); // Nakashima, Pedro
console.log(
  'formatarNome("Pedro Massao Favaro Nakashima") :>> ',
  formatarNome('Pedro Massao Favaro Nakashima')
); // Nakashima, Pedro Massao Favaro
