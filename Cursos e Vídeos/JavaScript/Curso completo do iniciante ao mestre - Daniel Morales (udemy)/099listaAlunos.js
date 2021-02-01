/* 


*/

//- V3 (aula 101) - Populando o objeto ÍNDICES_NOTAS de forma dinâmica
//! Sempre colocar um ; antes de uma função auto-invocável
;(function() {
    
    const trHeader = document.querySelector('thead tr')
    const thsHeader = trHeader.querySelectorAll('th')

    //-- Criar uma nodelist com as tags que tenham o atributo aluno-nota
    const thsAlunoNotas = trHeader.querySelectorAll('[aluno-nota]')
    // console.log(thsAlunoNotas)

    //-- Função que pega o índice
        function pegaÍndice(índice) {

        //-- Selecionar o índice cujo parâmetro aluno-nota é igual ao parâmetro passado
        const th = trHeader.querySelector(`[aluno-nota="${índice}"]`)

        //! Sintaxe antiga (mais cross-browser)
        // const i = Array.prototype.indexOf.call(thsHeader, th)
        //! Sintaxe mais moderna 1
        // const i = Array.from(thsHeader).indexOf(th)
        //! Sintaxe mais moderna 2
        const i = [...thsHeader].indexOf(th)

        return i

    }
    const ÍNDICES_NOTAS = {}
    //-- Transformando a nodelist thsAlunoNotas em array JS, e aplicando o forEach ao array criado. No forEach, será guardado o valor de cada atributo aluno-nota com a função getAttribute().
    Array.from(thsAlunoNotas).forEach(function(th) {
        // console.log(th.getAttribute('aluno-nota')) // n1, n2, n3, n4, média
        let prop = th.getAttribute('aluno-nota') // n1, n2, n3, n4, média
        ÍNDICES_NOTAS[prop] = pegaÍndice(prop)
    })

    
    //-- Retorna todas as linhas (tr) da tabela, com exceção do cabeçalho (por isso, usa-se o tbody):
    const trs = document.querySelectorAll('tbody tr')
    //-- Looping pelas linhas
    let ind_linha=0
    while (trs[ind_linha]) {
        // console.log(trs[x])
        //-- Retorna todas as células de uma dada linha:
        const tds = trs[ind_linha].querySelectorAll('td')
        // console.log(tds)
        //-- Qualquer informação que vem do html, vem como string. Por isso, para fazer conta, tem que converter para número:
        //--- Na primeira célula [0], está o nome do usuário. As notas começam a partir do índice [1].
        média = average(
            parseFloat(tds[ÍNDICES_NOTAS['n1']].textContent),
            parseFloat(tds[ÍNDICES_NOTAS['n2']].textContent),
            parseFloat(tds[ÍNDICES_NOTAS['n3']].textContent),
            parseFloat(tds[ÍNDICES_NOTAS['n4']].textContent)
        )
        //-- Injeta na célula [5] da tabela a média
        tds[ÍNDICES_NOTAS['média']].textContent = média.toFixed(2)
        ind_linha += 1
    }
})()











//- V2 (aula 100) - 

/* 
//! Sempre colocar um ; antes de uma função auto-invocável
;(function() {
    

    function pegaÍndice(índice) {
        const trHeader = document.querySelector('thead tr')
        const thsHeader = trHeader.querySelectorAll('th')
        //-- Selecionar o índice cujo parâmetro aluno-nota é igual ao parâmetro passado
        const th = trHeader.querySelector(`[aluno-nota="${índice}"]`)

        //! Sintaxe antiga (mais cross-browser)
        // const i = Array.prototype.indexOf.call(thsHeader, th)
        //! Sintaxe mais moderna 1
        // const i = Array.from(thsHeader).indexOf(th)
        //! Sintaxe mais moderna 2
        const i = [...thsHeader].indexOf(th)

        return i

    }

    const ÍNDICES_NOTAS = {
        n1: pegaÍndice('n1'),
        n2: pegaÍndice('n2'),
        n3: pegaÍndice('n3'),
        n4: pegaÍndice('n4'),
        média: pegaÍndice('média')
    }
    
    
    //-- Retorna todas as linhas (tr) da tabela, com exceção do cabeçalho (por isso, usa-se o tbody):
    const trs = document.querySelectorAll('tbody tr')
    //-- Looping pelas linhas
    let ind_linha=0
    while (trs[ind_linha]) {
        // console.log(trs[x])
        //-- Retorna todas as células de uma dada linha:
        const tds = trs[ind_linha].querySelectorAll('td')
        // console.log(tds)
        //-- Qualquer informação que vem do html, vem como string. Por isso, para fazer conta, tem que converter para número:
        //--- Na primeira célula [0], está o nome do usuário. As notas começam a partir do índice [1].
        média = average(
            parseFloat(tds[ÍNDICES_NOTAS['n1']].textContent),
            parseFloat(tds[ÍNDICES_NOTAS['n2']].textContent),
            parseFloat(tds[ÍNDICES_NOTAS['n3']].textContent),
            parseFloat(tds[ÍNDICES_NOTAS['n4']].textContent)
        )
        //-- Injeta na célula [5] da tabela a média
        tds[ÍNDICES_NOTAS['média']].textContent = média.toFixed(2)
        ind_linha += 1
    }
})()
 */

//- V1 - referenciando especificamente cada célula em uma determinada linha
/* 
(function() {
    //-- Retorna todas as linhas (tr) da tabela, com exceção do cabeçalho (por isso, usa-se o tbody):
    const trs = document.querySelectorAll('tbody tr')
    //-- Looping pelas linhas
    let ind_linha=0
    while (trs[ind_linha]) {
        // console.log(trs[x])
        //-- Retorna todas as células de uma dada linha:
        const tds = trs[ind_linha].querySelectorAll('td')
        // console.log(tds)
        //-- Qualquer informação que vem do html, vem como string. Por isso, para fazer conta, tem que converter para número:
        //--- Na primeira célula [0], está o nome do usuário. As notas começam a partir do índice [1].
        média = average(
            parseFloat(tds[1].textContent),
            parseFloat(tds[2].textContent),
            parseFloat(tds[3].textContent),
            parseFloat(tds[4].textContent)
        )
        //-- Injeta na célula [5] da tabela a média
        tds[5].textContent = média.toFixed(2)
        ind_linha += 1
    }
})()
 */



