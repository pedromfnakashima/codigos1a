

/* 

- HTML COLLECTION
getElementsByTAgName()
getElementsByClassName()
. Vivo => se atualiza na medida em que o DOM sofre atualização (seja via getElement, seja via querySelector).

- NODE LIST
querySelectorAll
. Estático => não se atualiza na medida em que o DOM sofre atualização (seja via getElement, seja via querySelector)..

*/

const nodelist = document.querySelectorAll('#list li')

const collection = document.getElementById('list').getElementsByTagName('li')

console.log(nodelist) // 5 elementos
console.log(collection) // 5 elementos

document.querySelector('#list').innerHTML += '<li> Item 6 </li>' // Adiciona 1 elemento ao DOM
console.log(' ---- ATUALIZOU O DOM ----- ')

console.log(nodelist) // 5 elementos
console.log(collection) // 6 elementos

document.querySelector('#list').innerHTML += '<li> Item 7 </li>' // Adiciona 1 elemento ao DOM
console.log(' ---- ATUALIZOU O DOM ----- ')

console.log(nodelist) // 5 elementos
console.log(collection) // 7 elementos

document.getElementById('list').innerHTML = '' // Limpa o DOM
console.log(' ---- ATUALIZOU O DOM ----- ')

console.log(nodelist) // 5 elementos
console.log(collection) // 0 elementos














