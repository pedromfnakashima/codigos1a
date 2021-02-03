/* 
268. Map e WeakMap
ao contrário do Symbol, aqui utiliza-se o operador new.
Podemos definir qualquer valor como sendo a chave.
*/

/* ex.1 */

const myMap = new Map();
const myObj = new Object();

myObj.prop1 = 'prop 1';

// myMap.set('prop1', 'prop 1');
// console.log('myMap.get("prop1") :>> ', myMap.get('prop1'));

// myMap.set(true, false);
// console.log('myMap.get(true) :>> ', myMap.get(true));

// myMap.set(myObj, 'meu objeto');
// console.log('myMap.get(myObj) :>> ', myMap.get(myObj));

const arr = [];
myMap.set(arr, myObj);
console.log('myMap.get(arr) :>> ', myMap.get(arr));

/* ex. 2 */

const myMap2 = new Map([
  [0, 'zero'],
  [1, 'um'],
  [2, 'dois'],
]);
// console.log('myMap2.get(0) :>> ', myMap2.get(0));
// console.log('myMap2.get(2) :>> ', myMap2.get(2));
// console.log('myMap2.has(2) :>> ', myMap2.has(2));
// console.log('myMap2.keys() :>> ', myMap2.keys());
// console.log('myMap2.values() :>> ', myMap2.values());
// console.log('myMap2.entries() :>> ', myMap2.entries());

// let keys = myMap2.keys();
// for (let k of keys) {
//   console.log('k :>> ', k);
// }

// let values = myMap2.values();
// for (let v of values) {
//   console.log('v :>> ', v);
// }

/* 
DIFERENÇAS
se o objeto não for mais acessível
iterações

weakmap

map

*/

let _contador = new WeakMap();

class Contador {
  constructor() {
    // this.contador = 0;
    _contador.set(this, 0);
  }
  increment() {
    // this.contador++;
    _contador.set(this, _contador.get(this) + 1);
    // console.log('this.contador :>> ', this.contador);
    console.log('_contador.get(this) :>> ', _contador.get(this));
  }
  get contador() {
    return _contador.get(this);
  }
}

console.log('---------------');
const c1 = new Contador();
c1.increment();
console.log('c1.contador :>> ', c1.contador);
c1.increment();
c1.increment();
c1.increment();
console.log('c1.contador :>> ', c1.contador);
