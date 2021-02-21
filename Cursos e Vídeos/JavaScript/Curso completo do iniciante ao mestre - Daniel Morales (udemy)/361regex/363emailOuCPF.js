/* 
Aula 363 a 364 - desafio: email ou CPF

Identificar se o usuário digitou um email válido ou um CPF válido.
Inicialmente, o botão está desabilitado. Se o usuário digitou um e-mail
válido ou um cpf válido, o botão tem que ser habilitado.

Site de regex para prototipação:
https://regexr.com/

*/

const text = document.getElementById('input');
const btn = document.getElementById('btn');

const regexCPF = /^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$/;
const regexEmail = /^[\w.-]+@[\w.-]+\.[\w]{2,}/;

text.addEventListener('input', (e) => {
  const valor = e.target.value;
  // console.log('é CPF?', regexCPF.test(valor));
  // console.log('é email?', regexEmail.test(valor));
  /* A expressão abaixo */
  // if (regexCPF.test(valor) || regexEmail.test(valor)) {
  //   btn.disabled = false;
  // } else {
  //   btn.disabled = true;
  // }
  /* é equivalente a: */
  btn.disabled = !(regexCPF.test(valor) || regexEmail.test(valor));
});
