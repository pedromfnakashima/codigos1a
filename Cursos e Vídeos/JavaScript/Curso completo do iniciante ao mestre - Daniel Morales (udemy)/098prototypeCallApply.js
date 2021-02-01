/* 

Rever esse código, e estudar. O conhecimento não ficou redondinho como nos outros.

Antigamente (ES5), quando não tinha spread operator e outras facilidades do ES novo
Array.prototype.<<método>>.call()
Array.prototype.<<método>>.apply()

Funções do desafio do arquivo 096
*/

function sum() {
    //! arguments, por não ser array, não tem o método reduce()
    //-- Abordagem 1: transformar em array
    // const numbers = []
    // for (let i=0; i<arguments.length; i+=1) {
    //     numbers.push(arguments[i])
    // }
    // console.log(numbers)
    //-- Abordagem 2: usar o prototype -> local de onde "se empresta" as funções do array
    const numbers = []
    //! O segundo argumento, é o mesmo da função de array .forEach (uma função qualquer que vai manipular cada elemento); o primeiro é o arguments. Prototype é necessário porque arguments não tem o método de array .forEach, mas é array-like. A forma de pegar emprestado método de array é usando a sintaxe:
    //!! Array.prototype.função_array(arguments, função_trata_elemento)
    Array.prototype.forEach.call(arguments, function(argument){
        numbers.push(argument)
    })
    // console.log(numbers)
    //-- Agora numbers é array, por isso dá pra usar o método de array .reduce sem o Array.prototype
    return numbers.reduce(function(sum,atual){
        return sum + atual
    },0)

}

function average() {
    const soma = sum.apply(null, arguments)
    // console.log(soma)
    return soma / arguments.length
}
console.log(average(1,2,3,4,5)) //

//- 3 Formas de executar uma função
//-- Forma 1: ()
// sum(1,2,3,4,5)
//-- Forma 2: .call() <== permite mudar o escopo do this; passa os argumentos SEPARADOS
// sum.call(null,1,2,3,4,5)
//-- Forma 3: .apply() <== passa os argumentos como array
// sum.apply(null,[1,2,3,4,5])

// sum(1,2,3,4,5)

// console.log(sum(1,2,3,4,5)) // 15






