
//- Identificar se existe um elemento num array
// let array_teste = [1,4,9,4];
// console.log(array_teste.indexOf(4)) //> 1 (posição da primeira ocorrência = 1)
// console.log(array_teste.lastIndexOf(4)) //> 1 (posição da última ocorrência = 3)
// console.log(array_teste.indexOf(5)) //> -1 (não encontrado)

// Criar um array com números randômicos não repetidos.

// console.log(Math.random());
// console.log(Math.random() * 100);
// console.log(Math.floor(Math.random() * 100));


function generateRandomInteger(max) {
    return parseInt(Math.random() * max)
}

// let arr = []
// while (arr.length <= 20) {
//     let randomNumber = generateRandomInteger(30)
//     // console.log(randomNumber)

//     if (arr.indexOf(randomNumber) < 0) {
//         arr.push(randomNumber)
//     }
//     else {
//         console.log(randomNumber, 'já existe no array')
//     }
// }
// console.log(arr)

let arr = []
let i = 0
while (arr.length <= 20) {
    
    i += 1
    
    let randomNumber = generateRandomInteger(30)
    // console.log(randomNumber)

    if (arr.indexOf(randomNumber) < 0) {
        arr.push(randomNumber)
    }
    else {
        console.log(randomNumber, 'já existe no array')
    }
}
console.log(arr)
console.log("o loop foi executado ",i," vezes")



