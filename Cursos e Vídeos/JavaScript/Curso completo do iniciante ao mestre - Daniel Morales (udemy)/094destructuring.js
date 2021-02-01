/* 
! Sintaxe: const [x] = []
Serve p/ recuperar variáveis de uma array
!Semelhante ao unpacking do python
*/

const arr = [10,20,30]

//-- Pega a primeiro valor do array e coloca em n1
// const [n1] = arr
//-- Pega o primeiro, o segundo e o terceiro valores do array, e coloca, respectivamente, em n1, n2 e n3
// const [n1,n2,n3] = arr

// console.log(n1)
// console.log(n2)
// console.log(n3)

//-- Pega o primeiro valor e coloca em n1, e o resto em n2
// const [n1,...n2] = arr

// console.log(n1)
// console.log(n2)

//-- Pega o primeiro valor e coloca em n1, e o último em n2
const [n1,,n2] = arr

console.log(n1)
console.log(n2)



