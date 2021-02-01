/* 

O 'input' é o melhor p/ captar entradas. É 'alterei um dado', NÃO IMPORTA se é digitando, seja no ctrl c ctrl v, seja cliando com  o botão direito do mouse e colar.

No caso dos eventos de TECLADO, de 'keypress', 'keydown' e 'keyup', o 'keyup' é o único que consegue mostrar o valor atualizado.

Diferença entre o 'keydown' e o 'keypress':
Se eu pressionar, por exemplo, ESC, apenas o evento 'keydown' é escutado; o 'keypress' não é escutado. Outros exemplos, 'SHIFT', 'CTRL'...
O 'keypress' só é disparado em caracteres alfanuméricos.
*/

const msg = document.getElementById('msg');

function keypress(e) {
  console.log('keypress');
  console.log(this.value); // this=elemento ao qual foi atrelado o evento
}
function keydown(e) {
  console.log('keydown');
  console.log(this.value); // this=elemento ao qual foi atrelado o evento
}

function keyup(e) {
  //! é o único que consegue mostrar o valor atualizado
  console.log('keyup');
  console.log(this.value); // this=elemento ao qual foi atrelado o evento
}
msg.addEventListener('keypress', keypress);
msg.addEventListener('keyup', keyup);
msg.addEventListener('keydown', keydown);
