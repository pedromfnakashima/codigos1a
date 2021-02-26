console.log('_________________________');

/* Versão mais longa */
// class Animal {
//   categoria: string;
//   constructor(categoria: string) {
//     this.categoria = categoria;
//   }
// }

/* Versão mais curta
--public: permite ler e editar a propr fora do objeto
*/
// class Animal {
//   constructor(public categoria: string) {}
// }

// const animal = new Animal('mamifero');
// console.log('animal :>> ', animal);
// console.log('animal.categoria :>> ', animal.categoria);
// animal.categoria = 'categoria editada fora da classe';
// console.log('animal :>> ', animal);

/* Versão mais curta
--readonly: não pode escrever a propriedade fora do objeto
*/
// class Animal {
//   constructor(readonly categoria: string) {}
// }

// const animal = new Animal('mamifero');
// console.log('animal :>> ', animal);
// console.log('animal.categoria :>> ', animal.categoria);
// // animal.categoria = 'categoria editada fora da classe'; //! erro
// console.log('animal :>> ', animal);

/* Versão mais curta
--private: não pode nem escrever, nem ler a propriedade fora do objeto
*/
// class Animal {
//   constructor(private categoria: string) {}
// }

// const animal = new Animal('mamifero');
// console.log('animal :>> ', animal);
// // console.log('animal.categoria :>> ', animal.categoria); //! erro
// // animal.categoria = 'categoria editada fora da classe'; //! erro
// console.log('animal :>> ', animal);

/* Versão mais curta
--protected: não pode nem escrever, nem ler a propriedade fora do objeto.
Porém, difere-se da private na questão de heranças.
*/
// class Animal {
//   constructor(protected categoria: string) {}
// }

// const animal = new Animal('mamifero');
// console.log('animal :>> ', animal);
// // console.log('animal.categoria :>> ', animal.categoria); //! erro
// // animal.categoria = 'categoria editada fora da classe'; //! erro
// console.log('animal :>> ', animal);

/* 
--- getter com private
*/

// class Animal {
//   constructor(private categoria: string) {}

//   mostrarCategoria(): void {
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// const animal = new Animal('mamifero');
// console.log('animal :>> ', animal);
// animal.mostrarCategoria();

/* 
Aula 407
criaremos a classe Gato com a sintaxe mais longa
- extends
*/

/*
--ex.1: private não permite acessar this.categoria fora da classe que gerou o objeto, mesmo que seja de uma classe que estende
*/

// class Animal {
//   constructor(private categoria: string) {}

