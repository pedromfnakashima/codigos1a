/* 
indexOf
lastIndexOf
includes
findIndex
find

*/

//- Exemplo 01: indexOf e lastIndexOf
/* 
indexOf: Retorna o primeiro valor encontrado; não encontrado -> -1
lastIndexOf: Retorna o último valor encontrado
*/
// let arr = [4, 5, 10, 20, 35, 4, 5]

// console.log(arr.indexOf(5))
// console.log(arr.lastIndexOf(5))
// console.log(arr.indexOf(55))

//- Exemplo 02: includes
/* 
include: retorna true ou false se o valor procurado for encontrado ou não
*/
// let arr = [4, 5, 10, 20, 35, 4, 5]

// console.log(arr.includes(5))
// console.log(arr.includes(5555))
// console.log(arr.indexOf(555) > -1)

//- Exemplo 02: find e findIndex
/* 
find: retorna o primeiro valor encontrado que satisfaça uma condição posta numa função de callback; se não encontra nada, retorna undefined.
findIndex: retorna o índice do primeiro valor encontrado que satisfaça uma condição posta numa função de callback; se não encontra nada, retorna -1.
*/
let arr = [4, 5, 10, 20, 35, 4, 5]

console.log(arr.find(function(el){
    return el > 10
}))

console.log(arr.findIndex(function(el){
    return el > 10
}))








