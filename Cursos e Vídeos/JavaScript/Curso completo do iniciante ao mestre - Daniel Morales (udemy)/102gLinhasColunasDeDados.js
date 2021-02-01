/* 
FUNÇÃO AUTO-INVOCÁVEL

;(function() {

})()

ARROW FUNCTION

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
        { nome: "Daniel", n1: 10, n2: 3, n3: 7.5, n4: 3 },
        { nome: "Maria", n1: 10, n2: 9, n3: 3, n4: 9.5 },
        { nome: "João", n1: 10, n2: 4.5, n3: 1, n4: 3.5 },
        { nome: "Joana", n1: 1, n2: 3, n3: 9, n4: 1.5 },
        { nome: "José", n1: 10, n2: 4.5, n3: 7, n4: 3 },
        { nome: "Arnaldo", n1: 10, n2: 4.5, n3: 7, n4: 3 },
        { nome: "Lucas", n1: 4.5, n2: 9, n3: 8, n4: 3 },
        { nome: "Luana", n1: 3, n2: 7, n3: 9, n4: 3 },
        { nome: "Beatriz", n1: 10, n2: 4, n3: 7, n4: 9 },
        { nome: "Sergio", n1: 4.5, n2: 9.5, n3: 10, n4: 2 }
    ];

    // alunos.forEach( (aluno) => {console.log(aluno['nome'])} )
    alunos.forEach( (aluno) => {
        aluno['média'] = average(aluno['n1'],aluno['n2'],aluno['n3'],aluno['n4'])
    } )
    // alunos.forEach( (aluno) => {console.log(aluno['média'])} )
    // const html = alunos.map( (aluno) => ` - oi -` )
    const html = alunos.map( (aluno) => `
        <tr>
            <td>${aluno['nome']}</td>
            <td>${aluno['n1']}</td>
            <td>${aluno['n2']}</td>
            <td>${aluno['n3']}</td>
            <td>${aluno['n4']}</td>
            <td>${aluno['média']}</td>
        </tr>
        ` ).join('') // conversão: ARRAY => STRING (sem separador)
    document.querySelector('tbody').innerHTML = html

// console.log(html)

})()




























