/* 

*/

(function () {
  window.addEventListener('scroll', destacaMenu);

  const menu = document.querySelector('.nav');
  const links = menu.querySelectorAll('li a');

  function destacaMenu() {
    let positions = [...links].map((link) => {
      // console.log('link :>> ', link);
      // console.log('link.href :>> ', link.href);
      // console.log('link.getAttribute("href") :>> ', link.getAttribute('href'));
      // console.log(
      //   'document.querySelector(link.getAttribute("href")) :>> ',
      //   document.querySelector(link.getAttribute('href'))
      // );
      // console.log('----');

      let href = link.getAttribute('href');
      let h2 = document.querySelector(href);
      return h2.getBoundingClientRect().top;
    });

    let linkAtivo = pegaUltimoElementoVisto(positions);
    let menuActived = menu.querySelector('.actived');
    if (menuActived) {
      menuActived.classList.remove('actived');
    }
    if (linkAtivo) {
      return linkAtivo.classList.add('actived');
    }
    return links[0].classList.add('actived');
  }

  function pegaUltimoElementoVisto(_positions) {
    // let positions = _positions.filter((n) => n < 100);
    let positions = _positions.filter((n) => n < innerHeight / 2); //! <= diz que, a partir do momento que o título2 estiver no momento da viewport, já marca (muda a classe)
    // console.log('positions.pop() :>> ', positions.pop()); //! array.pop é destrutivo, mesmo no console; deve estar comentado p/ o código funcionar
    return links[positions.length - 1];
  }

  destacaMenu();
})();
