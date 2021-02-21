/* 
Teste: https://regexr.com/

A partir da url:
https://www.google.com/search?user=pedro&id=1&q=regex

Quero um objeto da forma:
{
  user: 'pedro',
  id: 1,
  q: 'regex'
}


*/

/* Forma 1: */

// let url = 'https://www.google.com/search?user=pedro&id=1&q=regex';

/* Forma 2: */

let url = window.location.href + `search?user=pedro&id=1&q=regex`;

/* Forma 3 (não exemplificada):
let url = window.location.search;
Retorna os search parameters:
'?user=pedro&id=1&q=regex'

*/

let regex = /[&?](\w+)=(\w+)/g;

let arr;

const obj = {};

while ((arr = regex.exec(url))) {
  // console.log('arr :>> ', arr);
  obj[arr[1]] = arr[2];
}

console.log('obj :>> ', obj);
