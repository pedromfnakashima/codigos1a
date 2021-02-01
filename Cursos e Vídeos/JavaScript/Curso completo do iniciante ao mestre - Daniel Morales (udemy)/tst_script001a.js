/* 
Testes de closures
*/

//--- Teste 1a - funcionando

// function html_tag(tag) {
//   function wrap_text(msg) {
//     console.log('<' + tag + '>' + msg + '</' + tag + '>');
//   }
//   return wrap_text;
// }

// print_h1 = html_tag('h1');

// print_h1('Test Headline!');
// print_h1('Another Headline!');

// print_p = html_tag('p');

// print_p('Test Paragraph!');

//--- Teste 1b - template literal - funcionando

// function html_tag(tag) {
//   function wrap_text(msg) {
//     console.log(`<${tag}>${msg}</${tag}>`);
//   }
//   return wrap_text;
// }

// print_h1 = html_tag('h1');

// print_h1('Test Headline!');
// print_h1('Another Headline!');

// print_p = html_tag('p');

// print_p('Test Paragraph!');

//---- Teste 2a - Teste do logger

// function my_logger(orig_func) {
//   argumentosFora = [...arguments];

//   function wrap_text() {
//     console.log(`Função rodando com argumentos: ${argumentosFora}`);
//   }
//   return wrap_text;
// }

// my_logger('b', 'c', 'd')();

//---- Teste 2a1 - Verficando o nome da função

// function f_fora(f_input) {
//   nomeFunçãoInput = f_input.name;
//   console.log(nomeFunçãoInput);
// }

// function soma(a, b) {
//   // return a + b;
//   console.log('rodou função de dentro');
// }

// f_fora(soma);

function decorate(original, wrapper, context) {
  return function () {
    try {
      original.apply(this, arguments);
    } catch (e) {}
    try {
      wrapper.apply(context || this, arguments);
    } catch (e) {}
  };
}

function myFunction(arg1, arg2) {
  console.log('arg1 = ' + arg1 + ', arg2 = ' + arg2);
}

var newFunction = decorate(myFunction, function (arg1, arg2) {
  console.log('arg1 = ' + arg1 + ', arg2 = ' + arg2);
});

newFunction(1, 2);
