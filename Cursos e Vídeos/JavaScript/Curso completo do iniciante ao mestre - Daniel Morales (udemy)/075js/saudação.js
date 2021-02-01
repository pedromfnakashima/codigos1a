// Função auto-invocável p/ não poluir o escopo global
//- Colocar o nome do usuário
// (function(){
//     const nomeUsuário = 'Pedro'
//     //-- Forma 1:
//     // document.querySelector('.top-bar p').textContent = 'Bem-vindo(a), ' + nomeUsuário
//     //-- Forma 2:
//     const elemento = document.querySelector('.top-bar p')
//     // console.log(elemento.textContent)
//     // elemento.textContent = elemento.textContent + nomeUsuário
//     elemento.textContent += nomeUsuário
//     //! Obs.: a propriedade textContent NÃO renderiza tag html

// })()

//- Colocar o nome do usuário em negrito e itálico (inserir tags html) -> tem que usar o innerHTML ao invés do textContent
// (function(){
//     const nomeUsuário = 'Pedro'

//     const elemento = document.querySelector('.top-bar p')

//     elemento.innerHTML += '<b><i>' + nomeUsuário + '</i></b>'
//     //! Obs.: a propriedade innerHTML RENDERIZA tag html

// })()

// - Simular como se o usuário não estivesse logado - ESCONDENDO o elemento
//--> simplesmente ESCONDER ELEMENTO selecionado -- elemento.style permite escrever estilos CSS inline

// (function(){
//     // const nomeUsuário = 'Pedro'
//     const nomeUsuário = null
//     const elemento = document.querySelector('.top-bar p')

//     if (nomeUsuário) {
//         //--- Se existe o nomeUsuário, injeta html:
//         elemento.innerHTML += '<b><i>' + nomeUsuário + '</i></b>'

//     }

//     else {
//         //--- se não existe nomeUsuário, esconde a saudação:
//         elemento.style.display = 'none'

//     }

// })()

//-- esconder ELEMENTO-PAI (toda a barra, o class="top-bar") do elemento selecionado - usar elemento.parentElement ou elemento.parentNode: 
/* 
Para entender a navegação pelos elementos do DOM, digitar no console do Chrome:

const elemento = document.querySelector('.top-bar p')
elemento
elemento.parentNode
elemento.parentElement

*/


// (function(){
//     // const nomeUsuário = 'Pedro'
//     const nomeUsuário = null
//     const elemento = document.querySelector('.top-bar p')

//     if (nomeUsuário) {
//         //--- Se existe o nomeUsuário, injeta html:
//         elemento.innerHTML += '<b><i>' + nomeUsuário + '</i></b>'

//     }

//     else {
//         //--- se não existe nomeUsuário, esconde a saudação:
//         // elemento.style.display = 'none'
//         elemento.parentElement.style.display = 'none'

//     }

// })()

/* 
--Acessando ELEMENTO-FILHO de um elemento - usar elemento.children:
--- Exemplo 1:
Digitar no console do Chrome:
const elemento = document.querySelector('.top-bar p')
pai = elemento.parentElement
pai.children
pai.children[0]

--- Exemplo 2:
Digitar no console do Chrome:
document.querySelector('body').children
document.querySelector('body').children[0]

*/

// - Simular como se o usuário não estivesse logado - REMOVENDO o elemento - utilizar elemento.remove(), que não funciona no ie11, ou elementopai.removeChildren, que funciona no ie11


(function(){
    // const nomeUsuário = 'Pedro'
    const nomeUsuário = null
    const elemento = document.querySelector('.top-bar p')

    if (nomeUsuário) {
        //--- Se existe o nomeUsuário, injeta html:
        elemento.innerHTML += '<b><i>' + nomeUsuário + '</i></b>'

    }

    else {
        //--- se não existe nomeUsuário, esconde a saudação:
        // elemento.style.display = 'none'
        // elemento.parentElement.style.display = 'none'
        // elemento.remove() // obs.: não funciona no internet explorer (ie11)
        // obs.: Abaixo, funciona no ie11:
        const elementoASerRemovido = elemento.parentElement
        elementoASerRemovido.parentElement.removeChild(elementoASerRemovido)


    }

})()


// - Simular como se o usuário não estivesse logado - CRIANDO o elemento ===>>>> AULA 80









