import { MyMod2 } from './mod2.js';

function f_myMod1() {
  console.log('myMod 1 executado');
  return 'valor retornado de myMod1';
}

export function myMod1_nomeada() {
  return 'função exportada nomeada';
}

// export const PI = Math.PI;
export const PI = 'PI: ' + Math.PI;

export const obj = {
  foo: true,
  bar: 'olá mundo',
};

const nome = 'pedro';
const idade = 36;

// Abaixo, não estou exportando um objeto, mas utilizando um destructuring para exportar as propriedades nome e idade
export { nome, idade };
/* 
Equivalente a:
export const nome = 'pedro'
export const idade = 36
*/

console.log('new MyMod2() :>> ', new MyMod2());

export default f_myMod1;
