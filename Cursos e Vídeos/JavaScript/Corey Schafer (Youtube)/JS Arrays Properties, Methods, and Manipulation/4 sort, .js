// https://www.youtube.com/watch?v=cdPS-lmlwco&list=PL-osiE80TeTucQUM10Ezv4S7SVoFozLMK&index=4

// ----------------------------- sort() numérico: ordenação crescente

/* var array13 = [4,3,2,1,10,20,30,40];

console.log('Original: ' + array13.join(', '));

function sortNum(a,b){
    return a-b;
}

array13.sort(sortNum);

console.log('Ordenado crescente: ' + array13.join(', ')); */

// ----------------------------- sort() numérico: ordenação decrescente

/* var array13 = [4,3,2,1,10,20,30,40];

console.log('Original: ' + array13.join(', '));

function sortNum(a,b){
    return b-a;
}

array13.sort(sortNum);

console.log('Ordenado crescente: ' + array13.join(', ')); */

// ----------------------------- sort() string: ordenação crescente - robusto a letra minúscula
/* 
var array13 = ['Jack','Jill','Corey','Pete','anne'];

console.log('Original: ' + array13.join(', '));

function sortAlpha(a,b){
    var aLower = a.toLowerCase();
    var bLower = b.toLowerCase();
    if (aLower < bLower) return -1;
    if (aLower > bLower) return 1;
    return 0;
}

array13.sort(sortAlpha);

console.log('Ordenado crescente: ' + array13.join(', '));
 */
// ----------------------------- sort() object

var array13 = [
    {
        first:'Joe',
        last:'Smith'
    },
    {
        first:'Anne',
        last:'Smith'
    },
    {
        first:'Tom',
        last:'Doe'
    },
    {
        first:'Anne',
        last:'Doe'
    }
];
// Lista original
console.log('Original:')
for(var i=0; i<array13.length; i++){
    console.log((i+1) + ': ' + array13[i].first + ' ' + array13[i].last);
}

// Ordena pelo primeiro nome
function sortNames(a,b){
    var aLower = a.first.toLowerCase();
    var bLower = b.first.toLowerCase();
    var aLast = a.last.toLowerCase();
    var bLast = b.last.toLowerCase();
    if(aLower == bLower){
        if (aLast < bLast) return -1;
        if (aLast > bLast) return 1;
        return 0;
    }
    if (aLower < bLower) return -1;
    if (aLower > bLower) return 1;
    return 0;
}

array13.sort(sortNames)

console.log('Ordenado rpimeiro pelo primeiro nome e depois pelo sobrenome:')
for(var i=0; i<array13.length; i++){
    console.log((i+1) + ': ' + array13[i].first + ' ' + array13[i].last);
}











