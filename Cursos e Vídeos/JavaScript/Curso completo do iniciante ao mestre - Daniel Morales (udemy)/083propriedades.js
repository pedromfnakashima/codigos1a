/* 
ACESSANDO VALORES DAS PROPRIEDADES.
Nem sempre haverá equivalência "nome da propriedade no html" <=> "nome da propriedade no JS"

! Regra geral 1: propriedade no html tem duas palavras (é palavra composta; ex. 1: readonly; ex. 2: maxlength) => propriedade no JS escrito no padrão Camel Case (ex.:javaScript)

! Regra geral 2: palavra reservada no JS
Ex. 1: (for) => htmlFor
Ex. 2: (class) => className

Nome da propriedade no HTML => acesso no JS
- Valor do campo (digitado pelo usuário)
-- HTML: value => JS: value
- Atributo readonly do campo
-- HTML: readonly => JS: readOnly
- Atributo maxlength do campo
-- HTML: maxlength => JS: maxLength
- Atributo for do label
-- HTML: for="" => JS: htmlFor
- Classe do elemento
-- HTML: class="" => JS: className
*/

//- Nome da propriedade no HTML == Nome no JS
const txtNome = document.querySelector('#txtNome')

//-- Setando no HTML
txtNome.value = 'Pedro'
txtNome.disabled = true

//-- Acessando o valor
console.log(`Atributo no HTML: value => Acesso no JS: ${txtNome.value}`)

//- Nome da propriedade no HTML != Nome no JS
const txtEmail = document.querySelector('#txtEmail')
const labelContrato = document.querySelector('label[for="contrato"]')

//-- Setando no HTML
//--- Palavra composta no HTML
txtEmail.readOnly = true

//-- Acessando o valor

//--- Palavra composta no HTML

console.log(`Atributo no HTML:maxlength => Acesso no JS: ${txtEmail.maxLength}`)
console.log(`Atributo no HTML:readonly => Acesso no JS: ${txtEmail.readOnly}`)

//--- Palavra reservada no JS
console.log(`Atributo no HTML:for => Acesso no JS: ${labelContrato.htmlFor}`)
console.log(`Atributo no HTML:class => Acesso no JS: ${txtEmail.className}`)








