/* 
module.exports é o {} exportado

O que sempre é exportado é o que está pendurado em module.exports; nunca o que está dentro só de exports.

*/
// module.exports.teste = 'olá, mundo!!!';

// console.log('module.exports :>> ', module.exports); // {}

console.log('exports :>> ', exports);
console.log('module.exports === exports :>> ', module.exports === exports); // true

exports = { prop: 'não será exportado' };
// module.exports = { teste2: 'olá mundo' };
module.exports = () => {
  console.log('função em module.exports');
  return 'função retornada por module.exports';
};
console.log('module.exports :>> ', module.exports); // { teste2: 'olá mundo' }

console.log('exports :>> ', exports);
console.log('module.exports === exports :>> ', module.exports === exports); // false
