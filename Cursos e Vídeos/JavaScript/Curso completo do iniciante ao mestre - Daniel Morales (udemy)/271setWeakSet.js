/* 
271. set e weakset
set possui valores únicos, diferentemente do array
*/

const arr = [1, 2, 3, 4, 2, 3, 5];

const _set = new Set();
const _weakset = new WeakSet();

_set.add(1);
_set.add(2);
_set.add(2);
_set.add(3);
_set.add(6);

console.log('_set.size :>> ', _set.size);
console.log('_set.has(6) :>> ', _set.has(6));
_set.delete(6);
console.log('_set.size :>> ', _set.size);
console.log('_set.has(6) :>> ', _set.has(6));

for (let el of _set) {
  console.log('el :>> ', el);
}

/* 
DIFERENÇA ENTRE SET E WEAKSET
quando não tem mais acesso a variável
garbage collector
se dá pra colocar valores primitivos; não dá pra colocar valores primitivos dentro de um weakset.
weakset:
.assim que o objeto que foi passado como referência for excluído, o weakset também vai ser limpo, por isso que não funciona com valores primitivos; só funciona com tipos de dados que são passados como referência.
. weakset também não é iterável; só é possível iterar sobre um set normal.
. o weakset só serve para armazenar referências a objetos
. weakset também não tem .size
. só tem .add, .delete, .has
. depois da função auto-invocável está preparado para ser limpo
*/

(function () {
  let obj1 = { foo: 'bar' };
  let obj2 = { foo2: 'bar2' };
  _set.add(obj1);
  _weakset.add(obj2);
});

console.log('_set.size :>> ', _set.size);

// _weakset.add(2);// dá erro
// _weakset.add('2');// dá erro

/* 
abaixo dá erro
for (let x of _weakset) {
  console.log('x :>> ', x);
}
*/
for (let x of _set) {
  console.log('x :>> ', x);
}
