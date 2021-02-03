/* 
256. Object.create()
*/

const pai = {
  nome: 'pai',
  falar: function (msg) {
    console.log(`${this.nome} está falando.`);
  },
};

const filho = Object.create(pai, {
  nome: { value: 'junior', enumerable: true },
}); //! value é descritor

// console.log('filho :>> ', filho);
// console.log('filho.__proto__ :>> ', filho.__proto__);
// console.log('filho.falar() :>> ', filho.falar());

/* 
257. Object.assign()
Cria cópias de objeto.
Cria um objeto novo, colocando as propriedades dos métodos passados como parâmetros num objeto destino.
O método assign só vai copiar as propriedades enumeráveis. Como usamos o descritor (Object. create), a propriedade padrão é enumerable: false.
*/

const obj1 = {
  a: 'a',
  b: 'b',
  c: 'c',
};

const obj2 = {
  b: 'b2',
  d: 'd2',
};

/* abaixo colocamos uma prop não enumerável (padrão) em obj2 */
// Object.defineProperty(obj2, 'naoEnumeravel', {
//   value: 'nao enumeravel',
//   enumerable: false,
// });

Object.defineProperties(obj2, {
  naoEnumeravel: {
    value: 'VALOR DE NÃO ENUMERÁVEL',
    enumerable: false,
  },
  enumeravel: {
    value: 'VALOR DE ENUMERÁVEL',
    enumerable: true,
  },
});

// const filha = Object.assign(obj1, filho); // forma_1
/* 
{} é o objeto retornado que vai ser armazenado
*/
const filha = Object.assign({}, obj1, filho); // forma_1
obj1.d = 'd';

const clone = Object.assign(
  {},
  obj1,
  obj2
); /* quando tem propriedades de mesmo nome, faz com que o valor da última propriedade incluída prevalesça sobre o primeiro */

console.log('obj1 :>> ', obj1);
console.log('obj2 :>> ', obj2);
console.log('filha :>> ', filha); // forma_1-> com d,  // forma_2 -> com d
console.log('clone :>> ', clone);

/* clone do objeto com spread operator */

const obj3 = { ...obj1, ...obj2 };
const obj4 = { ...obj2, ...obj1 };
const obj5 = Object.assign({}, obj2);
console.log('obj3 :>> ', obj3);
console.log('obj4 :>> ', obj4);
console.log('obj5 :>> ', obj5);

/* 
258. Object.keys() values() e entries()
.keys, .values, .entries: não mostra propriedades não enumeráveis
*/

console.log('Object.keys(obj2) :>> ', Object.keys(obj2));
console.log('Object.values(obj2) :>> ', Object.values(obj2));
console.log('Object.entries(obj2) :>> ', Object.entries(obj2));

/* 
259. destructuring
(próximo arquivo)
*/
