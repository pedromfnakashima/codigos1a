/* 
FUNÇÃO AUTO-INVOCÁVEL

;(function() {

})()

ARROW FUNCTION
https://www.samanthaming.com/tidbits/47-arrow-functions-cheatsheet/

(argumento) => valor retornado
(argumento) => {valor retornado}


    <!--função average()-->
    <script src="099js/calc.js"></script>
    <!-- código JS -->
    <script src="102gLinhasColunasDeDados.js"></script>

CONVERSÃO DE ARRAY PARA STRING
[1,2,3].toString() // "1,2,3"
[1,2,3].join() // "1,2,3"
[1,2,3].join('') // "123"

*/
// primeira versão


;(function() {
    const alunos = [
        { nome: "Daniel", notas: [10, 3, 7.5, 3] },
        { nome: "Maria", notas: [10, 9, 3, 9.5] },
        { nome: "João", notas: [10, 4.5, 1, 3.5] },
        { nome: "Joana", notas: [1, 3, 9, 1.5] },
        { nome: "José", notas: [10, 4.5, 7, 3] },
        { nome: "Arnaldo", notas: [10, 4.5, 7, 3] },
        { nome: "Lucas", notas: [4.5, 9, 8, 3] },
        { nome: "Luana", notas: [3, 7, 9, 3] },
        { nome: "Beatriz", notas: [10, 4, 7, 9] },
        { nome: "Sergio", notas: [4.5, 9.5, 10, 2] }
    ];
    // alunos.forEach( (aluno) => {console.log(aluno['nome'])} )
    alunos.forEach( (aluno) => {
        // aluno['média'] = average(aluno['n1'],aluno['n2'],aluno['n3'],aluno['n4'])
        //- Transformar o array em 'tupla'
        //-- Com o operador ...
        aluno['média'] = average(...aluno['notas'])
        //-- Com o método apply
        // aluno['média'] = average.apply(null, aluno['notas'])
    } )
    // alunos.forEach( (aluno) => {console.log(aluno['média'])} )
    // const html = alunos.map( (aluno) => ` - oi -` )
    // const html = alunos.map( (aluno) => `
    //     <tr>
    //         <td>${aluno['nome']}</td>
    //         <td>${aluno['notas'][0]}</td>
    //         <td>${aluno['notas'][1]}</td>
    //         <td>${aluno['notas'][2]}</td>
    //         <td>${aluno['notas'][3]}</td>
    //         <td>${aluno['média']}</td>
    //     </tr>
    //     ` ).join('') // conversão: ARRAY => STRING (sem separador)
    
    const html = alunos.map( (aluno) => `
    <tr class="${aluno['média']<5 ? "reprovado" : "aprovado"}">
        <td>${aluno['nome']}</td>
        ${aluno['notas'].map( (n) => `<td>${n}</td>` ).join('')}
        <td>${aluno['média']}</td>
    </tr>
    ` ).join('') // conversão: ARRAY => STRING (sem separador)
    
    document.querySelector('tbody').innerHTML = html

// console.log(html)

})()




























