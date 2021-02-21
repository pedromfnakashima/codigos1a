/* 

*/

let str = 'hoje é 26/02/2018 e amanha será 27/02/18. Meu aniversario é 1/01';
const regex = /(\d{1,2})\//;
const regexGlobal = /(\d{1,2})\//g;

/* 
Search:
Retorna o índice da primeira ocorrência.
. É irrelevante a presença ou ausência da flag g (global).
. Se passar expressão regular que não existe, retorna -1.
*/
// console.log('str.search(regex) :>> ', str.search(regex));
// console.log('str.search(regexGlobal) :>> ', str.search(regexGlobal));

/* 
Match:
. Retorno muda dependendo se a expressão regular possui a flag g ou não.
.. Sem a flag g: com algumas informações adicionais a respeito da expressão regular.
.. Com a flag g: sem algumas informações adicionais a respeito da expressão regular.

*/

console.log('str.match(regex) :>> ', str.match(regex));
console.log('str.match(regexGlobal) :>> ', str.match(regexGlobal));
