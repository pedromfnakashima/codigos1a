/* 
265. Symbols
é um tipo de dado que possui uma chave única.
Não pode ser utilizado com o operador new.

Utiliade do Symbol: minimizar a chance da propriedade ser sobrescrita por engano.

--- Abaixo, na definição do objeto, o colchetes vai interpretar um código javaScript e vai colocar o código interpretado como o nome da propriedade, DINAMICAMENTE.
O nome disso é COMPUTED PROPERTY NAME
Referências:
https://ui.dev/computed-property-names/
https://medium.com/front-end-weekly/javascript-object-creation-356e504173a8
http://www-lia.deis.unibo.it/materiale/JS/developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer.html
*/

const NOME = Symbol();
console.log('typeof NOME :>> ', typeof NOME);

let n = 0;
const user = {
  ['teste' + ++n]: 'a' + n,
  ['teste' + ++n]: 'b' + n,
  ['teste' + ++n]: 'c' + n,
  [NOME]: 'com symbol',
  nome: 'com string',
  3: 'com número',
};
console.log('user :>> ', user);

/*  */
user.nome = 'nome alterado';

console.log('user :>> ', user);

console.log('user[NOME] :>> ', user[NOME]);

// console.log(
//   'Object.getOwnPropertySymbols(user) :>> ',
//   Object.getOwnPropertySymbols(user)
// );

let teste = Object.getOwnPropertySymbols(user);
console.log('teste[0] :>> ', teste[0]);
console.log('user[teste[0]] :>> ', user[teste[0]]);
console.log('typeof user[teste[0]] :>> ', typeof user[teste[0]]);
user[teste[0]] = 'nome alterado';
console.log('user :>> ', user);
