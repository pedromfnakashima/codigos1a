/* 
A função construtora é necessária quando a regex tem que ser dinâmica
*/

let str = 'hoje é meu dia preferido 26/02/2018. Meu aniversário é 1 de jan';
//- Com o //
// const regex = /02/;
// const regexG = /02/g;
//- Com o construtor new RegExp()
/* 
Argumentos:
1. regex;
2. flags;
*/
//-- não dinâmico
// const regexG = new RegExp('02', 'g');
//-- dinâmico

//--- Exemplo 1: com a flag g (global)

// let teste = '02';
// const regexG = new RegExp(teste, 'g');

// console.log('regexG.exec(str) :>> ', regexG.exec(str));
// console.log('regexG.exec(str) :>> ', regexG.exec(str));

//--- Exemplo 2: sem a flag g (global)

// let strRegex = 'meu';
// const regexG = new RegExp(strRegex);

// console.log('regexG.exec(str) :>> ', regexG.exec(str));
// console.log('regexG.exec(str) :>> ', regexG.exec(str));

//--- Exemplo 3: com as flags g (global) e i (case insensitive)

// let strRegex = 'meu';
// const regexG = new RegExp(strRegex, 'gi');

// console.log('regexG.exec(str) :>> ', regexG.exec(str)); // Primeira ocorrência: meu (minúsculo)
// console.log('regexG.exec(str) :>> ', regexG.exec(str)); // Primeira ocorrência: Meu (maiúsculo)

//--- Exemplo 4: passando caracteres especiais
//! precisa colocar uma barra a mais. Ex.: \\w, \\s, \\b (que nem no R)

let strRegex = 'meu';
const regexG = new RegExp('\\w', 'gi');

console.log('regexG.exec(str) :>> ', regexG.exec(str)); // Primeira ocorrência: meu (minúsculo)
console.log('regexG.exec(str) :>> ', regexG.exec(str)); // Primeira ocorrência: Meu (maiúsculo)
