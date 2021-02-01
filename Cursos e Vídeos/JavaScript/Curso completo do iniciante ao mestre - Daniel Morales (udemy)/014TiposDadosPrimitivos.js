
// De aula 14 a aula __

//- AULA 015 - concatenação, verificação do tipo da variável

let minhaVar = "minha string";
let minhaVar2 = 'minha \'string\' com aspas simples';
let minhaVar3 = `minha template literal`; /* como se fosse a fstring do python */

// let idade = 36;
// let msg = 'eu possuo 40 anos';
// let msg = 'eu possuo ' + idade + ' anos';
// let msg = `eu possuo ${idade} anos`;

// console.log(msg);

// VERIFICAR O TIPO DA VARIÁVEL

// console.log(typeof msg, typeof idade, typeof minhaVar);

tipoVar = typeof msg;

// console.log(`O tipo da variável msg é ${tipoVar}`);

// const n1 = 10
// const n2 = 1.1

// console.log(`O tipo da variável n1 é ${typeof n1}`);
// console.log(`O tipo da variável n2 é ${typeof n2}`);

//- AULA 016 - boolean

const vbol1 = true;
// console.log(`o valor de vobol1 é ${vbol1}`);

// AULA 017 -- undefined, null
let varTeste;
// console.log(varTeste); // undefined
// console.log(typeof varTeste); // undefined

let varTeste2 = undefined;
// console.log(varTeste2); // undefined
// console.log(typeof varTeste2); // undefined

let varTeste3 = null;
// console.log(varTeste3); // null
// console.log(typeof varTeste3); // object

//- AULA 018 -- converter de string para número

// const n1 = 10;
// const n2 = '2';
// console.log(typeof n1, typeof n2); // number, string

/* IMPORTANTE: TODA informação que vem da interface gráfica com o usuário vem como STRING. Por isso, se você quer fazer operações aritméticas, você deve converter para número.
Formas de conversão:
parseFloat:  descarta uma letra que estiver depois na string (se estiver antes, dá NaN);
parseInt: descarta uma letra que estiver depois na string (se estiver antes, dá NaN);
Number: se a string tiver letra, sempre converte para NaN.
*/


// let n3 = parseInt(n2);
// let n4 = parseFloat(n2);
// let n5 = Number(n2);

// console.log(`n1 * n2 = ${n1 * n2}`); // 20 converte n2 pra número por baixo dos panos e faz a multiplicação
// console.log(`n1 / n2 = ${n1 / n2}`); // 5 converte n2 pra número por baixo dos panos e faz a divisão
// console.log(`n1 + n2 = ${n1 + n2}`); // 102 ERRONEAMENTE, transforma n1 para string e CONCATENA
// console.log(`n1 + n3 (parseInt) = ${n1 + n3}`); // 12 CORRETAMENTE, soma
// console.log(`n1 + n4 (parsFloat) = ${n1 + n4}`); // 12 CORRETAMENTE, soma
// console.log(`n1 + n5 (Number) = ${n1 + n5}`); // 12 CORRETAMENTE, soma


// const n1 = 10;
// const n2 = '2a';

// let n3 = parseInt(n2);
// let n4 = parseFloat(n2);
// let n5 = Number(n2);

// let n3 = parseInt(n2);
// let n4 = parseFloat(n2);
// let n5 = Number(n2);

// console.log(`n1 * n2 = ${n1 * n2}`); // 20 converte n2 pra número por baixo dos panos e faz a multiplicação
// console.log(`n1 / n2 = ${n1 / n2}`); // 5 converte n2 pra número por baixo dos panos e faz a divisão
// console.log(`n1 + n2 = ${n1 + n2}`); // 102 ERRONEAMENTE, transforma n1 para string e CONCATENA
// console.log(`n1 + n3 (parseInt) = ${n1 + n3}`); // 12 CORRETAMENTE, soma
// console.log(`n1 + n4 (parsFloat) = ${n1 + n4}`); // 12 CORRETAMENTE, soma
// console.log(`n1 + n5 (Number) = ${n1 + n5}`); // 12 CORRETAMENTE, soma

//- AULA 019 -- converter de número para string

