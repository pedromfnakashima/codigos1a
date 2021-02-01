




//- Criando arrays e acessando elementos

//-- Forma 1
const arr = new Array();
// console.log(typeof arr);
// console.log(arr);

const arr2 = new Array(true, 'Pedro', 36, new Array(2, 4, 10));
// console.log(arr2);

arr[0] = 'Pedro';
arr[1] = 'Nakashima';
arr[2] = 36;
// console.log(arr);


// console.log(arr2[3]); // [ 2, 4, 10 ]
// console.log(arr2[3][1]); // 4
// console.log(arr2[3][3]); // undefined
// console.log(arr2[3].length) // 3
// // Último elemento: length - 1
// console.log(arr2[3][arr2[3].length - 1]) // 10: último elemento do array [2,4,10]

//-- Forma 2
const arr3 = ['Pedro', 'Massao', 36, [3,6,9], true];
// console.log(arr3)
// console.log(arr3[3])

//- Adicionando itens ao array definindo a posição

arr3[5] = 'novo valor'
// console.log(arr3)

//--- Conclusão: p/ adicionar um valor a um array basta definir o novo elemento como ocupando a posição length

arr3[arr3.length] = 'fui adicionado com o length'
// console.log(arr3)

//- Adicionando itens ao array utilizando o método push

arr3.push('fui adicionado com push')

arr3.push('a','b','c') // adicionando 3 valores de uma vez
console.log(arr3)

//- acessando com o auxílio de variáveis

let n = 1
console.log(arr3[n]) // Massao
