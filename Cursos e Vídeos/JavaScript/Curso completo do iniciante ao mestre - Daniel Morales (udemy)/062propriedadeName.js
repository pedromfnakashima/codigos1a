// retorna o nome da própria função

//-- exemplo 1

// function olaMundo() {
//     console.log('abc')
// }

// olaMundo()

// console.log(olaMundo.name) // olamundo

//-- exemplo 2

// teste = function olaMundo() {
//     console.log('abc')
// }

// teste()

// console.log(teste.name) // olamundo

//-- exemplo 3

// teste = function() {
//     console.log('abc')
// }

// teste()

// console.log(teste.name) // teste

//-- exemplo 4 - arrow function

const teste = () => {
    console.log('abc')
}

teste()

console.log(teste.name) // teste

