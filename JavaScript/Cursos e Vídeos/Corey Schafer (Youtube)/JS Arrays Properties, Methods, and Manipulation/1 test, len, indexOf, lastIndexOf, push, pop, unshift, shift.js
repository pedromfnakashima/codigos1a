// https://www.youtube.com/watch?v=1iPs43TppOY&list=PL-osiE80TeTucQUM10Ezv4S7SVoFozLMK

// ---------------- Test

/* var string1 = 'Test';

var object1 = {'name':'test'};

var array1 = [0,1,2,3,4,5];

var testString = Array.isArray(string1);
var testObj = Array.isArray(object1);
var testArray = Array.isArray(array1);

console.log('String: ' + testString)
console.log('Object: ' + testObj)
console.log('Array: ' + testArray) */

//------------------ Len

/* var array2 = [0,1,2,3,4,5,6,7,8,9];

var arrayLen = array2.length;

console.log('Length: ' + arrayLen);

var sum=0;
for(var i = 0; i<array2.length; i++){
    sum += array2[i];
}
console.log('Soma: ' + sum);
 */
// ------------------ indexOf() / lastIndexOf()

/* var array31 = [1,2,3,1,2,3,1,2,3]

var indexOfThree = array31.indexOf(3);
console.log('Index do 3: ' + indexOfThree);

var indexOfThree = array31.indexOf(3,3);
console.log('Index do 3: ' + indexOfThree);

// Ao invés de procurar da esquerda para direita, procura da direita para a esquerda
var lastIndexOfThree = array31.lastIndexOf(3);
console.log('Último Index do 3: ' + lastIndexOfThree); */

// --------------- Index de array com string

/* var array32 = ['Corey','Rob','Micky','Rob','Stan'];

var indexOfRob = array32.indexOf('Rob')
console.log('Index do Rob: ' + indexOfRob);

var lastIndexOfRob = array32.lastIndexOf('Rob')
console.log('Index último do Rob: ' + lastIndexOfRob);

var indexOfJoey = array32.indexOf('Joey')
console.log('Index de Não existente: ' + indexOfJoey); */

// ---------------- push() / pop() -> adiciona no final

/* var array4 = [1,2,3];

// Push One
array4.push('One')
console.log('Push: ' + array4.toString());

// Push Two
array4.push('Two')
console.log('Push: ' + array4.toString());

// POP (remove do final)
array4.pop();
console.log('Pop: ' + array4.toString());

// POP (remove do final)
array4.pop();
console.log('Pop: ' + array4.toString()); */

// ---------------- unshift() / shift() -> adiciona no início

var array5 = [1,2,3];

// Unshift One
array5.unshift('One');
console.log('Unshift: ' + array5.toString());

// Unshift Two
array5.unshift('Two');
console.log('Unshift: ' + array5.toString());

// Shift (remove do início)
array5.shift();
console.log('Shift: ' + array5.toString());

// Shift (remove do início)
array5.shift();
console.log('Shift: ' + array5.toString());
