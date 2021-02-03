/* 
261. deep freeze
*/

const obj1 = {
  foo: 'bar',
  internalProp: {},
};

Object.freeze(obj1); // <= congela o objeto externo
Object.freeze(obj1.internalProp); // <= congela o objeto interno

// Primeira camada
console.log('obj1 :>> ', obj1);
obj1.foo = 'alterado';
console.log('obj1 :>> ', obj1);

// Segunda camada
obj1.internalProp.foo = 'bar 2';
console.log('obj1 :>> ', obj1);

/* Fazendo o Object.freeze de forma recursiva, para atingir internamente todos os objetos */

function deepFreeze(obj) {
  const propNames = Object.getOwnPropertyNames(obj); // retorna todas as propriedades, inclusive as não enumeráveis
  propNames.forEach((name) => {
    let prop = obj[name];

    if (typeof prop === 'object' && prop !== null) {
      // porque typeof null === object
      deepFreeze(prop);
    }
  });
  return Object.freeze(obj);
}

const obj2 = {
  foo: 'bar',
  internalProp: {
    array: [1, 2, 3],
    internalObject: { teste: 'teste' },
  },
};
deepFreeze(obj2);

console.log('obj2 :>> ', obj2);
obj2.foo = 'alterado';
// obj2.internalProp.array.push('alterado');
obj2.internalProp.internalObject.teste = 'alterado';
console.log('obj2 :>> ', obj2);

/* 
263. isFrozen
verifica se um objeto está congelado ou não
próximo arquivo
*/
