/* 
212

call: Passar o contexto do this; não deixar o this mudar.

abaixo, estamos executando a função miar, mudando o contexto do this:
*/
// function miar() {
//   console.log(this.name, 'fala: miau');
// }

// const cat = {
//   name: 'mingal',
//   falar() {
//     console.log('this :>> ', this);
//     miar.call(this);
//   },
// };

// cat.falar();

/* 
213. apply vs call vs bind


*/

/* 
Ex. 1.
this = objeto global
*/

// function teste(str, n) {
//   console.log('this :>> ', this);
//   console.log('this.name :>> ', this.name); // undefined (não tem propriedade name no objeto global)
//   console.log('str, n :>> ', str, n);
// }
// teste('string', 10);

/* 
Ex. 2.
//- CALL
Mudar o escopo do this, para que não seja mais o objeto global.
Agora o this é o próprio objeto passado.
Passa os argumentos em seguida (do novo this).
*/

// function teste(str, n) {
//   console.log('this :>> ', this);
//   console.log('this.name :>> ', this.name); // undefined (não tem propriedade name no objeto global)
//   console.log('str, n :>> ', str, n);
// }
// teste.call({ name: 'Maria' });
// teste.call({ name: 'Maria' }, 'string1', 20);

/* 
//- APPLY
Passa array com os argumentos.
*/

function teste(str, n) {
  console.log('this :>> ', this);
  console.log('this.name :>> ', this.name); // undefined (não tem propriedade name no objeto global)
  console.log('str, n :>> ', str, n);
}
// teste.apply({ name: 'João' }, ['string2', 28]);

/* 
CALL
com o spread operator + array
*/
// teste.call({ name: 'Manoel' }, ...['string3', 32]);

/* 
- BIND

-- CALL e APPLY. no momento da execução da função, altera o this.
-- BIND. retorna duas funções: teste e teste2 (é o teste mudando o this)
Retorna uma nova função e armazena dentro de teste2

*/

const teste2 = teste.bind({ name: 'Joana' });
teste2('Joaquina', 30);
teste('Manuela', 40);

/* 
O bind é muito útil quando estivermos falando de botões, interface gráfica. Abaixo, testar no chrome:
Clicar no documento e ver o resultado no console.

*/
document.addEventListener('click', teste2);
