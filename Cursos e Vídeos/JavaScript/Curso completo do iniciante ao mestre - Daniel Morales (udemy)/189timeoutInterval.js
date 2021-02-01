/* 

setTimeout(fn, ms)
setInterval(fn, ms)
clearTimeout(id)
clearInterval(id)

- O JavaScript é Single Thread.

! Implicação: um processo por vez é executado (e não dois processos concorrentes).

Ex.:

setTimeout em 10 ms
CÓDIGO PRINCIPAL (20 ms p/ ser executado)
{
setTimeout dispara
}
setTimeout executado

Explicação (189 - 15:50)





*/

const tempoInicio = Date.now();

let n = 0;

// setTimeout(function () {
//   console.log('timeout depois de 2000 ms.');
//   const tempoFinal = Date.now();
//   console.log('tempoFinal - tempoInicio :>> ', tempoFinal - tempoInicio);
// }, 2000);

let str = '';
var d = document.querySelector('div');

setTimeout(function () {
  for (let i = 0; i < 1000; i++) {
    str += ` i: ${i} --`;
    d.textContent += str;
  }
}, 3000);

const intervalo = setInterval(function () {
  console.log(`interval n (n++) :>> ${n++} segundos.`);
  if (n > 10) {
    clearInterval(intervalo);
    const tempoFinal = Date.now();
    console.log(
      `tempoFinal - tempoInicio :>> , ${
        tempoFinal - tempoInicio
      } milissegundos.`
    );
  }
}, 1000);
