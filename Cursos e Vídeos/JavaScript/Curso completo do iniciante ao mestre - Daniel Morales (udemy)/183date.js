/* 
https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString
https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString

183. Introdução

*/

const data = new Date();
// console.log('data :>> ', data);
// console.log('data.getSeconds() :>> ', data.getSeconds());
// console.log('data.getDay() :>> ', data.getDay());
// console.log('data.getDate() :>> ', data.getDate());
// console.log('data.getMonth() :>> ', data.getMonth());
// console.log('data.getTime() :>> ', data.getTime());
// console.log('data.getFullYear() :>> ', data.getFullYear());
// console.log('data.getHours() :>> ', data.getHours());
// console.log('data.getUTCHours() :>> ', data.getUTCHours());
// console.log('Date.UTC(2021,1,28) :>> ', Date.UTC(2021, 1, 28));
// console.log('Date.now() :>> ', Date.now());
// console.log('data.getTimezoneOffset() :>> ', data.getTimezoneOffset());

// data.setDate(29);
// console.log('data :>> ', data);
// console.log('data.getSeconds() :>> ', data.getSeconds());
// console.log('data.getSeconds() :>> ', data.getSeconds());

// data.setTime(0); //timestamp inicial (1970, 0h)
// console.log('data :>> ', data);

/* 
184. toString()
*/

// console.log('data.toString() :>> ', data.toString());
// console.log('data.toDateString() :>> ', data.toDateString());
// console.log('data.toISOString() :>> ', data.toISOString());
// console.log('data.toLocaleDateString() :>> ', data.toLocaleDateString());
// console.log('data.toUTCString() :>> ', data.toUTCString());
// console.log('data.valueOf() :>> ', data.valueOf());
// console.log('data.toLocaleString("en-US") :>> ', data.toLocaleString('en-US'));
// console.log(
//   'data.toLocaleString("pt-BR", {month:"long", weekday: "long", day: "numeric"}) :>> ',
//   data.toLocaleString('pt-BR', {
//     month: 'long',
//     weekday: 'long',
//     day: 'numeric',
//   })
// );
// console.log(
//   'data.toLocaleString("pt-BR", {month:"long", weekday: "short", day: "numeric"}) :>> ',
//   data.toLocaleString('pt-BR', {
//     month: 'long',
//     weekday: 'short',
//     day: 'numeric',
//   })
// );
// console.log(
//   'data.toLocaleString("pt-BR", {month:"short", weekday: "short", day: "numeric"}) :>> ',
//   data.toLocaleString('pt-BR', {
//     month: 'short',
//     weekday: 'short',
//     day: 'numeric',
//   })
// );
// console.log(
//   'data.toLocaleString("pt-BR", {month:"short", weekday: "short", day: "numeric", year:"numeric"}) :>> ',
//   data.toLocaleString('pt-BR', {
//     month: 'short',
//     weekday: 'short',
//     day: 'numeric',
//     year: 'numeric',
//   })
// );
// console.log(
//   'data.toLocaleString("pt-BR", {month:"long", weekday: "long", day: "numeric", year:"numeric"}) :>> ',
//   data.toLocaleString('pt-BR', {
//     month: 'long',
//     weekday: 'long',
//     day: 'numeric',
//     year: 'numeric',
//   })
// );

// console.log(
//   'data.toLocaleString("pt-BR", {month:"long", weekday: "long", day: "numeric", year:"numeric", hour12:"false"}) :>> ',
//   data.toLocaleString('pt-BR', {
//     month: 'long',
//     weekday: 'long',
//     day: 'numeric',
//     year: 'numeric',
//     hour12: 'false',
//   })
// );
