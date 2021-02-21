/* 
O método exec normalmente não é utilizado.
*/

let str = 'hoje é 26/02/2018 e amanha será 27/02/18. Meu aniversario é 1/01';
const regex = /(\d{1,2})\//;
const regexG = /(\d{1,2})\//g;

/* 
Exec
. Busca numa string, pela expressão regular, e retorna algumas informações referentes ao resultado da busca.
. Retorna um array-like.
. Resultado diferente se tem a flag g (global) ou não
.. se não tem g, retorna sempre o mesmo resultado.
.. se tem g, retorna o próximo resultado encontrado; ou seja, retorna um resultado diferente a cada chamada.

Parte 1
*/

// console.log('regex.exec(str) :>> ', regex.exec(str));
// console.log('regex.exec(str) :>> ', regex.exec(str)); // Mesmo resultado
// console.log('regexG.exec(str) :>> ', regexG.exec(str));
// console.log('regexG.exec(str) :>> ', regexG.exec(str)); // Resultado diferente pois é a segunda chamada (retorna a próxima ocorrência)
// console.log(
//   'regexG.lastIndex :>> ',
//   regexG.lastIndex
// ); /* propriedade que é armazenada dentro da própria regex para que, na próxima execução do exec, ele começa a procurar a partir do referido índice*/

/* Parte 2 */
let arr = regexG.exec(str);

while (arr) {
  console.log(
    `Encontrei ${arr[0]} na posição ${arr.index}. Próxima busca começa em ${regexG.lastIndex}`
  );
  arr = regexG.exec(str);
}
console.log('Terminou o loop');
