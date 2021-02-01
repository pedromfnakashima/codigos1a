/* 
push
pop
shift
unshift
slice
splice
*/

//- Exemplo 01 - push
/* 
push: acrescenta valores no fim do array original (o modifica), mas retorna o novo length do array
*/

// let arr = [1, 3, 5, 7, 9]
// let teste = arr.push(11, 13, true, 'olá mundo')

// console.log(teste)
// console.log(arr)

//- Exemplo 02 - pop
/* 
push: remove o último elemento do array (modificando o array original), e retorna o valor removido
*/

// let arr = [1, 3, 5, 7, 9]
// let ultimoItem = arr.pop()

// console.log(ultimoItem)
// console.log(arr)

//-- Exemplo 02a - retornando o último item sem modificar o array original

// let arr = [1, 3, 5, 7, 9]
// let ultimoItem = arr[arr.length - 1]

// console.log(ultimoItem)
// console.log(arr)

//- Exemplo 03 - shift
/* 
shift: remove o primeiro elemento do array (modificando o array original), e retorna o valor removido
*/

// let arr = [1, 3, 5, 7, 9]
// let primeiroItem = arr.shift()

// console.log(primeiroItem)
// console.log(arr)

//- Exemplo 04 - unshift
/* 
unshift: inclui no início do array, retornando o novo length
*/

// let arr = [1, 3, 5, 7, 9]
// let teste = arr.unshift(4,5,6)

// console.log(teste)
// console.log(arr)

//- Exemplo 05 - slice
/* 
slice: recortar um pedaço do array, o array original permanecendo intacto.
*/

// let arr = [1, 3, 5, 7, 9]
// let arr2 = arr.slice(2,4)
// // let arr2 = arr.slice(2) // sem valor final, vai até o final do array

// console.log(arr)
// console.log(arr2)

//- Exemplo 06 - splice
/* 
splice: remove elementos do array original, retornando os valores removidos.
Modifica o array original.
*/

let arr = [1, 3, 5, 7, 9]
let arr2 = arr.splice(2,2,'olá mundo') // a partir do 2, remove 2 elementos, e adiciona outro elemento ('olá mundo')
// let arr2 = arr.splice(2,2) // a partir do 2, remove 2 elementos
// let arr2 = arr.splice(2) // a partir do 2, remove tudo


console.log(arr)
console.log(arr2)




