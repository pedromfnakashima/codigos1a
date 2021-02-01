/* 
every
some
forEach
filter
map

*/

//- Exemplo 01 - every

// const arr = [1,5,10,'olá',true]

// let sohNumeros = arr.every(function(el){
//     // console.log(el)
//     return typeof el === 'number'
// })
// console.log(sohNumeros)

//- Exemplo 02 - some

// const arr = [1,5,10,'olá',true]

// let sohNumeros = arr.some(function(el){
//     // console.log(el)
//     return typeof el === 'number'
// })
// console.log(sohNumeros)

//- Exemplo 03 - some

// const arr = [1,5,10,'olá',true]

// let sohNumeros = arr.some(function(el){
//     // console.log(el)
//     return typeof el === 'number' && el > 20
// })
// console.log(sohNumeros)

//- Exemplo 04 - filter

// const arr = [1,5,10,'olá',true]

// let sohNumeros = arr.some(function(el){
//     // console.log(el)
//     return typeof el === 'number'
// })

// const arr1 = arr.filter(function(el, i, _arr) {
//     // console.log(el)
//     // console.log(i)
//     // console.log(_arr)
//     return typeof el === 'number'
// })

// // console.log(sohNumeros)
// console.log(arr1)

//- Exemplo 05 - forEach

// const arr = [1,5,10,'olá',true]

// let sohNumeros = arr.some(function(el){
//     return typeof el === 'number'
// })

// const arr1 = arr.filter(function(el, i, _arr) {
//     return typeof el === 'number'
// })

// const arr2 = arr.forEach(function(el, i, _arr) {
//     console.log(el, i, _arr)
// })

// console.log(arr2)

//- Exemplo 06 - map

// const arr = [1,5,10,'olá',true]
arr1 = [1,5,10]

let arr2 = arr1.map(function(el, i, _arr) {
    return el * el
})

console.log(arr1)
console.log(arr2)











