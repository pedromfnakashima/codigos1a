/* 

*/

function Animal(tipo) {
  if (tipo) {
    this.tipo = tipo;
  }
}

//

Animal.prototype.obterTipo = function () {
  return this.tipo;
};

Animal.prototype.tipo = 'tipo desconhecido';

//

function Cachorro(nome, tipo) {
  this.nome = nome;
  Animal.call(this, tipo);
  this.constructor = Cachorro; // <= faz com que a propriedade constructor do objeto volte a ser Cachorro
}

// let rex = new Cachorro('Rex', 'mamifero');
// console.log('rex :>> ', rex);
// console.log('rex.constructor :>> ', rex.constructor);
// console.log('rex.__proto__ :>> ', rex.__proto__);

/* 
Vincular o protótipo do Cachorro com um objeto do tipo Animal
*/

Cachorro.prototype = new Animal();

let rex = new Cachorro('Rex', 'mamifero');
console.log('rex :>> ', rex);
console.log('rex.constructor :>> ', rex.constructor); // o construtor do rex não é mais o cachorro, mas passou a ser o Animal
console.log('rex.__proto__ :>> ', rex.__proto__);
console.log('rex.__proto__.__proto__ :>> ', rex.__proto__.__proto__); // protótipo da função construtora animal
console.log('rex.obterTipo() :>> ', rex.obterTipo());

/* loop */
console.log('-----------');

/* 
226
hasOwnProperty: verifica se a propriedade faz parte do próprio objeto em si, e não vai levar em consideração a cadeia de protótipo
instanceOf
isPrototypeOf
getPrototypeOf
*/

//--hasOwnProperty

// for (let prop in rex) {
//   // console.log('(todas) prop :>> ', prop);
//   if (rex.hasOwnProperty(prop)) { // verifica se a propriedade faz parte do próprio objeto em si, e não vai levar em consideração a cadeia de protótipo
//     console.log('(própria) prop :>> ', prop);
//   }
// }

//-- instanceof
/* 
Verificar se rex é instância de Animal.
Busca também na cadeia de protótipo.
Verifica se o objeto rex faz parte da cadeia de protótipo na qual estou buscando.
*/

console.log('rex instanceof Cachorro :>> ', rex instanceof Cachorro); // true

console.log('rex instanceof Animal :>> ', rex instanceof Animal); // true

console.log('rex instanceof Object :>> ', rex instanceof Object); // true

console.log('rex instanceof Array :>> ', rex instanceof Array); // false

//-- isPrototypeOf
/* 

*/

// Verifica se Cachorro é protótipo de rex.
console.log(
  'Cachorro.prototype.isPrototypeOf(rex) :>> ',
  Cachorro.prototype.isPrototypeOf(rex)
); // true

// Verifica se Animal é protótipo de rex.
console.log(
  'Animal.prototype.isPrototypeOf(rex) :>> ',
  Animal.prototype.isPrototypeOf(rex)
); // true

// Verifica se Object é protótipo de rex.
console.log(
  'Object.prototype.isPrototypeOf(rex) :>> ',
  Object.prototype.isPrototypeOf(rex)
); // true

//-- getPrototypeOf
/* 
Recupera o prototype do objeto rex.
*/

console.log('Object.getPrototypeOf(rex) :>> ', Object.getPrototypeOf(rex)); // Animal

console.log('rex.__proto__ :>> ', rex.__proto__);
console.log(
  'rex.__proto__ === Object.getPrototypeOf(rex) :>> ',
  rex.__proto__ === Object.getPrototypeOf(rex)
); // true

/* 
O objeto Object permite que eu crie propriedades que não sejam listadas.
-- Object.defineProperty()

*/

function Cachorro2(nome, tipo) {
  this.nome = nome;
  Animal.call(this, tipo);
  // this.constructor = Cachorro; // <= faz com que a propriedade constructor do objeto volte a ser Cachorro
  Object.defineProperty(Cachorro2.prototype, 'constructor', {
    value: Cachorro2,
    enumerable: false,
  }); // faz o mesmo da linha anterior, porém com a vantagem de poder passar (3º argumento) um objeto de configuração
}

let rex2 = new Cachorro2('Rex', 'mamifero');

console.log('-- Aula 226 --');
for (let prop in rex2) {
  console.log('prop :>> ', prop); // o prototype não é mostrado
}
