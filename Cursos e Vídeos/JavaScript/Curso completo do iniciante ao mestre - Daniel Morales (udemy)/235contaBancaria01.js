/* 
Desafio conta bancária

1. Criar conta abstrata ContaBancária
. cliente
. numero
. saldo
. depositar(valor)
. sacar(valor)

*/

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

const conta = new ContaBancaria('pedro', 1);
