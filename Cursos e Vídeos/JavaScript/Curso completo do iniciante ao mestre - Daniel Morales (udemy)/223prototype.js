/* 
223. prototype
*/

/*  */

function Animal(tipo) {
  if (tipo) {
    this.tipo = tipo;
  }
}

let cachorro = new Animal('mamifero');

console.log('cachorro :>> ', cachorro);
console.log('Animal.prototype :>> ', Animal.prototype);
console.log('Object :>> ', Object);
console.log('Object.prototype :>> ', Object.prototype);
console.log('cachorro.__proto__ :>> ', cachorro.__proto__);

/* 
__proto__ é uma forma de, a partir do objeto, acessar o objeto que está guardado na propriedade prototype da função construtora.
A propriedade prototype da função construtora Animal é um objeto.
A partir do objeto criado pela função construtora, eu tenho uma propriedade __proto__ que eu consigo ter acesso ao objeto que foi armazenado dentro de prototype.
*/

console.log(
  'cachorro.__proto__ === Animal.prototype :>> ',
  cachorro.__proto__ === Animal.prototype
); // true, pois são a mesma coisa, pois se trata da referência (posição na memória)

Animal.prototype.obterTipo = function () {
  return this.tipo;
};

Animal.prototype.tipo = 'tipo desconhecido';

console.log('cachorro.obterTipo() :>> ', cachorro.obterTipo());
console.log('cachorro.toString() :>> ', cachorro.toString());
console.log('cachorro.__proto__.__proto__ :>> ', cachorro.__proto__.__proto__);
console.log(
  'cachorro.__proto__.__proto__ === Object.prototype :>> ',
  cachorro.__proto__.__proto__ === Object.prototype
); // true

let gato = new Animal('mamífero');
let cobra = new Animal('reptil');
let peixe = new Animal();

console.log('peixe.obterTipo() :>> ', peixe.obterTipo());

/* 

*/
let arr = new Array(1, 2, 3);
console.log('arr.__proto__ :>> ', arr.__proto__);
console.log(
  'arr.__proto__ === Array.prototype :>> ',
  arr.__proto__ === Array.prototype
); // true

console.log('Array.prototype :>> ', Array.prototype);

Array.prototype.map2 = function () {};
console.log('arr.map2() :>> ', arr.map2());

// Função construtora
console.log('cachorro.constructor :>> ', cachorro.constructor);
