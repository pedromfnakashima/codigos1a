/* 
O que são eventos.
Evento é uma ocorrência interativa que ocorre por intervenção do usuário ou não.
Exemplos:
. Seguir um link;
. Submeter um formulário;
. Carregar uma página ou recurso do servidor;
. Digitar um texto;
. Mover um mouse...

Event handlers.
Uma função que é executada quando um evento ocorre.

Disparador de eventos.
É o elemento que disparou o evento. Ou seja, o elemento ao qual foi atrelado o event handler.

---EVENT HANDLER - DOM LEVEL 0 <= é pior
<button onclick="funcao()" id="btn">
    ...
<button>

ou

const btn = document.getElementById('btn')
btn.onclick = funcao // <= sem parênteses

! Problema com o Level 0: NÃO É POSSÍVEL atrelar 2 eventos no mesmo elemento html. Sempre se sobrescreve a função, seja ela definida no html, seja ela definida no JavaScript.

---EVENT HANDLER - DOM LEVEL 2 <= é melhor

const btn = document.getElementById('btn')
btn.addEventListener(evento, funcao, fase)

! Com o Level 2, ou seja, usando o Event Listener, É POSSÍVEL atrelar duas funções no mesmo objeto.

*/

// const btn1 = document.getElementById('btn1');
// const btn2 = document.getElementById('btn2');
// const btn3 = document.getElementById('btn3');

//- DOM level 0

// // 1º evento Level 0, em btn1
// btn1.onclick = function () {
//   console.log('click em btn1 - FUNÇÃO ANÔNIMA');
// };

// // 2º evento Level 0, em btn1
// function clicou() {
//   console.log(
//     'click btn 1/2 - FUNÇÃO CLICOU - SOBRESCREVEU o evento da FUNÇÃO ANÔNIMA que também estava atrelado a btn1'
//   );
// }
// // 2º evento Level 0 - função clicou SOBRESCREVE a função anônima (pois não é possível atrelar dois eventos no mesmo elemento HTML):
// btn1.onclick = clicou;

//- DOM level 2

// // 1º evento DOM Level 2, em btn2
// btn2.addEventListener('click', clicou);

// // 2º evento DOM Level 2, em btn2 - não sobrescreve 1º evento DOM Level 2 em btn2
// btn2.addEventListener('click', function () {
//   console.log(
//     'click btn 2 - FUNÇÃO ANÔNIMA - NÃO sobrescreveu o evento anterior; foi possível atrelar um segundo evento ao mesmo elemento HTML (bnt2)'
//   );
// });

/* 
PROPAGAÇÃO DE EVENTOS
. Fase de captura - valor = true
. Fase de bolha ou borbulhamento (bubling) - fase padrão - valor = false

Quando eu clico no link, estou clicando também em toda a hierarquia na qual aquele link está incluído.

EVENT HANDLER - DOM LEVEL 2 <= é melhor

const btn = document.getElementById('btn')
btn.addEventListener(evento, funcao, fase)

*/

//-- Fase de bolha: nível menor -> nível maior

//--- Exemplo do professor
/* btn3.addEventListener('click', function () {
  console.log('clicou no btn 3');
});

document.addEventListener('click', function () {
  console.log('clicou no documento');
}); */

//--- Exemplo do Kyle

// btn3.addEventListener(
//   'click',
//   function () {
//     console.log('clicou no btn 3');
//   },
//   { capture: false }
// );

// document.addEventListener(
//   'click',
//   function () {
//     console.log('clicou no documento');
//   },
//   { capture: false }
// );

//! Resultado (independentemente da ordem das funções): clicou no btn 3 >> clicou no documento

//-- Fase de captura -> nível maior -> nível maior

//--- Exemplo 01
// btn3.addEventListener('click', function() {
//     console.log('clicou no btn 3')
// }, false) // 3º argumento: false (padrão); se colocar true não faz diferença

// document.addEventListener('click', function() {
//     console.log('clicou no documento')
// }, true) // <= true: fase de captura

//--- Exemplo 1a (Kyle)

// btn3.addEventListener(
//   'click',
//   function () {
//     console.log('clicou no btn 3');
//   },
//   { capture: false }
// );

// document.addEventListener(
//   'click',
//   function () {
//     console.log('clicou no documento');
//   },
//   { capture: true }
// );

//! Resultado: clicou no documento >> clicou no btn 3

//--- Exemplo 02a (dispara a ação na fase de borbulhamento)

