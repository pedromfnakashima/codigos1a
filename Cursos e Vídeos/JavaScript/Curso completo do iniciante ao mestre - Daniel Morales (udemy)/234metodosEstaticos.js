/* 
234. métodos estáticos
São métodos que não fazem parte das instâncias da classe. Fazem parte da função construtora ou da classe.
É o caso de Math -> Math.random()

-- Para ser possível, de dentro do constructor, executar um método estático, é necessário chamar a classe pelo pelo nome da classe, ex.: Cachorro.beber(). Não é possível chamar um método estático, de dentro do constructor, através do this.
*/

// ES6

class Cachorro {
  constructor(nome) {
    //! Aqui, this é o próprio objeto, não a classe Cachorro; executado sempre que usar o operador new
    this.nome = nome;
    console.log('chamando método estático de dentro do constructor()');
    Cachorro.beber();
  }

  static comer() {
    //! ao colocar o static, faz com que comer não faça parte do objeto, mas sim da classe Cachorro
    console.log('this :>> ', this);
    console.log('comendo');
    this.beber(); //! this aqui é a classe Cachorro
  }

  static beber() {
    console.log('bebendo');
  }
}

const dog2 = new Cachorro('rex');
// console.log('dog2.comer() :>> ', dog2.comer()); //! com erro
console.log('Cachorro.comer() :>> ', Cachorro.comer()); //! sem erro
