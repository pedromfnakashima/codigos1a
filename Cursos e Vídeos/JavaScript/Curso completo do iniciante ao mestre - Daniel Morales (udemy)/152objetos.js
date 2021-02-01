/* 
- 153. OPERADOR NEW
*/

//
// const obj1 = {
//   nome: 'Pedro',
// };

// const obj2 = new Object();
// obj2['nome'] = 'Maria';
// obj2.idade = 28;

// console.log(obj1);
// console.log(obj2);

// // acesso a propriedades de dados primitivos
// const str1 = 'minha string';
// console.log(str1.length);

// const str2 = new String('minha string 2');
// console.log(str2);
// console.log(str2.length);

/* 
No chrome:
const str2 = new String('minha string 2');
console.log(str2);
console.log(str2.length);
str2.valueOf() <= valueOf() retorna o valor primitivo
new Number(20)
new Boolean('kkk')
//[[PrimitiveValue]]


operador new => construtor

*/

//

// const data1 = Date();
// console.log(data1); // Wed Jan 27 2021 07:55:11 GMT-0400 (Horário Padrão do Amazonas)
// console.log(typeof data1); // string

//

// const data2 = new Date();
// console.log(data2); // 2021-01-27T11:56:26.351Z
// console.log(typeof data2); // object

/* 
- 154. VALORES VS. REFERÊNCIA
Abaixo, quando passo a variável p/ a função, não passei a variável em si, mas o valor da variável; a variável x continua intacta.
*/
// let x = 10;
// function mudaX(x) {
//   x++;
//   console.log('x interno', x);
// }
// mudaX(x);
// console.log('x externo', x);

/* Quando passo uma array (ou objeto), o que eu passo é uma referência da array; o x de dentro é exatamente o mesmo de fora; alterações do array dentro ocorrem na array de fora, pois se passou apenas uma array*/

// let x = [10];
// let y = { n: 10 };
// function mudaX(x) {
//   x.push(11);
//   console.log('x interno', x);
// }
// mudaX(x);
// console.log('x externo', x);

// function mudaY(obj) {
//   obj.n++;
//   console.log('y interno', obj);
// }
// mudaY(y);
// console.log('y externo', y);

/* 
no chrome
{} === {} // false, pois são dois objetos diferentes com referências na memória diferentes
[] === [] // false, pois são dois objetos diferentes com referências na memória diferentes
[1,2] === [1,2] // false, pois são dois objetos diferentes com referências na memória diferentes
'2' === '2' // true, pois está comparando o valor e não mais a referência na memória
new String('s') === new String('s') // false, pois são dois objetos diferentes com referências na memória diferentes

- 155. OBJETOS CUSTOMIZADOS - POR QUE UTILIZAR, EM ALGUNS MOMENTOS AS FUNÇÕES CONSTRUTURAS DE OBJETOS?
Com repetição de código.
*/

// const task1 = {
//   name: 'task 1',
//   createdAt: new Date(),
//   updatedAt: null,
//   completed: false,
// };

// const task2 = {
//   name: 'task 2',
//   createdAt: new Date(),
//   updatedAt: null,
//   completed: false,
// };

// task1.name = 'task 1 updated';
// task1.updatedAt = new Date();

// console.log(task1);
// console.log(task2);

/* 
o ideal aqui é ter uma função que vai receber um novo valor e vai atualizar o nome e atualizar o updatedAt
//-- Função externa para alterar a propriedade
*/

function changeName(name) {
  // console.log('name :>> ', name);
  // console.log('this :>> ', this);
  this.name = name;
  this.updatedAt = new Date();
}

const task1 = {
  name: 'task 1',
  createdAt: new Date(),
  updatedAt: null,
  completed: false,
  // changeName: changeName,
  changeName,
};

const task2 = {
  name: 'task 2',
  createdAt: new Date(),
  updatedAt: null,
  completed: false,
  changeName,
};

task1.updatedAt = new Date();

// changeName('fora de objeto'); // function expression: this = objeto global; arrow function: this = não muda
task1.changeName('nome atualizado');
// console.log('task1 :>> ', task1);

task2.changeName('nome p/ teste 2');
// console.log('task2 :>> ', task2);

/* 
-156 FUNÇÕES CONSTRUTORAS
*/

// function Task(name) {
//   this.name = name;
//   this.createdAt = new Date();
//   this.updatedAt = null;
//   this.changeName = function (newName) {
//     this.name = newName;
//     this.updatedAt = new Date();
//   };
// }

// const task3 = new Task('minha tarefa');
// console.log('task3 :>> ', task3);
// task3.changeName('mudado por função');
// console.log('task3 :>> ', task3);

/* 
-- Para não permitir que  usuário altere o nome da tarefa diretamente. Ex.:
task1.name = 'nome_qualquer'
*/

// function Task(name) {
//   let _name = name;

//   this.createdAt = new Date();
//   this.updatedAt = null;
//   this.changeName = function (newName) {
//     if (newName) {
//       // faz com que, se não passa nenhum nome, não faz nada
//       _name = newName;
//       this.updatedAt = new Date();
//     }
//   };
//   this.getName = function () {
//     return _name;
//   };
// }

// const task3 = new Task('minha tarefa');
// task3.changeName('mudado por função');
// console.log('task3 :>> ', task3);
// console.log('task3.name :>> ', task3.name); // undefined
// console.log('task3._name :>> ', task3._name); // undefined
// console.log('task3.getName() :>> ', task3.getName()); // mudado por função
// task3.changeName('lálálá');
// console.log('task3.getName() :>> ', task3.getName()); //lálálá
// task3.changeName();
// console.log('task3.getName() :>> ', task3.getName()); //lálálá

/* 
- 157. obrigar o uso do operador new nos nossos contrutores => 'use strict'
Quando o usuário não utilizar o operador new na função construtora, o this interno vai ser o escopo global, e isso tem um pequeno problema.


*/

// const task4 = Task('minha segunda tarefa');
// console.log('task4 :>> ', task4); // undefined <= problema

// function Task(name) {
//   'use strict';
//   let _name = name;

//   this.createdAt = new Date();
//   this.updatedAt = null;
//   this.changeName = function (newName) {
//     if (newName) {
//       // faz com que, se não passa nenhum nome, não faz nada
//       _name = newName;
//       this.updatedAt = new Date();
//     }
//   };
//   this.getName = function () {
//     return _name;
//   };
// }

// // const task5 = Task('bla bla bla'); //! com erro
// const task5 = new Task('bla bla bla'); //! sem erro
// console.log('task5 :>> ', task5);

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */

/*  */
