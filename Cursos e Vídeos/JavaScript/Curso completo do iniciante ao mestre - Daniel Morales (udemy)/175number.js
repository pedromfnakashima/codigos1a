/* 
toPrecision, toFixed, toExponential()
*/

let numero = 1234567.89;

// console.log('numero.toFixed(2) :>> ', numero.toFixed(2));
// console.log('typeof numero.toFixed(2) :>> ', typeof numero.toFixed(2));
// console.log('numero.toFixed(5) :>> ', numero.toFixed(5));

// console.log('numero.toPrecision(7) :>> ', numero.toPrecision(7));
// console.log('typeof numero.toPrecision(7) :>> ', typeof numero.toPrecision(7));

// console.log('numero.toPrecision(15) :>> ', numero.toPrecision(15));
// console.log(
//   'typeof numero.toPrecision(15) :>> ',
//   typeof numero.toPrecision(15)
// );

// console.log('(123).toPrecision(6) :>> ', (123).toPrecision(6));

// numero = 12.34567;
// console.log('numero.toExponential() :>> ', numero.toExponential());
// console.log('numero.toExponential(4) :>> ', numero.toExponential(4));

// /*
// toString(), toLocaleString()
// O método toString pode ter comportamentos diferentes dependendo do tipo de objeto
// */

// numero = 15;
// console.log('numero.toString() :>> ', numero.toString());
// console.log('typeof numero.toString() :>> ', typeof numero.toString());

// // hexadecimal
// console.log('(15).toString(16)) :>> ', (15).toString(16));
// console.log('(16).toString(16)) :>> ', (16).toString(16));

// // toLocaleString - comportamento no devTools do firefox ou chrome
// numero = 123456.789;
// console.log('numero.toLocaleString() :>> ', numero.toLocaleString());
// console.log(
//   'numero.toLocaleString("pt-BR") :>> ',
//   numero.toLocaleString('pt-BR')
// );

// console.log(
//   'numero.toLocaleString("pt-BR", {style: "currency", currency:"BRL"} :>> ',
//   numero.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })
// );

// console.log(
//   'numero.toLocaleString("pt-PT", {style: "currency", currency:"EUR"} :>> ',
//   numero.toLocaleString('pt-PT', { style: 'currency', currency: 'EUR' })
// );

// console.log(
//   'numero.toLocaleString("en-US", {style: "currency", currency:"USD"} :>> ',
//   numero.toLocaleString('en-US', { style: 'currency', currency: 'USD' })
// );

/* 
MAX_VALUE, MIN_VALUE
parseFloat()
isFinite

*/

console.log('Number.MAX_VALUE :>> ', Number.MAX_VALUE);
console.log('Number.MIN_VALUE :>> ', Number.MIN_VALUE);

console.log('parseFloat("6.123") :>> ', parseFloat('6.123'));
console.log('Number.parseFloat("6.123") :>> ', Number.parseFloat('6.123'));

console.log('isFinite(2) :>> ', isFinite(2)); // true
console.log('isFinite("2") :>> ', isFinite('2')); // true

console.log('Number.isFinite(2) :>> ', Number.isFinite(2)); // true
console.log('Number.isFinite("2") :>> ', Number.isFinite('2')); // false porque não é número (não faz a conversão implícita)
