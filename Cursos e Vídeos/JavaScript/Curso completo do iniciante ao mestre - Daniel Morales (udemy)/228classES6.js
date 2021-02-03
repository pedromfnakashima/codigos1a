/* 
228. class(ES6)
*/

// ES 5
function Animal(tipo) {
  if (tipo) {
    this.tipo = tipo;
  }
}

Animal.prototype.tipo = 'tipo desconhecido';

Animal.prototype.obterTipo = function () {
  return this.tipo;
};

let gato = new Animal('mamífero');

// ES 6

class AnimalC {
  constructor(tipo) {
    if (tipo) {
      this.tipo = tipo;
    }
  }

  obterTipo() {
    return this.tipo;
  }
}

AnimalC.prototype.tipo = 'tipo desconhecido';

// comparação animal e gato

let animal = new AnimalC('anfíbio');
let sapo = new AnimalC();

// console.log('animal :>> ', animal);
// console.log('gato :>> ', gato);

/* 
AnimalC também é uma função
*/

// console.log('typeof Animal :>> ', typeof Animal); // function
// console.log('typeof AnimalC :>> ', typeof AnimalC); // function

// console.log('gato.obterTipo() :>> ', gato.obterTipo());
// console.log('animal.obterTipo() :>> ', animal.obterTipo());

// console.log('Animal.prototype :>> ', Animal.prototype);
// console.log('AnimalC.prototype :>> ', AnimalC.prototype);

/* 
229. extends
-- Diferenças entre usar a palavra FUNCTION e a palavra CLASS
. Function: 
. Class: 

*/
console.log(
  'Aula 229 - Diferenças entre usar a palavra FUNCTION e a palavra CLASS'
);

/*  Palavra Function */
// Animal('teste tipo');
// console.log('tipo :>> ', tipo);

// function AnimalES5(tipo) {
//   if (this instanceof Animal) {
//     if (tipo) this.tipo = tipo;
//   } else {
//     throw new Error('Animal must be created with new operator');
//   }
// }

// AnimalES5('teste tipo'); // erro

/* Palavra Class */
// AnimalC('aaabbb'); // erro

// console.log('Object.getPrototypeOf(gato) :>> ', Object.getPrototypeOf(gato));

console.log('Aula 229 - Herança utilizando o ES 2015');

class GatoC extends AnimalC {
  constructor(nome) {
    super('mamifero');
    this.nome = nome;
  }
}

let mingal = new GatoC('mingal');
console.log('mingal :>> ', mingal);
