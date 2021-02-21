/* 
Aula 374
*/

// const fs = require('fs');
// const emoji = require('node-emoji');

// fs.writeFile('teste.txt', 'olá, mundo', (err) => {
//   if (err) throw err;
//   console.log('Salvo com sucesso!', emoji.get('coffee'));
// });

/* 
Aula 375
*/

// const teste = require('./modules/mod1.js');
const fn = require('./modules/mod1.js');

// console.log('teste :>> ', teste);

/* console.log('fn :>> ', fn);
console.log('fn() :>> ', fn());
 */

/* Aula 376 */

const mod2 = require('./modules/mod2.js');
const mod3 = require('./modules/mod3.js');

console.log('mod2 :>> ', mod2);
console.log('mod3 :>> ', mod3);

//- Sem erro (duas linhas abaixo)
console.log('__dirname :>> ', __dirname);
console.log('__filename :>> ', __filename);
