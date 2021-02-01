// https://www.youtube.com/watch?v=JskeRdu_X8Q&list=PL-osiE80TeTucQUM10Ezv4S7SVoFozLMK&index=5

// --------------------------- filter() com array

/* var array14 = [86,28,19,4,21,25,13,52];

console.log('Original: ' + array14.join(', '));

function numOver(element, index, theArray){
    return element > 20;
}

var filteredArray = array14.filter(numOver);

console.log('Filtered: ' + filteredArray.join(', ')); */


// --------------------------- filter() com object

/* var array14 = [
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
for(var i=0; i<array14.length; i++){
    console.log('(' + array14[i].name + ', ' + array14[i].age + ')');
}

function filterAge(element){
    return element.age > 30;
}

var filteredArray = array14.filter(filterAge);

// Array filtrado
console.log('Filtered:')
for(var i=0; i<filteredArray.length; i++){
    console.log('(' + filteredArray[i].name + ', ' + filteredArray[i].age + ')');
}
 */

// --------------------------- every() com array

/* var array15 = [86,28,19,14,21,25,13,52];
console.log('Original: ' + array15.join(', '));

function isEvery(element){
    return element > 10;
}

var passed = array15.every(isEvery)
console.log('Every result: ' + passed); */

// --------------------------- every() com object
/* 
var array15 = [
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
for(var i=0; i<array15.length; i++){
    console.log('(' + array15[i].name + ', ' + array15[i].age + ')');
}

function allUnder(element){
    return element.age < 60;
}

var passed = array15.every(allUnder)
console.log('Every result: ' + passed); */

// --------------------------- some() com array

/* var array16 = [86,28,21,4,22,24,14,52];
console.log('Original: ' + array16.join(', '));

function someOdd(element){
    return (element % 2 == 1);
}

var passed = array16.some(someOdd)
console.log('Some result: ' + passed); */

// --------------------------- some() com object

var array16 = [
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
for(var i=0; i<array16.length; i++){
    console.log('(' + array16[i].name + ', ' + array16[i].age + ')');
}

function someAge(element){
    return element.age > 50;
}

var passed = array16.some(someAge)
console.log('Some result: ' + passed);