//   mostrarCategoria(): void {
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Gato extends Animal {
//   // nome: string;
//   // public nome: string; // padrão = public, por isso é equivalente à linha anterior
//   // readonly nome: string; //
//   private nome: string; //

//   constructor(nome: string) {
//     super('mamifero');
//     this.nome = nome;
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//     console.log('this.categoria :>> ', this.categoria); // gera erro
//   }
// }

// const mingal = new Gato('mingal');
// console.log('mingal :>> ', mingal);
// // console.log('mingal.nome :>> ', mingal.nome);
// // mingal.nome = 'nome alterado';

/*
--ex.3: protected protege o categoria de fora da classe, mas não promete das classes-filhas (estendidas)
*/

// class Animal {
//   constructor(protected categoria: string) {}

//   mostrarCategoria(): void {
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Gato extends Animal {
//   // nome: string;
//   // public nome: string; // padrão = public, por isso é equivalente à linha anterior
//   // readonly nome: string; //
//   private nome: string; //

//   constructor(nome: string) {
//     super('mamifero');
//     this.nome = nome;
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//     console.log('this.categoria :>> ', this.categoria); // não gera erro
//   }
// }

// const mingal = new Gato('mingal');
// console.log('mingal :>> ', mingal);

// // console.log('mingal.nome :>> ', mingal.nome);
// // mingal.nome = 'nome alterado';

/*
--ex.4: no código abaixo, é possível editar categoria a partir de uma instância da classe filha (Gato)
*/

// class Animal {
//   constructor(protected categoria: string) {}

//   mostrarCategoria(): void {
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Gato extends Animal {
//   private nome: string; //

//   constructor(nome: string) {
//     super('mamifero');
//     this.nome = nome;
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//     console.log('this.categoria :>> ', this.categoria); // não gera erro
//     this.categoria = 'categoria editada de dentro de uma classe filha';
//     console.log('this.categoria :>> ', this.categoria); // não gera erro
//   }
// }

// const mingal = new Gato('mingal');
// console.log('mingal :>> ', mingal);

// mingal.mostrarDetalhes();

/*
--ex.4: no código abaixo, NÃO é possível editar categoria a partir de uma instância da classe filha (Gato). Basta adicionar o readonly depois do protected.
Fazendo isso, nem de dentro da instância da classe mãe é possível mudar categoria; só é possível definir a categoria no construtor.
*/

// class Animal {
//   constructor(protected readonly categoria: string) {}

//   mostrarCategoria(): void {
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Gato extends Animal {
//   private nome: string; //

//   constructor(nome: string) {
//     super('mamifero');
//     this.nome = nome;
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//     console.log('this.categoria :>> ', this.categoria); // não gera erro
//     // this.categoria = 'categoria editada de dentro de uma classe filha'; //! gera erro
//     console.log('this.categoria :>> ', this.categoria); // não gera erro
//   }
// }

// const mingal = new Gato('mingal');
// console.log('mingal :>> ', mingal);

// mingal.mostrarDetalhes();

/* 
-408 classes abstratas

Abaixo, criamos uma classe nova, Cachorro.
Fazemos isso utilizando a versão enxuta.

*/

// class Animal {
//   constructor(protected readonly categoria: string) {}

//   mostrarCategoria(): void {
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Gato extends Animal {
//   private nome: string; //

//   constructor(nome: string) {
//     super('mamifero');
//     this.nome = nome;
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Cachorro extends Animal {
//   constructor(protected readonly nome: string) {
//     super('mamifero');
//   }

//   mostrarDetalhe(): void {
//     console.log('this.nome :>> ', this.nome);
//   }
// }

// console.log('----------- Instância de Animal -----------');

// const animal = new Animal('mamifero');
// console.log('animal :>> ', animal);

// console.log('----------- Instância de Gato -----------');

// const mingal = new Gato('mingal');
// console.log('mingal :>> ', mingal);

// mingal.mostrarDetalhes();

// console.log('----------- Instância de Cachorro -----------');
// const toto = new Cachorro('toto');
// toto.mostrarDetalhe();

/* 
--Classe abstrata = classe que só pode ser usada para estender outras classes, mas nunca para instanciar. Basta colocar na frente da palavra class a palavra abstract
*/

// abstract class Animal {
//   constructor(protected readonly categoria: string) {}

//   mostrarCategoria(): void {
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Gato extends Animal {
//   private nome: string; //

//   constructor(nome: string) {
//     super('mamifero');
//     this.nome = nome;
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Cachorro extends Animal {
//   constructor(protected readonly nome: string) {
//     super('mamifero');
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//   }
// }

// console.log('----------- Instância de Animal -----------');

// // const animal = new Animal('mamifero'); //! erro
// // console.log('animal :>> ', animal); //! erro

// console.log('----------- Instância de Gato -----------');

// const mingal = new Gato('mingal');
// console.log('mingal :>> ', mingal);

// mingal.mostrarDetalhes();

// console.log('----------- Instância de Cachorro -----------');
// const toto = new Cachorro('toto');
// toto.mostrarDetalhes();

/* 
- 409. getters e setters
*/

/* 
-- sem getter e setter
*/

// abstract class Animal {
//   constructor(protected readonly categoria: string) {}

//   mostrarCategoria(): void {
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Gato extends Animal {
//   private nome: string; //

//   constructor(nome: string) {
//     super('mamifero');
//     this.nome = nome;
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Cachorro extends Animal {
//   constructor(public nome: string) {
//     super('mamifero');
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//   }
// }

// console.log('----------- Instância de Animal -----------');

// // const animal = new Animal('mamifero'); //! erro
// // console.log('animal :>> ', animal); //! erro

// console.log('----------- Instância de Gato -----------');

// const mingal = new Gato('mingal');
// console.log('mingal :>> ', mingal);

// mingal.mostrarDetalhes();

// console.log('----------- Instância de Cachorro -----------');
// const toto = new Cachorro('toto');
// toto.mostrarDetalhes();
// toto.nome = 'nome alterado'; //! sem erro
// toto.mostrarDetalhes();

/* 
-- com getter e setter
*/

// abstract class Animal {
//   constructor(protected readonly categoria: string) {}

//   mostrarCategoria(): void {
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Gato extends Animal {
//   private nome: string; //

//   constructor(nome: string) {
//     super('mamifero');
//     this.nome = nome;
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Cachorro extends Animal {
//   constructor(private _nome: string) {
//     super('mamifero');
//   }

//   get nome() {
//     console.log('função get chamada');
//     return this._nome;
//   }

//   set nome(n: string) {
//     console.log('função set chamada');
//     this._nome = n;
//   }

//   mostrarDetalhes(): void {
//     console.log('this._nome :>> ', this._nome);
//   }
// }

// console.log('----------- Instância de Animal -----------');

// // const animal = new Animal('mamifero'); //! erro
// // console.log('animal :>> ', animal); //! erro

// console.log('----------- Instância de Gato -----------');

// const mingal = new Gato('mingal');
// console.log('mingal :>> ', mingal);

// mingal.mostrarDetalhes();

// console.log('----------- Instância de Cachorro -----------');
// const toto = new Cachorro('toto');
// toto.mostrarDetalhes();

// console.log('toto.nome :>> ', toto.nome); // chamado com get
// toto.nome = 'novo nome do toto';
// console.log('toto.nome :>> ', toto.nome); // chamado com get
// toto.mostrarDetalhes();

/* 
- 410. lista de objetos (array listaAnimais não protegida)
*/

// abstract class Animal {
//   constructor(protected readonly categoria: string) {}

//   mostrarCategoria(): void {
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Gato extends Animal {
//   private nome: string; //

//   constructor(nome: string) {
//     super('mamifero');
//     this.nome = nome;
//   }

//   mostrarDetalhes(): void {
//     console.log('this.nome :>> ', this.nome);
//     console.log('this.categoria :>> ', this.categoria);
//   }
// }

// class Cachorro extends Animal {
//   constructor(private _nome: string) {
//     super('mamifero');
//   }

//   get nome() {
//     console.log('função get chamada');
//     return this._nome;
//   }

//   set nome(n: string) {
//     console.log('função set chamada');
//     this._nome = n;
//   }

//   mostrarDetalhes(): void {
//     console.log('this._nome :>> ', this._nome);
//   }
// }

// console.log('----------- Instância de Animal -----------');

// // const animal = new Animal('mamifero'); //! erro
// // console.log('animal :>> ', animal); //! erro

// console.log('----------- Instância de Gato -----------');

// const mingal = new Gato('mingal');
// console.log('mingal :>> ', mingal);

// mingal.mostrarDetalhes();

// console.log('----------- Instância de Cachorro -----------');
// const toto = new Cachorro('toto');
// toto.mostrarDetalhes();

// console.log('toto.nome :>> ', toto.nome); // chamado com get
// toto.nome = 'novo nome do toto';
// console.log('toto.nome :>> ', toto.nome); // chamado com get
// toto.mostrarDetalhes();

// /*
// --listaAnimais (array) só pode guardar objetos do tipo Animal, ou seja, objetos criados a partir da função construtora Animal (que tenha prop categoria)
// --- Com listaAnimais em readonly, o que  não pode mudar é o endereço na memória da lista; mas ainda assim é possível utilizar os métodos de uma array para aterá-la.
// */
// class Cliente {
//   readonly listaAnimais: Animal[] = []; // Endereço de memória AA

//   adicionarAnimais(...animais: Animal[]): void {
//     // esse parâmetro é uma array de objetos do tipo animal
//     // console.log('animais :>> ', animais);
//     // console.log('...animais :>> ', ...animais);
//     this.listaAnimais.push(...animais);
//   }
// }

// const pedro = new Cliente();
// pedro.adicionarAnimais(toto, mingal);
// console.log('pedro :>> ', pedro);
// console.log('pedro.listaAnimais :>> ', pedro.listaAnimais);
// // pedro.listaAnimais = []; //! com erro // endereço AB
// // pedro.listaAnimais.length = 0; //! sem erro // endereço AA
// pedro.listaAnimais.pop(); //! sem erro // endereço AA
// console.log('pedro.listaAnimais :>> ', pedro.listaAnimais);

/* 
- 410. lista de objetos (array listaAnimais não protegida)
*/

abstract class Animal {
  constructor(protected readonly categoria: string) {}

  mostrarCategoria(): void {
    console.log('this.categoria :>> ', this.categoria);
  }
}

class Gato extends Animal {
  private nome: string; //

  constructor(nome: string) {
    super('mamifero');
    this.nome = nome;
  }

  mostrarDetalhes(): void {
    console.log('this.nome :>> ', this.nome);
    console.log('this.categoria :>> ', this.categoria);
  }
}

class Cachorro extends Animal {
  constructor(private _nome: string) {
    super('mamifero');
  }

  get nome() {
    console.log('função get chamada');
    return this._nome;
  }

  set nome(n: string) {
    console.log('função set chamada');
    this._nome = n;
  }

  mostrarDetalhes(): void {
    console.log('this._nome :>> ', this._nome);
  }
}

console.log('----------- Instância de Animal -----------');

// const animal = new Animal('mamifero'); //! erro
// console.log('animal :>> ', animal); //! erro

console.log('----------- Instância de Gato -----------');

const mingal = new Gato('mingal');
console.log('mingal :>> ', mingal);

mingal.mostrarDetalhes();

console.log('----------- Instância de Cachorro -----------');
const toto = new Cachorro('toto');
toto.mostrarDetalhes();

console.log('toto.nome :>> ', toto.nome); // chamado com get
toto.nome = 'novo nome do toto';
console.log('toto.nome :>> ', toto.nome); // chamado com get
toto.mostrarDetalhes();

/*
--listaAnimais (array) não é alterado mais de fora
*/
class Cliente {
  private readonly _listaAnimais: Animal[] = []; // Endereço de memória AA
  private _tempListaAnimais: Animal[] = [];

  adicionarAnimais(...animais: Animal[]): void {
    // esse parâmetro é uma array de objetos do tipo animal
    // console.log('animais :>> ', animais);
    // console.log('...animais :>> ', ...animais);
    this._listaAnimais.push(...animais);

    this._tempListaAnimais.length = 0;
    this._tempListaAnimais = [...this._listaAnimais];
  }

  get listaAnimais() {
    // return [...this._listaAnimais]; // retorna uma cópia - endereço de memória AB, uma cópia da propriedade privada (pode gerar problema de memória)
    return [...this._tempListaAnimais]; // mais performático
  }
}

const pedro = new Cliente();
pedro.adicionarAnimais(toto, mingal);
console.log('pedro :>> ', pedro);
pedro.listaAnimais.length = 0;
console.log('pedro :>> ', pedro);

/* 
Aula 412 - intefaces vs. classes abstratas
próximo arquivo
*/