// btn3.addEventListener('click', function() {
//     console.log('clicou no btn 3')
// }, false) // 3º argumento: false (padrão); se colocar true não faz diferença

// const container1 = document.getElementById('container1')
// container1.addEventListener('click', function() {
//     console.log('clicou em container1')
// }, false)

//--- Exemplo 02b (dispara a ação na fase de borbulhamento)

// btn3.addEventListener(
//   'click',
//   (e) => {
//     console.log('clicou no btn3');
//   },
//   { capture: false }
// );

// const container1 = document.getElementById('container1');
// container1.addEventListener(
//   'click',
//   (e) => {
//     console.log('clicou em container1');
//   },
//   { capture: true }
// );

//! clicou no btn 3 >> clicou no container

//--- Exemplo 03 (dispara a ação na fase de captura)

// btn3.addEventListener('click', function() {
//     console.log('clicou no btn 3')
// }, false) // 3º argumento: false (padrão); se colocar true não faz diferença

// const container1 = document.getElementById('container1')
// container1.addEventListener('click', function() {
//     console.log('clicou em container1')
// }, true)

//! clicou no container >> clicou no btn 3

//- Para PARAR A PROPAGAÇÃO, precisa ter acesso ao OBJETO EVENTO e
/* 
OBJETO DE EVENTO
Seja com o DOM 0 ou DOM 2, os handlers (funções atreladas a eventos) recebem por parâmetro um objeto do tipo evento. Para ter acesso a esse objeto, basta dar um nome ao parâmetro.

Para ter acesso ao objeto de evento, precisa passar um nome à função que tá no segundo argumento.

Situação: quando chegar no btn3, quero parar a propagação.

*/
//--- Exemplo 1a

// btn3.addEventListener(
//   'click',
//   function (objetoEvento) {
//     // console.log(objetoEvento) // <= objeto MouseEvent, com vários atributos. Há o método stopPropagation()
//     objetoEvento.stopPropagation(); //! não vai propagar, nem pra container, nem pra document
//     console.log('clicou no btn 3');
//   },
//   false
// );

// const container1 = document.getElementById('container1');
// container1.addEventListener(
//   'click',
//   function () {
//     console.log('clicou em container1');
//   },
//   false
// );

// document.addEventListener(
//   'click',
//   function (e) {
//     console.log('clicou no documento');
//     console.log('currentTarget: ', e.currentTarget);
//     console.log('target: ', e.target);
//   },
//   false
// );

//--- Exemplo 1b (metodologia kyle)

// const container1 = document.getElementById('container1');
// container1.addEventListener(
//   'click',
//   (e) => {
//     console.log('clicou em container1');
//   },
//   { capture: false }
// );

// btn3.addEventListener(
//   'click',
//   (e) => {
//     // console.log(e);
//     console.log('clicou em btn3');
//     e.stopPropagation();
//   },
//   { capture: false }
// );

//! Resultado: clicou no btn 3

//- DELEGAÇÃO DE EVENTOS
/* 
Especialmente útil quando tempos muitos filhos com eventos atrelados individualmente. Delegar um evento é o ato de atrelar um evento ao elemento pai, economizando recursos da máquina.
Ou seja, é colocar o evento não no filho (exemplo: li), mas no elemento-pai (exemplo: ul). A partir do pai, é possível identificar qual foi a li clicada.

*/

/* const container2 = document.querySelector('.container2');
const btns = document.querySelectorAll('.container2 button'); // <= nodelist */

//-- Tarefa: colocar um evento em cada um dos botões (filhos)

//--- Forma 1 - inviável quando tiver muitos filhos (botões)

// btns[0].addEventListener('click', function(e) {
//     e.stopPropagation()
//     console.log('clicou em btn')
// })

// btns[1].addEventListener('click', function(e) {
//     e.stopPropagation()
//     console.log('clicou em btn')
// })

// btns[2].addEventListener('click', function(e) {
//     e.stopPropagation()
//     console.log('clicou em btn')
// })

//--- Forma 2 - viável, mas pode causar problema de performance da aplicação
/*
ETAPAS:
1. Transformar a nodelist btns em objeto do tipo Array;
2. Executar um loop;

*/

// [...btns].forEach( btn => {
//     btn.addEventListener('click', function(e){
//         e.stopPropagation()
//         console.log(e.target) //! e.target é o elemento que disparou o evento (elementoa atrelado ao evento)
//     })
// })

//--- Forma 3a - colocar o listern não em btns, mas no container2 (pai, que contém os botões)

