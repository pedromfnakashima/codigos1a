/* 
Aula 365
Datas em uma string:
Trocar o formato DD/MM/AAAA por sua forma extensa:
DD de MM de AAAA

Teste regex: https://regexr.com/

*/

let str = 'hoje é 26/02/2018 e amanha será 27/02/18. Meu aniversario é 1/01';
const meses = [
  'janeiro',
  'fevereiro',
  'março',
  'abril',
  'maio',
  'junho',
  'jullho',
  'agosto',
  'setembro',
  'outubro',
  'novembro',
  'dezembro',
];

const regex = /(\d{1,2})\/(\d{1,2})(?:\/(\d{2,4}))?/g; // agora precisa do g porque tem mais de uma ocorrência

str = str.replace(regex, function (a, dia, mês, ano, e, f) {
  return `${dia} de ${meses[parseInt(mês) - 1]} ${ano ? `de ${ano}` : ''}`;
});

console.log('str :>> ', str);
