
//- Exemplo em que a função muda GLOBALMENTE o valor de uma variável definida externamente

// let n = 'global'

// function mostraN() {
//     n = 'local';
//     console.log(`valor de n: ${n}`);
// }

// mostraN();

// console.log(`valor de n: ${n}`);


//- Exemplo em que a função muda LOCALMENTE o valor de uma variável definida externamente


// let n = 'global'

// function mostraN() {
//     let n = 'local';
//     console.log(`valor de n: ${n}`);
// }

// mostraN();

// console.log(`valor de n: ${n}`);

//-- Conclusão 1: SEMPRE use o LET dentro da função quando for definir uma variável!!!

// function mostraN() {
//     let n1 = 'local';
// }

// mostraN();

// console.log(`valor de n: ${n1}`); // erro!!!

//-- Conclusão 2: Variáveis definidas dentro da função com o LET NÃO podem ser acessadas exteramente

// let n1 = 'global'

// function mostraN() {
//     let n1 = 'local';

//     if (true) {
//         let n1 = 'n1 dentro do if com let';
//         var n2 = 'n2 dentro do if com var';
//     }
//     console.log(`valor de n1 dentro da função, com let: ${n1}`);
//     console.log(`valor de n2 dentro da função, com var: ${n2}`);
// }

// mostraN();

// console.log(`valor de n1 fora da função: ${n1}`); // 

//-- Conclusão 3: Variáveis definidas dentro de um bloco IF (ou bloco de loop) com o LET NÃO sobrescrevem o valor da variável definida dentro da função; Variáveis definidas dentro do bloco com o LET NÃO podem ser acessadas exteramente do bloco, ainda que dentro da função.

//!! SEMPRE definir uma função com o let; quando quiser redefinir o valor, usar variável='novo_valor';

//--- Conclusão 4: essas conclusões NÃO se aplicam se a variável for definida com o VAR. Ou seja: NUNCA definir uma variável com o VAR.

//--- Conclusão 5:VAR gera escopo de FUNÇÃO, enquanto CONST e LET geram escopo de BLOCO.

// function fnExt() {

//     let n = 'n local na função fnExt';

//     function fnInt() {
//         let n = 'n local na função fnInt';
//         console.log(n);
//     }

//     fnInt();

//     console.log(n);

// }

// fnExt()

//!! SEMPRE definir uma função com o let; quando quiser redefinir o valor, usar variável='novo_valor';


function fnExt() {

    let n = 'n local na função fnExt';

    function fnInt() {
        n = 'n local na função fnInt';
        console.log(n);
    }

    fnInt();

    console.log(n);

}

fnExt()

//-- Conclusão 6: atribuindo um valor da forma variável = 'valor_variável' sempre tem a capacidade de mudar globalmente o valor daquela variável (NO ÂMBITO DE ONDE A VARIÁVEL FOI DEFINIDA)

