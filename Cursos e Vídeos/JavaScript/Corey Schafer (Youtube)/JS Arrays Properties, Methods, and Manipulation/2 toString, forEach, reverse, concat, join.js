//https://www.youtube.com/watch?v=8JgU2WmrZXI&list=PL-osiE80TeTucQUM10Ezv4S7SVoFozLMK&index=2

// -------------------- toString()

/* var array6 = ['This',1,'Time'];

var string6 = array6.toString();

console.log('String: ' + string6); */

// -------------------- forEach()

/* var array7 = [1,2,3,4,5,6,7,8,9];

console.log('Original: ' + array7.join(', '));

function timesTen(element, index, array){
    array[index] = element * 10;
}

array7.forEach(timesTen);

console.log('Depois: ' + array7.join(', ')); */

// -------------------- forEach()
/* 
var array7 = [
    {
        name: 'Corey',
        age: 28
    },
    {
        name: 'John',
        age: 52
    },
    {
        name: 'Steve',
        age: 36
    }
];

function listPeople(element,index){
    console.log('Pessoa: ' + (index+1));
    console.log('Nome: ' + element.name);
    console.log('Idade: ' + element.age);
    console.log('---------------');
}

array7.forEach(listPeople); */

// -------------------- reverse()

/* var array8 = [0,1,2,3,4,5,6,7,8,9];
console.log('Original: ' + array8.toString());
array8.reverse();
console.log('Invertido: ' + array8.toString());

var array8 = ['Reverse','This','Array'];
console.log('Original: ' + array8.toString());
array8.reverse();
console.log('Invertido: ' + array8.toString()); */

// -------------------- concat()
/* 
var array91 = ['a','b','c']
var array92 = ['d','e','f']

console.log('Array 1: ' + array91.toString());
console.log('Array 2: ' + array92.toString());

var arrayConcat = array91.concat(array92);

console.log('Array concatenado: ' + arrayConcat.toString());

var arrayConcat2 = array91.concat(1,2,3,['d','e','f']);

console.log('Array concatenado2: ' + arrayConcat2.toString());
 */
// -------------------- join()

var array10 = [192,168,1,1];
var string10 = array10.join('.');
console.log('Array concatenado: ' + string10.toString());

var array10 = ['A', ' ', 'S','t','r','i','n','g'];
var string10 = array10.join('');
console.log('Array concatenado: ' + string10.toString());















