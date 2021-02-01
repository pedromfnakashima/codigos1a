/* 

*/

// classe viva
// const bodyFx = document.getElementsByClassName('fx');
// console.log('bodyFx :>> ', bodyFx);

(function () {
  const bodyFx = document.getElementsByClassName('fx');
  // console.log('bodyFx :>> ', bodyFx);

  window.addEventListener('scroll', function () {
    // console.log('pageYOffset :>> ', pageYOffset);
    if (pageYOffset > 250 && !bodyFx[0]) {
      console.log('adiciona classe fx');
      document.body.classList.add('fx');
    } else if (pageYOffset <= 250 && bodyFx[0]) {
      console.log('remove classe fx');
      document.body.classList.remove('fx');
    }
  });
})();
