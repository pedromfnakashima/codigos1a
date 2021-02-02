/* 
212. Métodos de objetos
*/

// ex. 1:

// const dog = {
//   name: 'rex',
//   falar: function () {
//     console.log(this.name, 'fala: au au');
//   },
// };
// dog.falar();

// ex. 2:

// function latir() {
//   console.log(this.name, 'fala: au au');
// }
// function miar() {
//   console.log(this.name, 'fala: miau');
// }

// const dog = {
//   name: 'rex',
//   falar: latir,
// };

// const cat = {
//   name: 'mingal',
//   falar: miar,
// };

// dog.falar();
// cat.falar();

// ex. 3:

function latir() {
  console.log(this.name, 'fala: au au');
}
function miar() {
  console.log(this.name, 'fala: miau');
}

const dog = {
  name: 'rex',
  falar() {
    console.log(this.name, ' fala: au au');
  },
  falar2() {
    console.log(this.name, ' falar2');
  },
};

const cat = {
  name: 'mingal',
  falar: miar,
};

dog.falar();
dog.falar2();
cat.falar();
