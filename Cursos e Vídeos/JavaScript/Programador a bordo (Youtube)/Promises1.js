/* 
Ex. 1.
*/

// console.log('Primeiro');
// setTimeout(function () {
//   console.log('Segundo');
// }, 0);
// console.log('Terceiro');
// console.log('Quarto');
// setTimeout(function () {
//   console.log('Meio');
// }, 0);
// console.log('Quinto');

/* 
ESTADOS DE UMA PROMISE:
. PENDENTE. 
. REALIZADA. 
. REJEITADA. 
. ESTABELECIDA. 

// Ex. 2a. Função que retorna uma Promise já resolvida.
// */
// function jaRealizada() {
//   return Promise.resolve('PARAM RESOLVIDO');
// }

// jaRealizada().then(function (x) {
//   console.log('Promise resolvida', x);
// });

// /*
// Ex. 2b. Função que retorna uma Promise já rejeitada.
// */

// function jaRejeitada() {
//   return Promise.reject('PARAM REJEITADO');
// }
// jaRejeitada().catch(function (x) {
//   console.log('Promise rejeitada', x);
// });

/* 
Ex. 3.
*/

// function promRes() {
//   return new Promise(function (resolve, reject) {
//     resolve('Olá de resolvido');
//   });
// }
// promRes().then(function (mensagem) {
//   console.log(mensagem);
// });

// function promRej() {
//   return new Promise(function (resolve, reject) {
//     reject('Olá de rejeitado');
//   });
// }
// promRej().catch(function (mensagem) {
//   console.log(mensagem);
// });

/* 
Ex. 4.
*/

// function promRes() {
//   return new Promise(function (resolve, reject) {
//     setTimeout(function () {
//       resolve('Resolvido depois de 3 segundos');
//     }, 3000);
//   });
// }
// promRes().then(function (mensagem) {
//   console.log(mensagem);
// });

// function promRej() {
//   return new Promise(function (resolve, reject) {
//     reject('Olá de rejeitado');
//   });
// }
// promRej().catch(function (mensagem) {
//   console.log(mensagem);
// });

/* 
Ex. 5a
*/

// window.fetch('https://viacep.com.br/ws/79032370/json/')
//   .then(function (data) {
//   data.json().then(function (endereco) {
//     console.log(endereco);
//   });
// });

/* 
Ex. 5b
*/

// window
//   .fetch('https://viacep.com.br/ws/79032370/json/')
//   .then(function (data) {
//     return data.json();
//   })
//   .then(function (endereco) {
//     console.log(endereco);
//   });

/* 
Ex. 5c
*/

console.log('Processando dados');

function jaRealizada() {
  return Promise.resolve('79032370');
}

jaRealizada()
  .then(function (cep) {
    return window.fetch(`https://viacep.com.br/ws/${cep}/json/`);
  })
  .then(function (data) {
    return data.json();
  })
  .then(function (endereco) {
    console.log(endereco);
  });
