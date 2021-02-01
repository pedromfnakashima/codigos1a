/* 
concat
join
toString
*/

//- Exemplo 01 - toString

// let arr1 = [1, 2, 3]
// let arr2 = [5, 6, 7]

// console.log(arr1.toString())

//- Exemplo 02 - join

// let arr1 = [1, 2, 3]
// let arr2 = [5, 6, 7]

// console.log(arr1.join(' - '))

//- Exemplo 3 - concat

// let arr1 = [1, 2, 3]
// let arr2 = [5, 6, 7]

// let arr3 = arr1.concat(arr2,4,89,9,10,['olá','mundo'])
// console.log(arr1)
// console.log(arr2)
// console.log(arr3)

//- Exemplo 4 - atribuição da referência vs. criação de cópia
//-- Exemplo 4a - atribuição da referência (duas variáveis que apontam para o mesmo objeto) - comportamento igual ao do python

// let arr1 = ['a','b','c']
// let arr2 = arr1

// arr2[arr2.length] = 'novo valor'
// console.log(arr1)
// console.log(arr2)

//-- Exemplo 4b - cópia do array (duas variáveis que apontam para objetos diferentes) - método diferente de cópia, com relação ao python (.copy())

let arr1 = ['a','b','c']
let arr2 = [].concat(arr1) // cria uma cópia de arr1

arr2[arr2.length] = 'novo valor'
console.log(arr1)
console.log(arr2)









