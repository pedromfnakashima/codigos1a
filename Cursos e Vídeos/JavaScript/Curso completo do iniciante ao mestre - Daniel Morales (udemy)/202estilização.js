/* 
202. Introdução
*/

//

let div = document.querySelector('div');
// console.log('div :>> ', div);
// console.log('div.style.backgroundColor :>> ', div.style.backgroundColor);

// div.style.backgroundColor = '#ddd';
// console.log('div.style.backgroundColor :>> ', div.style.backgroundColor);

// add(), remove(), toggle()

div.classList.add('teste1');
div.classList.add('teste2');

// console.log('div :>> ', div);

// console.log('div.className :>> ', div.className);

/* 
Estilos computados
getComputedStyle()
*/

// console.log('getComputedStyle(div) :>> ', getComputedStyle(div));
// console.log(
//   'getComputedStyle(div).backgroundColor :>> ',
//   getComputedStyle(div).backgroundColor
// );

/* 
--Tamanho e posição no DOCUMENTO
elemento.offsetHeight
elemento.offsetWidth
elemento.offsetLeft
elemento.offsetTop

Essas propriedades não têm relação com o CSS em si, nem com a viewport (implicando que, escrollando a tela, não muda por exemplo o div.offsetTop) mas como esses elementos estão sendo visualizados na tela.
*/

// console.log('Tamanho do elemento:');
// console.log('div.offsetHeight :>> ', div.offsetHeight);
// console.log('div.offsetWidth :>> ', div.offsetWidth);
// console.log('Posição do elemento no documento:');
// console.log('div.offsetLeft :>> ', div.offsetLeft);
// console.log('div.offsetTop :>> ', div.offsetTop);

/* 
-- Posição em relação à VIEWPORT (área visível)
elemento.getBoundingClientRect().
bottom
left
right
top
width
height

As propriedades são relacionadas à referência -canto superior esquerdo-.

*/

console.log('div.getBoundingClientRect() :>> ', div.getBoundingClientRect());
console.log(
  'div.getBoundingClientRect().top :>> ',
  div.getBoundingClientRect().top
);
console.log(
  'div.getBoundingClientRect().bottom :>> ',
  div.getBoundingClientRect().bottom
);
console.log('innerHeight :>> ', innerHeight);
