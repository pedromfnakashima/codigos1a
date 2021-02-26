/* 
Interfaces vs. classes abstratas

Os dois cumprem o mesmo objetivo de forma diferente.


*/

export abstract class Animal {
  constructor(protected readonly categoria: string) {}

  mostrarCategoria(): void {
    console.log('this.categoria :>> ', this.categoria);
  }

  abstract mostrarDetalhes(): void;
  abstract idade: number;
}

interface AnimalInterface {
  categoria: string;
  mostrarDetalhes(): void;
  idade?: number;
}

const laica: AnimalInterface = {
  categoria: 'mamífero',
  mostrarDetalhes() {
    console.log('qualquer coisa');
  },
};

console.log('laica :>> ', laica);

class Gato extends Animal {
  constructor(public nome: string, public idade: number) {
    super('mamifero');
  }

  mostrarDetalhes() {
    console.log('mostrar detalhe chamado');
  }
}

interface CachorroInterface {
  latir(): void;
}

class Cachorro implements AnimalInterface, CachorroInterface {
  constructor(
    public categoria: string,
    public readonly nome: string,
    public idade?: number
  ) {}

  mostrarDetalhes() {
    console.log('mostrarDetalhes de Cachorro');
    console.log('this.nome :>> ', this.nome);
    console.log('this.categoria :>> ', this.categoria);
    console.log(this.idade ? this.idade + 1 : '');
  }

  latir() {
    console.log(this.nome, 'está latindo');
  }
}

console.log('---------- Instância de gato -----------');
const mingal = new Gato('mingal', 5);
console.log('mingal :>> ', mingal);

console.log('---------- Instância de cachorro -----------');
const toto = new Cachorro('mamifero', 'toto');
console.log('toto :>> ', toto);

toto.latir();

interface Pessoa {
  name: string;
}

interface Pessoa {
  idade: number;
}

const pedro: Pessoa = {
  name: 'Pedro',
  idade: 36,
};
console.log('pedro :>> ', pedro);

// type TesteT = number
type TesteT = number | { qtd: number };
// const idade: TesteT = 10
const idade: TesteT = { qtd: 1 };
