
// https://www.youtube.com/watch?v=qxzp4X6sfGo&list=PL-osiE80TeTucQUM10Ezv4S7SVoFozLMK&index=8

// ----------------------------- map() com array numérico

/* var array18 = [10,20,30,40,50];

console.log('Original: ' + array18.join(', '))

function addTax(element) {
    return '$' + (element * 1.06).toFixed(2);
}

var mapped = array18.map(addTax);

console.log('Mapped: ' + mapped.join(', '))
 */


// ----------------------------- map() com array string

/* var array18 = ['anne','bob','corey','dan','eric'];

console.log('Original: ' + array18.join(', '))

function toUpper(element) {
    return element.toUpperCase();
}

var mapped = array18.map(toUpper)

console.log('Mapped: ' + mapped.join(', ')) */

// ----------------------------- map() encadeado reduce()

/* var array19 = [10,20,30,40,50];

console.log('Original: ' + array19.join(', '))

// aplica alíquotas
function addTax(current,index,array) {
    var total = current * 1.06;
    total = Math.round(total * 100) / 100;
    return Number(total.toFixed(2));
}

// soma tudo
function sumTotal(previous,current){
    return previous + current;
}

var result19 = array19.map(addTax).reduce(sumTotal);
console.log('Result: ' + result19) */


// ----------------------------- encadeando funções

var result19 = 'Please Reverse Me'.split('').reverse().join('');
console.log('Result: ' + result19)
