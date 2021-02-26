"use strict";
/*
Interfaces vs. classes abstratas

Os dois cumprem o mesmo objetivo de forma diferente.


*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Animal = void 0;
class Animal {
    constructor(categoria) {
        this.categoria = categoria;
    }
    mostrarCategoria() {
        console.log('this.categoria :>> ', this.categoria);
    }
}
exports.Animal = Animal;
const laica = {
    categoria: 'mamífero',
    mostrarDetalhes() {
        console.log('qualquer coisa');
    },
};
console.log('laica :>> ', laica);
class Gato extends Animal {
    constructor(nome, idade) {
        super('mamifero');
        this.nome = nome;
        this.idade = idade;
    }
    mostrarDetalhes() {
        console.log('mostrar detalhe chamado');
    }
}
class Cachorro {
    constructor(categoria, nome, idade) {
        this.categoria = categoria;
        this.nome = nome;
        this.idade = idade;
    }
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
const pedro = {
    name: 'Pedro',
    idade: 36,
};
console.log('pedro :>> ', pedro);
// const idade: TesteT = 10
const idade = { qtd: 1 };
