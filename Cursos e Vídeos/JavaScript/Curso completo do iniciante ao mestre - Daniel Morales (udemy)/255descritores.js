'use strict';
/* 
Definindo propriedades de um objeto da forma tradicional.
Padrão:
configurable: true, enumerable: true, writable: true
*/

const pessoa = {
  nome: 'Pedro',
};

/* propriedades do objeto */
console.log(
  'Object.getOwnPropertyDescriptor(pessoa,"nome") :>> ',
  Object.getOwnPropertyDescriptor(pessoa, 'nome')
);

/*
Definindo propriedades de um objeto com o Object.defineProperty
com defineProperty é possível mudar o descritor
Se a propriedade já existe, vai alterar o descritor da propriedade; se a propriedade não existe, cria outra propriedade.
Padrão:
configurable: false, enumerable: false, writable: false
*/
Object.defineProperty(pessoa, 'sobrenome', {
  value: 'Nakashima',
  enumerable: true,
  configurable: true,
  writable: true,
});

console.log(
  'Object.getOwnPropertyDescriptor(pessoa,"sobrenome") :>> ',
  Object.getOwnPropertyDescriptor(pessoa, 'sobrenome')
);

// pessoa.sobrenome = 'aasfdjdf'; // não altera - se tá com 'use strict', dá erro
/* também não funciona o looping (porque enumerable:false): */
for (let prop in pessoa) {
  console.log('prop :>> ', prop);
}

/* dá erro porque configurable: false */
// delete pessoa['sobrenome'];
/* dá erro porque configurable: false */
// Object.defineProperty(pessoa, 'sobrenome', {
//   configurable: true
// })
/* possível mesmo com configurable: false, desde que antes writable:true */
Object.defineProperty(pessoa, 'sobrenome', {
  writable: false,
});

/* possível */
Object.defineProperties(pessoa, {
  prop1: {
    value: 'prop 1',
    writable: true,
  },
  prop2: {
    writable: false,
    value: 10,
  },
});

console.log('pessoa :>> ', pessoa);