// let n1 = 'oi';
// let n2 = 10;

// Forma 1: concatenar com string vazia
// n2 = n2 + ''
// console.log(n2, typeof n2);

// Forma 2: .toString()
// n2 = n2.toString(n2)
// console.log(n2, typeof n2);

//- AULA 020 -- operadores aritméticos

// let n1 = 10;
// let n2 = 2;

// console.log(n1 + n2);
// console.log(n1 - n2);
// console.log(n1 * n2);
// console.log(n1 / n2);
// console.log(n1 % n2); // resto da divisão
// console.log(2 ** 3); // potência


//- AULA 021 -- operadores de atribuição

// let n3 = 20;

// n3 = n3 + 15;
// n3 += 15;
// n3 -= 2;
// n3 *= 2;
// n3 /= 11;
// n3 %= 2;
// n3 **= 0;
// console.log(n3);

//- AULA 022 -- incremento e decremento

let i = 0
// São equivalentes:
// i = i + 1
// i += 1
// i++

// São equivalentes:
// i = i - 1
// i -= 1
// i--

// console.log(i++); // 0
// console.log(i); // 1

// console.log(++i); // 1
// console.log(i); // 1


//- AULA 023 -- operadores de comparação
/* 
igualdade de valor ==
igualdade de valor e tipo ===
<, >, <=, >=
!= valores diferentes
!== valores e tipos diferentes
 */
// let n1 = 10;
// let n2 = '10';
// console.log(`n1 == n2: ${n1 == n2}`); // true
// console.log(`n1 === n2: ${n1 === n2}`); // false
// console.log(`n1 != n2: ${n1 != n2}`); // true
// console.log(`n1 !== n2: ${n1 !== n2}`); // false

// console.log(`n1 < 10: ${n1 < 10}`); // false
// console.log(`n1 > 10: ${n1 > 10}`); // false
// console.log(`n1 >= 10: ${n1 >= 10}`); // true

//- AULA 024 -- operadores lógicos - parte 1

/* 
AND: &&
OR: ||
NOT: !

 */

//- AULA 025 -- operadores lógicos - parte 2
//- AULA 026 -- precedência de operadores

// let idade = 17;
// let paisPresentes = true;
// let comprouBilhete = false;
// // const podeViajar = idade>18 || paisPresentes == true;
// const podeViajar = (idade>=18 || paisPresentes) && comprouBilhete;

// console.log(`Pode viajar? ${podeViajar}`);


//- AULA 027 -- condicional if else

// let idade = 17;
// let paisPresentes = true;
// let comprouBilhete = true;

// if ( (idade>=18 || paisPresentes) && comprouBilhete ) {
//     console.log(`Pode viajar`);
// }
// else {
//     console.log(`Não pode viajar`);
// }


// if (! comprouBilhete ) {
//     console.log(`Não comprou o bilhete`);
// }
// else {
//     if ( idade>=18 ) {
//         console.log(`É maior de idade`);
//     }
//     else {
//         console.log(`Comprou o bilhete, mas precisa estar acompanhado dos pais`);
//     }
// }

// let n1 = 0;
// let n2 = 7;
// média = (n1 + n2) /2;

// if (n1==0 || n2==0) {
//     console.log(`Reprovado`);
// }
// else if (média < 7) {
//     console.log(`Recuperação`);
// }
// else {
//     console.log(`Aprovado`);
// }


//- AULA 028 -- operador ternário

let idade = 20;
let paisPresentes = true;
let comprouBilhete = true;

// let msgMaiorIdade = '';
// if (idade >= 18) {
//     msgMaiorIdade = 'É maior de idade';
// }
// else {
//     msgMaiorIdade = 'É menor de idade';
// }

// OPERADOR TERNÁRIO

// let msgMaiorIdade = (idade >= 18) ? 'maior de idade': 'menor de idade';
// console.log(msgMaiorIdade);

//- AULA 029 -- valores falsy e truthy

// if (true) {
//     console.log(`true`);
// }
// else {
//     console.log(`false`);
// }

/* 
FALSY:
0, '', NaN, undefined, null, false
TRUTHY:
todos os demais
 */
