// https://www.youtube.com/watch?v=1gupsllu5wQ&list=PL-osiE80TeTucQUM10Ezv4S7SVoFozLMK&index=7

// ----------------------------- reduce() e reduceright()

// ----------------------------- reduce() com array numérico

/* var array17 = [1,2,3,4,5];

console.log('Original: ' + array17.join(', '));

function addValues(previous,current,index,array){
    return previous + current;
}

var result17 = array17.reduce(addValues);

console.log('Reduce Result: ' + result17); */

// ----------------------------- reduce() com array string - junta as strings

/* var array17 = ['a','b','c','d','e'];

console.log('Original: ' + array17.join(', '));

function addValues(previous,current,index,array){
    return previous + current;
}

var result17 = array17.reduce(addValues);

console.log('Reduce Result: ' + result17); */

// ----------------------------- reduceRight() com array string - junta as strings de forma invertida

/* var array17 = ['a','b','c','d','e'];

console.log('Original: ' + array17.join(', '));

function addValues(previous,current,index,array){
    return previous + current;
}

var result17 = array17.reduceRight(addValues);

console.log('Reduce Result: ' + result17); */

// ----------------------------- reduce() com object

var array17 = [
    {
        name:'Corey',
        age:28
    },
    {
        name:'John',
        age:52
    },
    {
        name:'Steve',
        age:36
    }
];

// Array original
console.log('Original:')
for(var i=0; i<array17.length; i++){
    console.log('(' + array17[i].name + ', ' + array17[i].age + ')');
}

function totalAge(previous,current){
    return previous + current.age;
}

var result17 = array17.reduce(totalAge,0);

console.log('Reduce Result: ' + result17);


