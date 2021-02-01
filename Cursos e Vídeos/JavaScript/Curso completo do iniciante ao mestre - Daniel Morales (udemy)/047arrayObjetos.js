

//- Definindo array de objetos

//-- Forma 1

pessoa1 = {nome:'Pedro', idade:36, email:'email@servidor.com.br'};
pessoa2 = {nome:'fulano', idade:40, email:'fulano@servidor.com.br'};

const pessoas = [pessoa1, pessoa2];

// console.log(pessoas);

//-- Forma 2

const pessoas2 = [
    {
        nome:'Maria',
        idade: 28
    },
    {
        nome:'Helena',
        idade: 45
    },
    {
        nome:'João',
        idade: 18
    }
]

// console.log(pessoas2);
// console.log(pessoas2[0]);
// console.log(pessoas2[0]['nome']);

//- Iterando array de objetos

for (chave in pessoas2) {
    // console.log(chave);
    // console.log(pessoas2[chave]);
    console.log(`${pessoas2[chave]['nome']} tem ${pessoas2[chave]['idade']} anos.`);
}



