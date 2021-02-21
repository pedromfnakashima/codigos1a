/* 



*/

/* Não robusto a tags */

// document.querySelector('input').addEventListener('input', (e) => {
//   const valor = e.target.value;

//   Array.from(document.querySelectorAll('p')).map((paragraph) => {
//     const paragraphText = paragraph.innerText;
//     const regex = new RegExp(valor, 'gi');
//     const htmlReplaced = paragraphText.replace(regex, (result) => {
//       return `<span class="hgt">${result}</span>`;
//     });
//     paragraph.innerHTML = htmlReplaced;
//   });
// });

/* Robusto a tags */

const paragraphsOrigins = Array.from(document.querySelectorAll('p')).map(
  (p) => p.innerHTML
);

document.querySelector('input').addEventListener('input', (e) => {
  const valor = e.target.value;

  Array.from(document.querySelectorAll('p')).map((paragraph, i) => {
    const paragraphHTML = paragraphsOrigins[i];
    if (valor) {
      const regex = new RegExp(valor, 'gi');
      const htmlReplaced = paragraphHTML.replace(regex, (result) => {
        return `<span class="hgt">${result}</span>`;
      });
      paragraph.innerHTML = htmlReplaced;
    } else {
      paragraph.innerHTML = paragraphHTML;
    }
  });
});
