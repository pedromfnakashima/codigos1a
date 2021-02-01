
//- ex.1 Função de fora, que utiliza como argumento outra função (a função de callback)

// function teste(cb) {
//     console.log('função teste')
//     cb()
// }

//-- ex.1a executando e passando como argumento (sem executar) uma função anônima
// teste(function() { // 
//     console.log('função anônima de callback')
// })

//-- ex.1b executando e passando como argumento (sem executar) uma função não anônima

// function fn() {
//     console.log('função anônima de callback')
// }

// teste(fn)

//- ex.2 Função de fora, que utiliza como argumento outra função (a função de callback)

// const teste = function(cb) {
//     console.log('função teste')
//     cb()
// }

// const fn = function() {
//     console.log('função anônima de callback')
// }

// teste(fn)

//- ex.3 Fazendo com que a função de callback receba parâmetros; verificando se o argumetno é do tipo função (porque só pode ser executado se for função)

const teste = function(cb) {
    console.log('função teste')

    // VALIDAÇÃO DO ARGUMENTO (SE É FUNÇÃO) DA FORMA 1:
    // if (typeof cb ==="function") {
    //      cb(30)   
    // }
    // else {
    //     console.log('deveria ter passado função')
    // }
    // VALIDAÇÃO DO ARGUMENTO (SE É FUNÇÃO) DA FORMA 2 (CURTO CIRCUITO):
    typeof cb ==="function" && cb(30)   

}

const fn = function(parametro) {
    console.log('função anônima de callback', parametro)
}

// fn(30)

// teste(fn)
teste() // typeof de undefined NÃO é function, então não vai executar


