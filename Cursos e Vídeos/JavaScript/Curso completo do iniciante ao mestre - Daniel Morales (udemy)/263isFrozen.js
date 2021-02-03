/* 
263. isFrozen
OUTROS (264):
Outros métodos de checagem
Assim como temos o método isFrozen() para verificar se um objeto está freeze ou não, temos mais dois métodos com nomes bastante auto-explicativos:

Object.isSealed() - https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Object/isSealed

Object.isExtensible() - https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Object/isExtensible
*/

const obj1 = {
  nome: 'Pedro',
};

const obj2 = {
  nome: 'Maria',
};

Object.freeze(obj1);

/* as três configurações abaixo em obj2 (writable, configurable, preventExtensions) equivalem a .freeze */
Object.defineProperty(obj2, 'nome', {
  writable: false,
  configurable: false,
});
Object.preventExtensions(obj2);

console.log('Object.isFrozen(obj1) :>> ', Object.isFrozen(obj1));
console.log('Object.isFrozen(obj2) :>> ', Object.isFrozen(obj2));
