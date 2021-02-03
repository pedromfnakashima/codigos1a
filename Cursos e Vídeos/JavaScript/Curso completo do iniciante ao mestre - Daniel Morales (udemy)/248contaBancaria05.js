/* 
Desafio conta bancária

5. Polimorfismo
. Criar uma classe especializada em transferir.
Essa classe terá um único método execute(contaOrigem, contaDestino, valor).
Tanto contaOrigem quanto contaDestino precisam ser instâncias de ContaBancária.
Tanto CC quanto CP têm o método sacar(), que têm implementações diferentes.
Mas como sabemos que contaOrigem e contaDestino possuem o método sacar, independentemente se for CC ou CP podemos chamar esse método (polimorfismo).



*/

class Transferir {
  static execute(contaOrigem, contaDestino, valor) {
    if (
      !contaOrigem instanceof ContaBancaria ||
      !contaDestino instanceof ContaBancaria
    ) {
      throw new Error('contas precisam herdar de ContaBancária');
    }
    try {
      contaOrigem.sacar(valor);
      contaDestino.depositar(valor);
    } catch (e) {
      console.log('deu ruim', e.message);
    }
  }
}

class Cliente {
  // classe abstrata
  constructor(nome, documento, tipoDocumento) {
    if (this.constructor === Cliente) {
      throw new Error('Cliente é uma classe abstrata');
    }

    this.nome = nome;
    this.documento = documento;
    this.tipoDocumento = tipoDocumento;
  }
}

class PessoaFisica extends Cliente {
  constructor(nome, documento) {
    super(nome, documento, 'CPF');
  }
}

class PessoaJuridica extends Cliente {
  constructor(nome, documento) {
    super(nome, documento, 'CNPJ');
  }
}

const cliente1 = new PessoaFisica('pedro', '12.123.144-30');
const cliente2 = new PessoaFisica('pedro lanches', '122.133.144/0001-01');
console.log('cliente1 :>> ', cliente1);
console.log('cliente2 :>> ', cliente2);

class ContaBancaria {
  // classe abstrata
  constructor(cliente, numero) {
    // Impedir que alguém use a classe diretamente com o operador new (faz classe abstrata):
    if (this.constructor === ContaBancaria) {
      throw new Error('ContaBancaria é uma classe abstrata');
    }
    // Inicialização:
    this.cliente = cliente;
    this.numero = numero;
    this.saldo = 0;
  }

  get dadosCliente() {
    console.log('this.cliente.constructor :>> ', this.cliente.constructor);
    return `${this.cliente.nome}, ${this.cliente.tipoDocumento}: ${this.cliente.documento}`;
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

// const pedro = new Cliente('pedro', 1);
// const maria = new Cliente('maria', 2);
const pedro = new PessoaFisica('pedro', '12.133.144-10');
const maria = new PessoaJuridica('maria', '123.123.123/0001-01');

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

//
console.log('cc1.dadosCliente :>> ', cc1.dadosCliente);
console.log('cp1.dadosCliente :>> ', cp1.dadosCliente);
console.log('cp2.dadosCliente :>> ', cp2.dadosCliente);

//

console.log('cp1 :>> ', cp1); // saldo: 1000
console.log('cc1 :>> ', cc1); // saldo: 2000

Transferir.execute(cp1, cc1, 500);

console.log('cp1 :>> ', cp1); // saldo: 500
console.log('cc1 :>> ', cc1); // saldo: 2500

Transferir.execute(cp1, cc1, 600); // deu ruim Saldo insuficiente
