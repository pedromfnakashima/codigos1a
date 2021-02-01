/* 
reverse
reduce
Desafio
*/

//- Exemplo 01 - reverse
/* 
Inverte a ordem do array, modificando a array original
*/
// arr = [1, 2, 3]
// console.log(arr.reverse())
// console.log(arr)

//- Exemplo 02 - reduce
/* 
Faz um loop, aplica uma função.
Retorna um único valor.

!Sintaxe:

let abc = array.reduce(função, tipo de dado a ser recebido)
Exemplos:
let abc = arr.reduce(function(acumulador,atual,i,_arr){}, {})
let nomesPorOrdem = nomes.reduce(function(acumulador,atual,i,_arr){}, 0)
let nomesPorOrdem = nomes.reduce(function(acumulador,atual,i,_arr){}, '')
let nomesPorOrdem = nomes.reduce(function(acumulador,atual,i,_arr){}, {})
const numerosUnicos = numeros.reduce(function(){},[])


*/
//-- Acumulador inicial é 0
// arr = [1, 2, 3, 4]

// let j = 0
// let soma = arr.reduce(function(acumulador,atual,i,_arr){
//     console.log(`i: ${i}`)
//     console.log(`j: ${j++}`)
//     console.log(`acumulador: ${acumulador}`, `atual: ${atual}`)
//     return acumulador + atual
// }, 0)
// console.log('--------------------')
// console.log(`arr: ${arr}`)
// console.log(`soma: ${soma}`)

//-- Acumulador inicial é uma string
// arr = [1, 2, 3, 4]

// let j = 0
// let soma = arr.reduce(function(acumulador,atual,i,_arr){
//     console.log(`i: ${i}`)
//     console.log(`j: ${j++}`)
//     console.log(`acumulador: ${acumulador}`, `atual: ${atual}`)
//     return acumulador + atual
// }, '---')
// console.log('--------------------')
// console.log(`arr: ${arr}`)
// console.log(`soma: ${soma}`) // concatenou

//-- Array de nomes, contagem das letras iniciais, utilizando o reduce
/* 
Contar nomes que começam com determinada letra.
*/
// const nomes = ['Daniel','Maria','Joana','João']

// let nomesPorOrdem = nomes.reduce(function(nomes,nomeAtual){
//     /* 
//     nomes = acumulador
//     nomeAtual = atual
//     */
//     let primeiraLetra = nomeAtual[0]
//     if (nomes[primeiraLetra]) { // verifica se existe uma chave ('propriedade')
//         nomes[primeiraLetra] += 1
//     }
//     else {
//         nomes[primeiraLetra] = 1
//     }
//     return nomes
// }, {})
// console.log(nomesPorOrdem)

//-- Array com números únicos, utilizando o reduce

const numeros = [1,3,4,1,4,5,3,5,8,9]

const numerosUnicos = numeros.reduce(function(numerosUnicos,numeroAtual){
    if (numerosUnicos.indexOf(numeroAtual) < 0) {
        numerosUnicos.push(numeroAtual)
    }
    return numerosUnicos
},[])

console.log(numerosUnicos)



