"use strict"
 // o "use strict" tem que ficar exatamente na PRIMEIRA linha, e não pode vir acompanhado de comentário. Senão não funciona!
// x=10 // com o "use strict", dá erro no browser
// let x = 10

//- Conclusão 1: sempre usar o "use strict"; e sempre o colocar no começo do documento.

function foo() {
    // x = 20 //! se não usar declarar com let (ou com o const), essa variável passa para o escopo global!! O 'use strict' salva o programador, e avisa que tem erro.
    let x = 20 // jeito correto
}
foo()
// console.log(x)

//- Conclusão 2: sempre usar declarar uma variável, e sempre declarar com o let ou o const.











