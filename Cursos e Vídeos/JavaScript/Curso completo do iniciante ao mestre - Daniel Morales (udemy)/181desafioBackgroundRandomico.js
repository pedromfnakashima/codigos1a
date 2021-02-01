/* 

*/

function getRandomNumber(inicio = 0, fim = 10, integer = true) {
  let r = Math.random() * (fim - inicio + 1) + inicio;
  return integer ? parseInt(r) : r;
}

(function () {
  let n = getRandomNumber(1, 5);
  document.body.style.backgroundImage = `url(181images/${n}.jpg)`;
})();
