


// function init() {
//     let isValid = false
//     console.log('init menu', isValid)
// }
// init()

//- Definindo função auto-invocável
// (function() {
//     let isValid = false
//     console.log('menu', isValid)

//     function init(){
//         console.log('init do menu')
//     }
//     init()

// })()

//- Passando parâmetros para função auto-invocável
//-- exemplo 1
// (function(n1,n2,n3) {
//     let isValid = false
//     console.log(`menu. n1:${n1},n2:${n2},n3:${n3}.`, isValid)

//     function init(){
//         console.log(`init do menu`)
//     }
//     init()

// })('a','b','c')


//-- exemplo 2 - passando como argumentos objetos window e document
(function(win, doc) {
    "use strict"
    let isValid = false

    win.alert('olá, mundo')
    doc.write('olá, mundo')

    console.log(`menu.`, isValid)

    function init(){
        console.log(`init do menu`)
    }
    init()

})(window, document)














