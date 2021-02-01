/* 
Criar duas funções: sum() e average()
. As funções podem receber 1 ou + parâmetros;
. Use e abuse das facilidades do ES6

*/

function sum() {
    //- Transformando arguments em array
    //-- Forma 1: Array.from()
    // const numbers = Array.from(arguments)
    //-- Forma 2: [...arguments]
    const numbers = [...arguments]
    // console.log(numbers)
    return numbers.reduce(function(sum,atual){
        return sum + atual
    },0)
    
}

function average() {
    return sum(...arguments) / arguments.length
}

let soma = sum(1,2,3,4,5)
let média = average(1,2,3,4,5)
console.log(soma)
console.log(média)











