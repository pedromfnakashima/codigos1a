
/* Semelhante ao args e kwargs do python
Deixa livre o número de argumentos
*/

//- soma com o array

// function somar(arr) {
//     let total = 0
//     for (let i=0; i<arr.length; i+=1) {
//         total += arr[i]
//     }
    
//     return total
// }

// console.log(somar([1,2]))
// console.log(somar([1,2,3,4]))
// console.log(somar([1,2,3,4,5,6,7,8,9,10]))

//- soma com arguments (se comporta como array)
//- Obs. 1: arguments NÃO EXISTE dentro de arrow functions.

function somar() {
    
    console.log(arguments) // argumetns: no console, parece objeto; no browser, parece array.

    let total = 0
    for (let i=0; i<arguments.length; i+=1) {
        total += arguments[i]
    }
    
    return total
}

console.log(somar(1,2))
console.log(somar(1,2,3,4))
console.log(somar(1,2,3,4,5,6,7,8,9,10))




