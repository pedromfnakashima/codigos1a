/* 
...
Útil sempre que precisar quebrar o array e passar em elementos separados.
*/

const arr = [1,2,3]
const arr2 = [4,5,6]

function sum() {
    console.log(arguments)
    console.log(arguments.length)
}

// sum(arr)
// sum(...arr)

// arr.push(arr2)
// console.log(arr) // [ 1, 2, 3, [ 4, 5, 6 ] ]

arr.push(...arr2)
console.log(arr) // [ 1, 2, 3, 4, 5, 6 ]






















