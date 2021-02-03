/* 
Desafio conta bancária

3. Criar classe Cliente e compor as classes concretas
. nome
. documento

*/

class Cliente {
  constructor(nome, documento) {
    this.nome = nome;
    this.documento = documento;
  }
}

class ContaBancaria {
  constructor(cliente, numero) {
    // Impedir que alguém use a classe diretamente com o operador new:
    if (this.constructor === ContaBancaria) {
      throw new Error('ContaBancaria é uma classe abstrata');
    }
    // Inicialização:
    this.cliente = cliente;
    this.numero = numero;
    this.saldo = 0;
  }

  depositar(valor) {
    this.saldo += valor;
  }

  sacar() {
    throw new Error('método sacar() precisa ser implementado');
  }
}

class ContaPoupanca extends ContaBancaria {
  constructor(cliente, numero) {
    super(cliente, numero);
    this.aniversario = Date.now();
  }

  sacar(valor) {
    if (valor > this.saldo) {
      throw new Error('Saldo insuficiente.');
    }
    this.saldo -= valor;
  }
}

class ContaCorrente extends ContaBancaria {
  constructor(cliente, numero) {
    super(cliente, numero);
    this.limite = 0;
  }

  sacar(valor) {
    let disponivel = this.saldo + this.limite;
    if (valor > disponivel) {
      throw new Error('Saldo insuficiente.');
    }
    this.saldo -= valor;
  }
}

const pedro = new Cliente('pedro', 1);
const maria = new Cliente('maria', 2);

const cp1 = new ContaPoupanca(pedro, 1);
const cp2 = new ContaPoupanca(maria, 2);
const cc1 = new ContaCorrente(maria, 3);

//
console.log('cp1 :>> ', cp1);
cp1.depositar(1000);
console.log('cp1 :>> ', cp1);
//
cc1.limite = 1000;
cc1.depositar(2000);
console.log('cc1 :>> ', cc1);
//
// cc1.sacar(3001); // erro: saldo insuficente
console.log('cc1 :>> ', cc1);
//
// cp1.sacar(1001); // erro: saldo insuficente
console.log('cp1 :>> ', cp1);
console.log('cp2 :>> ', cp2);