// container2.addEventListener('click', function(e) {
//     e.stopPropagation()
//     console.log(e.target)
// })

//! Problema: quando clica fora (fora dos botões, porém na div de classe container2), também dispara

//--- Forma 3b - colocar o listern não em btns, mas no container2 (pai, que contém os botões), mas só executa a funcionalidade se o que disparou o evento foi elemento do tipo button

// const container2 = document.querySelector('.container2');
// const btns = document.querySelectorAll('.container2 button'); // <= nodelist

// container2.addEventListener('click', function (e) {
//   e.stopPropagation();
//   //! Resolve o problema: pergunta se o e.target é do tipo button
//   // console.log(e.target.nodeName)
//   if (e.target.nodeName === 'BUTTON') {
//     console.log(e.target);
//   }
// });

//--- Forma 3c (metodologia Kyle) -

// container2.addEventListener('click', (e) => {
//   if (e.target.matches('button')) {
//     console.log(e.target);
//   }
// });

//---- Forma 3d (metodologia Kyle) - com funçã <<== SOLID

// function addGlobalEventListener(type, selector, callback) {
//   document.addEventListener(type, (e) => {
//     if (e.target.matches(selector)) {
//       callback(e);
//     }
//   });
// }

// addGlobalEventListener('click', '.container2 button', (e) => {
//   console.log(e.target);
// });

// addGlobalEventListener('click', '#container1 button', (e) => {
//   console.log(e.target);
// });

//! Problema resolvido.

//- .target vs .currentTarget
/* 
Explicação:
https://stackoverflow.com/questions/10086427/what-is-the-exact-difference-between-currenttarget-property-and-target-property/10086501

.target: elemento ao qual o event listener é atrelado. É fixo.
.currrentTarget: elemento que é disparado. É dinâmico.

obs.: o this, se a o callbalck for atribuído com function expression, é a mesma coisa que o e.currentTarget
obs.: o this, se a o callbalck for atribuído com arrow function, é o this é o de fora (qual?)

*/

//--- Exemplo 1a - não bom, por isso foi apagado - professor

//--- Exemplo Pedro (metodologia Kyle) -

const body = document.querySelector('body');
const segundaDiv = document.querySelector('.container2');
const bnt3 = document.querySelector('.container2 #btn3');

body.addEventListener(
  'click',
  (e) => {
    // console.log('body capture');
    console.log(
      'O click que foi atrelado a',
      e.target.tagName,
      'está atualmente em',
      e.currentTarget.tagName
    );
  },
  { capture: true }
);

body.addEventListener(
  'click',
  (e) => {
    // console.log('body bubble');
    console.log(
      'O click que foi atrelado a',
      e.target.tagName,
      'está atualmente em',
      e.currentTarget.tagName
    );
  },
  { capture: false }
);

segundaDiv.addEventListener(
  'click',
  (e) => {
    // console.log('segundaDiv capture');
    console.log(
      'O click que foi atrelado a',
      e.target.tagName,
      'está atualmente em',
      e.currentTarget.tagName
    );
  },
  { capture: true }
);

segundaDiv.addEventListener(
  'click',
  (e) => {
    // console.log('segundaDiv bubble');
    console.log(
      'O click que foi atrelado a',
      e.target.tagName,
      'está atualmente em',
      e.currentTarget.tagName
    );
  },
  { capture: false }
);

bnt3.addEventListener(
  'click',
  (e) => {
    // console.log('bnt3 capture');
    console.log(
      'O click que foi atrelado a',
      e.target.tagName,
      'está atualmente em',
      e.currentTarget.tagName
    );
  },
  { capture: true }
);

bnt3.addEventListener(
  'click',
  (e) => {
    // console.log('bnt3 bubble');
    console.log(
      'O click que foi atrelado a',
      e.target.tagName,
      'está atualmente em',
      e.currentTarget.tagName
    );
  },
  { capture: false }
);

/* document.addEventListener(
  'click',
  (e) => {
    // console.log('document capture');
    console.log(
      'O click que foi atrelado a',
      e.target.tagName,
      'está atualmente em',
      e.currentTarget.tagName
    );
  },
  { capture: true }
);

document.addEventListener(
  'click',
  (e) => {
    // console.log('document bubble');
    console.log(
      'O click que foi atrelado a',
      e.target.tagName,
      'está atualmente em',
      e.currentTarget.tagName
    );
  },
  { capture: false }
); */
