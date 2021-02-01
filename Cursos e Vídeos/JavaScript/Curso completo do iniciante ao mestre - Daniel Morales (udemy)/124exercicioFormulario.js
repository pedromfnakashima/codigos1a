/* 
no Chrome , inspecionar console, engrenagem (devTools) => 'Preserve log' impede que quando carrega a página limpe o histórico
*/

(function () {
  'use strict';

  const txtTitulo = document.getElementById('txtTitulo');
  const btn = document.getElementById('btn');
  //-- Faz com que a função ocorra não no click do usuário, mas no submit. Nesse caso, o ENTER vai ser sempre equivalente a clicar no submit.
  const formCadastro = document.querySelector('.formCadastro');

  //- função mostrarMensagemDeErro(), que é usada no VALIDADOR DO TÍTULO <- substitui o alert('Preencha todos os campos');
  // div feedbackMessage:
  const feedbackMessage = document.getElementById('feedbackMessage');
  //botão de dentro da div feedbackMessage
  const feedbackMessageCloseBtn = feedbackMessage.getElementsByTagName(
    'button'
  )[0];

  function mostrarMensagemDeErro(msg, cb) {
    // alert(msg); // teste
    //-- adiciona a classe 'show'
    feedbackMessage.classList.add('show');
    //-- modifica o texto do parágrafo que tá dentro de feedbackMessage; como retorna htmlcollection, tem que pegar o primeiro elemento com [0]
    feedbackMessage.getElementsByTagName('p')[0].textContent = msg;

    //-- coloca o focus no botão de fechar X (permite que, com um ENTER, o usuário feche)
    // console.log('feedbackMessageCloseBtn: ', feedbackMessageCloseBtn);
    feedbackMessageCloseBtn.focus();

    //-- faz com que, sempre que a função mostrarMensagemDeErro for executada, adiciona um outro eventListener no botão;
    //!! atenção: NÃO É POSSÍVEL remover listener quando utiliza-se função anônima; para ser possível remover o listener, é preciso passar função nomeada

    function ocultarMensagemDeErro() {
      console.log(
        'clicou no X do fechar, button de dentro da div feedbackMessage'
      );
      feedbackMessage.classList.remove('show');

      feedbackMessageCloseBtn.removeEventListener(
        'click',
        ocultarMensagemDeErro
      );
      feedbackMessageCloseBtn.removeEventListener('keyup', apertouTecladoNoBTN);

      if (typeof cb === 'function') {
        //! se for uma função, executa
        cb();
      }
    }

    feedbackMessageCloseBtn.addEventListener('click', ocultarMensagemDeErro);

    //-- permite que o usuário faça desaparecer a div feedbackMessage com o botão ESC

    function apertouTecladoNoBTN(e) {
      // console.log('e.keyCode', e.keyCode); //! 27 qual tecla foi digitada (+ cross-browser).
      // console.log('e.key', e.key); //! Escape qual tecla foi digitada.
      // console.log('e', e); //! objeto e
      if (e.keyCode === 27) {
        ocultarMensagemDeErro();
      }
    }

    feedbackMessageCloseBtn.addEventListener('keyup', apertouTecladoNoBTN);
  }

  //-- eventListener que faz 'fechar' a mensagem de alerta, que é a div de id feedbackMessage; na prática, faz desaparecer a classe show da div feedbackMessage
  feedbackMessageCloseBtn.addEventListener('click', function () {
    feedbackMessage.classList.remove('show');
  });

  //- VALIDADOR DO TÍTULO (se não é vazio)
  formCadastro.addEventListener('submit', function (e) {
    // console.log(txtTitulo.value);
    if (!txtTitulo.value) {
      // se for string vazia, é avaliado como false
      // alert('Preencha todos os campos'); // teste
      //!! na função abaixo, recebe uma string, e uma função de callback, que fará dar o foco em título depois que o usuário clicar no X para fechar; a função passada só é executada dentro da função de fora (mostrarMensagemDeErro), quando clicar no botão de fechar.
      mostrarMensagemDeErro('Preencha todos os campos', function () {
        //-- Quando não digitar informação, aparecer o alert, clicar em ok, colocar o foco no input:
        txtTitulo.focus();
      });

      //-- Impede o comportamento-padrão do browser, de navegar p/ o alvo:
      e.preventDefault();
    }
  });

  // btn.addEventListener('click', function (e) {
  // });
  //- Contador
  const txtDescricao = document.getElementById('txtDescricao');
  const contadorContainer = document.getElementById('contador'); //! objetivo: remover o display:None
  const resta = contadorContainer.getElementsByTagName('span')[0]; //! objetivo: acesso à span de dentro do contador; como retorna htmlcollection (mesmo que exista apenas 1 span), colocamos o índice [0]
  const maxima = txtDescricao.maxLength; //! objetivo: acesso ao atributo maxlength de txtDescricao

  function mostrarNumero(n) {
    resta.textContent = n;
  }

  // resta.textContent = maxima;
  mostrarNumero(maxima);

  //-- remove o style que tem o display:None (na prática, faz reaparecer o "255 caracteres")
  // contadorContainer.removeAttribute('style'); //--- forma 1
  contadorContainer.style.display = 'block'; //--- forma 2

  //-- capta a entrada de dados no formulário -> será usado do 'input' (dispara sempre que ocorrer uma alteração no input); Possibilidade de copiar e colar com o botão direito do mouse (nesse caso, somente o input é disparado - não são disparados o 'keyup', 'keydown' e 'keypress');

  function checkLength() {
    // console.log('input');
    //-- pega o length do value do texto que foi digitado no campo; como está usando function expression, o 'this' vai ser o elemento ao qual foi atrelado o evento; assim, o 'this' é txtDescricao
    let numeroLetrasDigitadas = this.value.length;
    let caractersRestantes = parseInt(maxima) - parseInt(numeroLetrasDigitadas);
    // resta.textContent = caractersRestantes;
    mostrarNumero(caractersRestantes);
  }

  txtDescricao.addEventListener('input', checkLength);

  //- Desabilitar o botão "Adicionar", e só habilitar quando o usuário marcar 'Comprometo-me a entregar esta tarefa o quanto antes'.
  btn.disabled = true;

  const chkAceito = document.getElementById('chkAceito');

  chkAceito.addEventListener('change', function () {
    btn.disabled = !this.checked; // ! recebe o oposto do chkAceito
  });

  //- Ao invés de usar o alert (quando o usuário tenta enviar sem nenhum dado),
})();
