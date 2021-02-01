const avo = document.querySelector('.avo');
const pai = document.querySelector('.pai');
const filho = document.querySelector('.filho');

/* 
-Exemplo 01
*/

/* avo.addEventListener('click', (e) => {
  // console.log(e);
  // console.log(e.target);
  console.log('avo 1');
});

avo.addEventListener('click', (e) => {
  // console.log(e);
  // console.log(e.target);
  console.log('avo 2');
}); */

/* 
-Exemplo 02
*/

/* avo.addEventListener('click', (e) => {
  console.log('avo 1');
});

pai.addEventListener('click', (e) => {
  console.log('pai 1');
});

filho.addEventListener('click', (e) => {
  console.log('filho 1');
});

document.addEventListener('click', (e) => {
  console.log('document 1');
}); */

/* 
-Exemplo 03 - capture: true
*/

/* avo.addEventListener(
  'click',
  (e) => {
    console.log('avo capture');
  },
  { capture: true }
);

avo.addEventListener(
  'click',
  (e) => {
    console.log('avo bubble');
  },
  { capture: false }
);

pai.addEventListener(
  'click',
  (e) => {
    console.log('pai capture');
  },
  { capture: true }
);

pai.addEventListener(
  'click',
  (e) => {
    console.log('pai bubble');
  },
  { capture: false }
);

filho.addEventListener(
  'click',
  (e) => {
    console.log('filho capture');
  },
  { capture: true }
);

filho.addEventListener(
  'click',
  (e) => {
    console.log('filho bubble');
  },
  { capture: false }
);

document.addEventListener(
  'click',
  (e) => {
    console.log('document capture');
  },
  { capture: true }
);

document.addEventListener(
  'click',
  (e) => {
    console.log('document bubble');
  },
  { capture: false }
); */

/* 
-Exemplo 04: stopPropagation
*/

/* avo.addEventListener(
  'click',
  (e) => {
    console.log('avo capture');
  },
  { capture: true }
);

avo.addEventListener(
  'click',
  (e) => {
    console.log('avo bubble');
  },
  { capture: false }
);

pai.addEventListener(
  'click',
  (e) => {
    e.stopPropagation(); //! <= stopPropagation
    console.log('pai capture');
  },
  { capture: true }
);

pai.addEventListener(
  'click',
  (e) => {
    console.log('pai bubble');
  },
  { capture: false }
);

filho.addEventListener(
  'click',
  (e) => {
    console.log('filho capture');
  },
  { capture: true }
);

filho.addEventListener(
  'click',
  (e) => {
    console.log('filho bubble');
  },
  { capture: false }
);

document.addEventListener(
  'click',
  (e) => {
    console.log('document capture');
  },
  { capture: true }
);

document.addEventListener(
  'click',
  (e) => {
    console.log('document bubble');
  },
  { capture: false }
); */

/* 
Exemplo 05: once:true
*/

/* avo.addEventListener(
  'click',
  (e) => {
    console.log('avo bubble');
  },
  { capture: false }
);

pai.addEventListener(
  'click',
  (e) => {
    console.log('pai bubble');
  },
  { capture: false, once: true }
);

filho.addEventListener(
  'click',
  (e) => {
    console.log('filho bubble');
  },
  { capture: false }
); */

/* 
Exemplo 06: removeEventListener
*/

/* avo.addEventListener(
  'click',
  (e) => {
    console.log('avo bubble');
  },
  { capture: false }
);

pai.addEventListener('click', printHi);

setTimeout(() => {
  pai.removeEventListener('click', printHi);
}, 2000);

filho.addEventListener(
  'click',
  (e) => {
    console.log('filho bubble');
  },
  { capture: false }
);

function printHi() {
  console.log('Hi');
} */

/* 
-Exemplo 07a: delegação de eventos
Só com isso, não adiciona o evento na novaDiv
*/

/* const divs = document.querySelectorAll('div');

divs.forEach((div) => {
  div.addEventListener('click', () => {
    console.log('olá');
  });
});

const novaDiv = document.createElement('div');
novaDiv.style.width = '200px';
novaDiv.style.height = '200px';
novaDiv.style.backgroundColor = 'purple';
document.body.append(novaDiv); */

/* 
--Exemplo 07b: delegação de eventos

*/

/* const divs = document.querySelectorAll('div');

divs.forEach((div) => {
  div.addEventListener('click', () => {
    console.log('olá');
  });
});

const novaDiv = document.createElement('div');
novaDiv.style.width = '200px';
novaDiv.style.height = '200px';
novaDiv.style.backgroundColor = 'purple';
novaDiv.addEventListener('click', () => {
  console.log('olá');
});
document.body.append(novaDiv); */

/* 
--Exemplo 07c: delegação de eventos
Aqui vai fazer o delegation de fato.

*/

/* const divs = document.querySelectorAll('div');

document.addEventListener('click', (e) => {
  if (e.target.matches('div')) {
    console.log('olá');
  }
});

const novaDiv = document.createElement('div');
novaDiv.style.width = '200px';
novaDiv.style.height = '200px';
novaDiv.style.backgroundColor = 'purple';

document.body.append(novaDiv); */

/* 
--Exemplo 07d: delegação de eventos (COM FUNÇÃO)
Aqui vai fazer o delegation de fato.

*/

const divs = document.querySelectorAll('div');

addGlobalEventListener('click', 'div', (e) => {
  console.log('olá');
});

function addGlobalEventListener(type, selector, callback) {
  document.addEventListener(type, (e) => {
    if (e.target.matches(selector)) {
      callback(e);
    }
  });
}

const novaDiv = document.createElement('div');
novaDiv.style.width = '200px';
novaDiv.style.height = '200px';
novaDiv.style.backgroundColor = 'purple';

document.body.append(novaDiv);
