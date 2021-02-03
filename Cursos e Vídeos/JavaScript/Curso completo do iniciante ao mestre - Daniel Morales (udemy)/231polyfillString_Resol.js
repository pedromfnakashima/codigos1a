/* 

231

https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll
https://caniuse.com/?search=replaceAll

Replicar o replaceAll caso ele não seja suportado pelo browser.

*/

if (!String.prototype.replaceAll) {
  String.prototype.replaceAll = function (busca, troca) {
    // console.log('this :>> ', this);
    // console.log('this.valueOf() :>> ', this.valueOf());

    if (!(busca instanceof String || typeof busca === 'string')) {
      throw Error('first parameter must be a string');
    }

    if (!(troca instanceof String || typeof troca === 'string')) {
      throw Error('second parameter must be a string');
    }

    return this.valueOf().split(busca).join(troca);
  };
}