// if (10) {
//     console.log(`true`);
// }
// else {
//     console.log(`false`);
// }

// if ('false') {
//     console.log(`true`);
// }
// else {
//     console.log(`false`);
// }

// if (null) {
//     console.log(`true`);
// }
// else {
//     console.log(`false`);
// }

// if (0) {
//     console.log(`true`);
// }
// else {
//     console.log(`false`);
// }

// if ('oi' * 2) { // NaN
//     console.log(`true`);
// }
// else {
//     console.log(`false`);
// }

// if (undefined) { // NaN
//     console.log(`true`);
// }
// else {
//     console.log(`false`);
// }

// let n
// if (n) {
//     console.log(`true`);
// }
// else {
//     console.log(`false`);
// }

//- AULA 030 -- curto-circuito
/* 
Muito usado para colocar valor padrão em argumentos de funções
 */

// let n = 0;
// if (n === 0) {
//     n = 10
// }
// console.log(n); // 10

// let n = 0;
// if (!n) {
//     n = 10
// }
// console.log(n); // 10

// let n = 0;
// n = n || 10;
// console.log(n); // 10

// let n = 1;
// n = n || 10;
// console.log(n); // 1

// let = isValid = true;
// // if (isValid) {
// //     console.log('é válido'); // é válido
// // }

// isValid && console.log('é válido'); // é válido

// let = isValid = false;
// isValid && console.log('é válido'); //

// let = isValid = false;
// isValid || console.log('é válido'); // é válido

// correção na aula seguinte (31)

// let = isValid = true;
// isValid && console.log('é válido'); // 
// isValid || console.log('não é válido'); // 

// let = isValid = false;
// isValid && console.log('é válido'); // 
// isValid || console.log('não é válido'); // 

// console.log(0 && 'ola'); // 0
// console.log(0 || 'ola'); // ola
// console.log('ola' || 'mundo'); // ola
// console.log('ola' && 'mundo'); // mundo

// let n = true || 'ola'
// console.log(n) // true

// let n = true && 'ola'
// console.log(n) // ola

// let n = NaN && 'ola'
// console.log(n) // NaN

// let n = NaN || 'ola'
// console.log(n) // ola

//- AULA 031 -- conditional switch

// COM O IF E ELSE


// // let diaSemana = 6; // numérico
// let diaSemana = '6'; // string --> vai para o bloco else
// if (diaSemana === 0) {
//     console.log('hoje é domingo');
// }
// else if (diaSemana === 1) {
//     console.log('hoje é segunda');
// }
// else if (diaSemana === 2) {
//     console.log('hoje é terça');
// }
// else if (diaSemana === 3) {
//     console.log('hoje é quarta');
// }
// else if (diaSemana === 4) {
//     console.log('hoje é quinta');
// }
// else if (diaSemana === 5) {
//     console.log('hoje é sexta');
// }
// else if (diaSemana === 6) {
//     console.log('hoje é sábado');
// }
// else {
//     console.log('--');
// }


// COM O SWITCH


// // let diaSemana = 6; // numérico
// let diaSemana = '6'; // string -> vai para o default (ou seja, compara VALOR e TIPO)

// let dia = ''
// switch ( diaSemana ) {
//     case 0:
//         dia = 'domingo'
//         break;
//     case 1:
//         dia = 'segunda'
//         break;
//     case 2:
//         dia = 'terça'
//         break;
//     case 3:
//         dia = 'quarta'
//         break;
//     case 4:
//         dia = 'quinta'
//         break;
//     case 5:
//         dia = 'sexta'
//         break;
//     case 6:
//         dia = 'sábado'
//         break;
//     default:
//         dia = ' -- '
// }

// console.log(`Hoje é ${dia}`);

//- AULA 032 -- repetições repetição loop looping (no arquivo 032repetições.html)

//- AULA 033 -- break vs continue (no arquivo 033breakContinue.html)

// Tabuada:
//- AULA 034 -- funções (no arquivo 034funcoes.html)

// Pedro (eu fiz, fazendo paralelo com o Python)
f1 = function(a,b) {
    c = a + b
    return c
}
valor = f1(2,3)
console.log(valor)






















