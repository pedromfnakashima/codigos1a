/* 
250. Exercício
Crie um objeto produto.
Esse produto tem uma única propriedade chamada quantidade.
Proteja essa propriedade para que receba apenas números maiores que 0.
Toda vez que o valor de quantidade for consultdo, mostre no console um contador.
Evite variáveis no escopo global.
*/

/*  */
(function () {
  let _quantidade = 0;
  let _contador = 0;

  this.produto = {
    get quantidade() {
      console.log(
        `quantidade foi consultada ${++_contador} vez${
          _contador > 1 ? 'es' : ''
        }.`
      );
      return _quantidade;
    },
    set quantidade(valor) {
      if (valor > 0) {
        _quantidade = valor;
      }
    },
  };
})();

produto.quantidade = 20;
console.log('produto.quantidade :>> ', produto.quantidade);
produto.quantidade = 21;
console.log('produto.quantidade :>> ', produto.quantidade);
produto.quantidade = 22;
console.log('produto.quantidade :>> ', produto.quantidade);
