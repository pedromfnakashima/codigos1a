/* 

























Testes....
*/

// const paragrafos = document.querySelectorAll('.card p');
// // const originTexts = Array.from(paragrafos).map((p) => p.textContent);
// const originTexts = Array.from(paragrafos).map((p) => p.innerText);

(function () {
  const paragrafos = Array.from(document.querySelectorAll('.card p'));
  const originTexts = paragrafos.map((p) => p.innerText);
  const maxLength = 100;

  paragrafos.forEach((p, i) => {
    if (p.innerText.length > maxLength) {
      p.textContent = p.innerText.substring(0, maxLength) + '...'; // obs: professor coloclou innerHTML

      const btn = document.createElement('button');
      btn.innerHTML = '<i class="fas fa-chevron-down"></i>';
      p.parentElement.classList.add('text.hidden');

      // btn.addEventListener('click', toggleText);
      btn.addEventListener('click', function (e) {
        toggleText(e, p, i);
      });

      p.parentElement.appendChild(btn);
    }
  });

  function toggleText(e, p, i) {
    console.log('e.currentTarget :>> ', e.currentTarget);
    console.log('this :>> ', this);
    const card = e.currentTarget.parentElement;

    card.classList.toggle('text-hidden');
    e.currentTarget.querySelector('i').classList.toggle('fa-chevron-down');
    e.currentTarget.querySelector('i').classList.toggle('fa-chevron-up');

    if (card.classList.contains('text-hidden')) {
      card.querySelector('p').textContent =
        originTexts[i].substring(0, maxLength) + '...'; // poderia ter usado o parâmetro p, que é o meu parágrafo
    } else {
      card.querySelector('p').textContent = originTexts[i]; // poderia ter usado o parâmetro p, que é o meu parágrafo
    }
  }
})();
