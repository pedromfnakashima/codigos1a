/* 

Pouco suporte de browsers:
. replaceAll
. 












*/

/* .replace - substitui apenas a primeira ocorrência */

// let str1 = 'minha string bacanuda';
// console.log('str1.replace() :>> ', str1.replace('i', 'o'));
// console.log('str1 :>> ', str1);

/* regex - substitui todas as ocorrências - com expressão regular - mesmo efeito de replace all - é cross-Browser (ao contrário de replaceAll) */
// let str1 = 'minha string bacanuda';
// console.log('str1 replace i por o com regex :>> ', str1.replace(/i/g, 'o'));
// console.log('str1 :>> ', str1);

/* indexOf - retorna a primeira ocorrência*/
// let str1 = 'minha string bacanuda';
// console.log('str1.indexOf("string") :>> ', str1.indexOf('string'));

/* lastIndexOf - retorna a última ocorrência */
// let str1 = 'minha string bacanuda';
// // console.log('str1.lastIndexOf("i") :>> ', str1.lastIndexOf('i'));

// /* includes vs indexOf de string que não existe  */
// console.log(
//   'str1.lastIndexOf("não_existe") :>> ',
//   str1.lastIndexOf('não_existe')
// );
// console.log('str1.includes("não_existe") :>> ', str1.includes('não_existe'));
// console.log('str1.indexOf("não_existe") :>> ', str1.indexOf('não_existe'));
// console.log(
//   'str1.indexOf("não_existe") >= 0 :>> ',
//   str1.indexOf('não_existe') >= 0
// );

/* slice e substring.
Primeiro parâmetro: início (incluído);
Segundo parâmetro: final (excluído) - opcional (default: .length -1 <= vai até o final);
. valores negativos.
slice (melhor): permite que passe valores negativos;
substring: qualquer valor negativo passado, é entedido como zero.

.se passa valor inicial > valor final:
slice: não faz a inversão
substring: faz a inversão

*/
// let str1 = 'minha string bacanuda';
// console.log('str1.slice(2,7) :>> ', str1.slice(2, 7));
// console.log('str1.substring(2,7) :>> ', str1.substring(2, 7));
// console.log('str1.slice(2) :>> ', str1.slice(2));
// console.log('str1.substring(2) :>> ', str1.substring(2));
// console.log('str1.slice(-2) :>> ', str1.slice(-2));
// // console.log('str1.substring(-2) :>> ', str1.substring(-2)); //! <= comportamento não esperado
// console.log('str1.slice(-5, -1) :>> ', str1.slice(-5, -1));

/* toLowerCase e toUpperCase */
// let str1 = 'Minha String Bacanuda';
// console.log('str1.toUpperCase() :>> ', str1.toUpperCase());
// console.log('str1.toLowerCase() :>> ', str1.toLowerCase());
// console.log('str1 :>> ', str1);

/* valueOf - retorna o valor primitivo de um objeto do tipo string */
// let strAsObject = new String('minha string como objeto');
// console.log('strAsObject :>> ', strAsObject);
// console.log('strAsObject.valueOf() :>> ', strAsObject.valueOf());
// console.log('strAsObject.toString() :>> ', strAsObject.toString());

/* trim
remove espaços vazios e quebras de linhas, antes e depois
*/

// let str1 = '             abc              ';
// let str2 = `
//   teste
//   pula linha

//   fim da linha

//        oi

// `;
// console.log('-----------------------------------');
// console.log('str1 :>> ', str1);
// console.log('-----------------------------------');
// console.log('str1.trim() :>> ', str1.trim());
// console.log('-----------------------------------');
// console.log('str2 :>> ', str2);
// console.log('-----------------------------------');
// console.log('str2.trim() :>> ', str2.trim());
// console.log('-----------------------------------');

/* padStart e padEnd
Preenchimento da string
Preenche a string (com caracteres específicos ou espaço - padrão) p/ ter um length específico, passado como parâmetro
*/

// let str1 = '0123456789';
// console.log('str1.padStart(20) :>> ', str1.padStart(20));
// console.log('str1 :>> ', str1);
// console.log('str1.padStart(20,"*") :>> ', str1.padStart(20, '*'));
// console.log('str1.padEnd(20,"*") :>> ', str1.padEnd(20, '*'));

// Aplicação - mascarar telefone
// telefone1 = '91234-2345'; // '9****-**45'
// telefone2 = '1234-2345'; // '1***-**45'
// function mascararTelefone(numero) {
//   let hifenPosicao = numero.indexOf('-');
//   let numeroInicio = numero.slice(0, hifenPosicao);
//   let numeroFinal = numero.slice(hifenPosicao + 1);

//   let doisUltimosNumeros = numeroFinal.slice(-2);
//   return `${numeroInicio[0].padEnd(
//     numeroInicio.length,
//     '*'
//   )}-${doisUltimosNumeros.padStart(numeroFinal.length, '*')}`;
// }
// console.log('------telefone1--------');
// console.log(mascararTelefone(telefone1));
// console.log('------telefone2--------');
// console.log(mascararTelefone(telefone2));

/* startsWith e endsWith
retornam booleando; verifica se uma string começa com algo
Segundo parâmetro (opcional): que posição começar a procurar
*/
// let str2 = 'Hoje é Sábado';
// console.log('str2.startsWith("Hoje") :>> ', str2.startsWith('Hoje')); // true
// console.log('str2.startsWith("oje",1) :>> ', str2.startsWith('oje', 1)); // true
// console.log('str2.startsWith("je",1) :>> ', str2.startsWith('je', 2)); // true
// console.log('str2.endsWith("Sábado") :>> ', str2.endsWith('Sábado')); // true
// console.log('str2.endsWith("é","6") :>> ', str2.endsWith('é', '6')); // true
// console.log('str2.startsWith("Sábado") :>> ', str2.startsWith('Sábado')); // false (começou a procurar a partir da posição 1)
// console.log('str2.startsWith("Sábado",0) :>> ', str2.startsWith('Sábado', 0)); // false (começou a procurar a partir da posição 1)

/* charAt */
// let str3 = 'abcdefgh';
// console.log('str3.charAt(1) :>> ', str3.charAt(1));
// console.log('str3[1] :>> ', str3[1]);
// console.log('str3.charCodeAt(1) :>> ', str3.charCodeAt(1));
