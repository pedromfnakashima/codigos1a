
// Acessando com o auxílio de arrays

// const nomes = ['Daniel','Maria','Joao']
// const idades = [40,28,35]

// console.log(nomes[0],idades[0])

// Acessando com o auxílio de objects

//- Criando objects

//-- Forma 1

const pessoa = new Object();
// console.log(pessoa);

pessoa.nome = 'Pedro';
pessoa.idade = 36;

// console.log(pessoa);
// console.log(pessoa.nome);
// console.log(pessoa.idade);
// console.log(pessoa['nome']);
// console.log(pessoa['idade']);

//--- acessando com variáveis:

prop = 'idade';
// console.log(pessoa[prop]);

//-- Forma 2

const pessoa2 = {
    nome: 'pedro',
    idade: 36
}

console.log(pessoa2);

