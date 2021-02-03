/* 
233. classes abstratas

Uma classe abstrata é uma classe que não pode ser usada diretamente. Ela só pode ser estendida.

O constructor sempre é executado, mesmo que você não chame. Ele é chamado sempre que você utiliza o operador new.

Eu não quero que a função comer seja chamada de Animal. Eu quero que todo mundo que estenda a classe Animal seja obrigado a implementar o método comer.

*/

class Animal {
  constructor(tipo) {
    if (this.constructor === Animal) {
      // <= faz com que Animal só seja usada p/ estender outras classes
      throw new Error('Animal is an abstract class.');
    }

    if (tipo) {
      console.log('this.constructor :>> ', this.constructor);
      this.tipo = tipo;
    }
  }

  comer() {
    // console.log(`${this.tipo} está comendo.`);
    throw new Error('Method "comer()" must me implemented.');
  }
}

class Gato extends Animal {
  constructor(nome) {
    super('mamífero');
    this.nome = nome;
  }

  comer() {
    console.log(`${this.nome} está comendo.`);
  }
}

// const animal = new Animal('mamifero'); // Erro: Animal is an abstract class
const mingal = new Gato('mingal');

console.log('mingal.comer() :>> ', mingal.comer()); // ANTES (1): mamifero está comendo; ANTES (2) Method "comer()" must me implemented; DEPOIS: mingal está comendo.
