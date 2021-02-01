
const produto = {
    nome: 'caneta',
    qtd: 10,
    comprar: function(n) {
        if (n > this.qtd) {
            console.log('compra não realizada');
            return 'quantidade não disponível'; // o return  faz sair da função
        }
        this.qtd -= n;
    }

}

// outra sintaxe (em versões mais recentes do JavaScript):

// const produto = {
//     nome: 'caneta',
//     qtd: 10,
//     comprar(n) {
//         if (n > this.qtd) {
//             console.log('compra não realizada');
//             return 'quantidade não disponível'; // o return  faz sair da função
//         }
//         this.qtd -= n;
//     }

// }

// Arrow function

const produto2 = {
    nome: 'caneta',
    qtd: 10,
    comprar: function(n) {
        if (n > this.qtd) {
            // console.log('compra não realizada');
            return 'quantidade não disponível'; // o return  faz sair da função
        }
        this.qtd -= n;
    },
    teste1: function() {
        console.log('------- TESTE1 -----');
        console.log(this);
    },
    teste2: () => {
        console.log('------- TESTE2 -----');
        console.log(this);
    }

}

//- Tirar 2 canetas do estoque (qtd)


//-- Forma 1 - mudando diretamente com atribuição chave-valor

// produto['qtd'] -= 2;
// console.log(produto);

//-- Forma 2 - através de método do próprio objeto

// produto.comprar(3);
// console.log(`Quantidade restante: ${produto['qtd']}`);

// produto.comprar(2);
// console.log(`Quantidade restante: ${produto['qtd']}`);

// produto.comprar(8);
// console.log(`Quantidade restante: ${produto['qtd']}`);


// --- O que tem dentro do 'this': método normal vs. método arrow function. Num script RODANDO SOZINHO.
//--- MÉTODO NORMAL: 'this' = próprio objeto.
//--- MÉTODO ARROW FUNCTION: 'this' = objeto vazio.

// --- O que tem dentro do 'this': método normal vs. método arrow function. Num script rodando no NAVEGADOR (esse script é importado no arquivo 046métodosObjeto.html - ver no console do chrome).
//--- MÉTODO NORMAL: 'this' = próprio objeto.
//--- MÉTODO ARROW FUNCTION: 'this' = objeto WINDOW.


//!! CONCLUSÃO 1: não usar (via de regra) a arrow function.

produto2.comprar(3);
// console.log(produto2);

produto2.teste1();
produto2.teste2();



