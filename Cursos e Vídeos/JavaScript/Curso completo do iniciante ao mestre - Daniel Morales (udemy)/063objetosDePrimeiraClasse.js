/*

-Funções do JS são objetos de primeira classe.
Funções em javascript são tratadas como qualquer outro objeto. A consequência disso é que:
* podem ser passadas como parâmetros para outras funções (call-back);
* podem ser atribuídas em propriedades de objetos (métodos);
* podem ser retornadas como resultado de outra função;
* podem ser suas próprias propriedades.

*/

//-- exemplo 1

// function fn(cb) {
//     console.log('executar ação de callback')
//     console.log(typeof cb)
//     cb()
// }

// fn(function(){
//     console.log('função passada por parâmetro')
// })

//-- exemplo 2 - verificar se é função mesmo que foi passado como parâmetro, utilizando o curto-circuito

// function fn(cb) {
//     console.log('executar ação de callback')
//     // console.log(typeof cb)
//     // lê-se (abaixo): se o tipo do objeto for função, então executa. Também poder ser feito com um IF.
//     typeof cb === 'function' && cb()
// }

//--- String é passada como parâmetro
// fn('abc') // sem erro

//--- Função ANÔNIMA é passada como parâmetro
// fn(function(){
//     console.log('função passada por parâmetro')
// })

//-- exemplo 3 - a função que é passada como parâmetro não precisa ser anônima; Na verdade, se for não anônima, fica até mais claro o código. Mas, da mesma forma como antes, a função é passada NÃO EXECUTADA

// function fn(cb) {
//     console.log('executar ação de callback')
//     // console.log(typeof cb)
//     // lê-se (abaixo): se o tipo do objeto for função, então executa. Também poder ser feito com um IF.
//     typeof cb === 'function' && cb()
// }

// function callback() {
//     console.log('função passada por parâmetro')
// }

// //--- Função NÃO ANÔNIMA é passada como parâmetro
// fn(callback)

/* 
- É possível atribuir funções a propriedades de objetos (como chaves do dicionário do python)
! Observação: quando a proprieade (chave) e o nome da função são o mesmo, basta colocar a função lá (sem a chave), que a chave, na hora da interpretação, vai ser o próprio nome da função. Ou seja, no código abaixo, são equivalentes:
const obj = {
    callback // quando chave = valor
}

! é equivalente a (chave:valor):

const obj = {
    callback: callback
}

! é equivalente a ('chave': valor) <<-- com aspas:

const obj = {
    'callback': callback
}

*/

// function callback() {
//     console.log('função passada por parâmetro')
// }

// // const obj = {
// //     callback
// // }

// // const obj = {
// //     callback: callback
// // }

// const obj = {
//     'callback': callback
// }



// obj.callback()

//- Retornando função como resultado de outra função

//-- exemplo 1 do Professor. (ideia de CLOSURE, também explicada pelo Corey Schafer)

// function mult(n1) {

//     return function(n2) {
//         return n1 * n2
//     }

// }

// const vezes10 = mult(10)
// const vezes3 = mult(3)

// const result1 = vezes10(2)
// const result2 = vezes3(2)

// console.log(result1)
// console.log(result2)


//-- exemplo 2 do professor

// function fn3() {
//     return function _fn3() { // pode ser função anônima ou nomeada, tanto faz
//         console.log('função retornada por parâmetro')
//     }
// }

// const funcao3 = fn3()
// funcao3()

//-- exemplo 3a do professor - função é obj de primeira classe => dá pra colocar propriedades dentro dela
//--- Conclusão: a função tem comportamento de classe do python

// function fn3() {
//     return function _fn3() { // pode ser função anônima ou nomeada, tanto faz
//         console.log('função retornada por parâmetro')
//     }
// }

// fn3.count = 0

// console.log(fn3.count)

// fn3.count += 1

// console.log(fn3.count)

//-- exemplo 3b do professor - função é obj de primeira classe => dá pra colocar propriedades dentro dela
//--- Conclusão: a função tem comportamento de classe do python
//--- Nesse exemplo 3b count acaba funcionando como um contador de quantas vezes eu chamei a função. Dá pra criar um sistema de cache dentro da função, com isso.

function fn3() {
    
    fn3.count += 1
    
    return function _fn3() { // pode ser função anônima ou nomeada, tanto faz
        console.log('função retornada por parâmetro')
    }
}

fn3.count = 0

const funcao3a = fn3()

console.log(fn3.count) // 1

const funcao3b = fn3()
const funcao3c = fn3()

console.log(fn3.count) // 3


//-- exemplo do Pedro.
// function f2() {

//     function f1() {
//         console.log('olá mundo')
//     }

//     return f1

// }

// teste = f2()
// teste()



