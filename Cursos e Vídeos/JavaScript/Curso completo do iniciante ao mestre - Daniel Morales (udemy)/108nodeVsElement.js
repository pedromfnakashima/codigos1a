

/* 
###################################################################
Node vs. Element
###################################################################

Há 12 tipos diferentes de "nós" no DOM HTML (elemento, atributo, texto, comentário, etc).
Um elemento é só um tipo específico de nó.

###################################################################
-NAVEGAR ENTRE NÓS:
###################################################################

Node.
    parentNode
    parentElement
    nextSibling
    previousSibling

Node.
    childNodes
    children
    firstChild
    firstElementChild
    lastChild
    lastElementChild
    hasChildNodes()

################################################################
-ADICIONAR NÓS <= depois de ser criado (faz com que, efetivamente, fique visível para o usuário)
################################################################

ParentNode.
    prepend()
    append()

Node.
    appendChild()
    insertBefore()
    cloneNode()

ChildNode.
    after()
    before()

Element.
    insertAdjacentElement()
    insertAdjacenHTML()
    insertAdjacentText()

##############################################################
-REMOVER NÓS
##############################################################
Node.
    replaceChild()
    removeChild()

ChildNode.
    remove() <= não funciona no ie

##############################################################
-CRIAR NÓS <= não faz automaticamente que seja visível para o usuário. É necessário adicionar ao document
##############################################################

document.
    createElement()
    createAttribute()
    createTextNode()
    write()

##############################################################


*/

//- parentElement e parentNode
//-- apontando para o mesmo objeto
// O objeto document tem um atalho para acessar o body
// console.log(document.body)
// console.log(document.body.parentElement)
// console.log(document.body.parentNode)

// console.log(document.body.parentElement === document.body.parentNode) // true (apontam para o mesmo objeto, o HTML)

//-- apontando para objetos diferentes

// const html = document.body.parentElement
// console.log(html.parentElement) // null; pois o objeto html não tem um elemento pai; html não tem um pai do tipo que seja um element, só tem um pai que seja do tipo document
// console.log(html.parentNode) // document; o objeto html tem um nó pai, que é do tipo document; nó do tipo document não é um nó do tipo element

//! obs: fragmento => tb faz com que parentNode e parentElement sejam diferentes

//- nextSibling e previousSibling
/* 
Servem para navegar entre irmãos
*/

// const h2 = document.querySelector('h2')
// console.log(h2.nextSibling) // um enter (texto)
// console.log(h2.nextElementSibling) // ul
// console.log(h2.previousSibling) // dois enters
// console.log(h2.previousElementSibling) // <p>teste2</p>

// const h2NextSibling = h2.nextElementSibling
// h2NextSibling.style.backgroundColor = 'yellow' // pinta a ul de amarelo

//- children e childNodes
/* 
children: sempre retorna apenas os nós que são do tipo element
childNodes: sempre retorna todos os nós, independentemente se for do tipo element ou não

*/
// const link = document.querySelector('a')
// const list = document.querySelector('ul ul') // seleciona a ul de dentro

// console.log(link)
// console.log(list)

// console.log(list.childNodes) // coleção c/ 7 elementos; todos os nós abaixo, incluindo quebras de linhas, comentários
// console.log(list.children) // coleção c/ 3 elementos, todos nós do do tipo element; 

// console.log(link.parentElement.childNodes) // coleção c/ 3 elementos;
/* 
Os 3 elementos da coleção acima:
Texto 1: aaaaaaaa
a: link
Texto 2: bbbbbb
*/

// console.log(link.parentElement.childNodes[0].textContent)
// console.log(link.parentElement.childNodes[2].textContent)
// console.log(link.parentElement.children) // coleção c/ 1 elemento (a); 

//- firstChild, firstElementChild, lastChild, lastElementChild, hasChildNodes
/* 
firstChild: retorna o primeiro nó.
firstElementChild: retorna o primeiro nó que é do tipo element.
lastChild: retorna o último nó.
lastElementChild(): retorna o último nó que é do tipo element.
hasChildNodes: verifica se o elemento que você tá buscando tem nó ou não.
*/

//-- firstChild, firstElementChild, lastChild, lastElementChild
// const link = document.querySelector('a')

// console.log(link.parentElement.firstChild) // aaaa; é o primeiro nó
// console.log(link.parentElement.firstElementChild) // <a></a> é o primeiro nó do tipo element; obs.: só há um único filho que é do tipo element.


// console.log(link.parentElement.lastChild) // bbbbbb; é o último nó
// console.log(link.parentElement.lastElementChild) // <a></a> é o último nó do tipo element; obs.: só há um único filho que é do tipo element.

//-- hasChildNodes()
// const list = document.querySelector('ul ul')
/* Abaixo, pegaremos a úlima li, que está vazia */
// console.log(list.lastElementChild.hasChildNodes()) // false; se colocar um texto, passa a ser true; se colocar um enter ou mesmo um comentário, já passa a ser true

// console.log(list.lastElementChild) // <li> </li>
// console.log(list.lastElementChild.childNodes) //--- objeto nodelist <= cliando, é possível ver todas as propriedades
// obs.: __proto__ retorna o tipo de objeto
// console.log(list.lastElementChild.childNodes.__proto__) // NodeList
// console.log(list.lastElementChild.childNodes[0]) // <!-- comentário aqui -->
// console.log(list.lastElementChild.childNodes[0].textContent) // comentário aqui
// console.log(list.lastElementChild.childNodes[0].baseURI) // 
// console.log(list.lastElementChild.childNodes[0].data) // 
// console.log(list.lastElementChild.childNodes[0].parentNode) // 
// console.log(list.lastElementChild.childNodes[0].nodeType) // 8; código do comentário

//- Cria elementos no DOM (criar nós)
/* 
createElement: 



*/

//-- Cria o elemento do tipo h1 (título)
const título = document.createElement('h1')
// console.log(title) // já é possível ver no console, apesar de não existir ainda no DOM

//-- Adiciona atributo - forma 1

//--- Cria o atributo (atributo)
const atributo = document.createAttribute('id')

//--- Define o valor para o atributo (título1)
atributo.value = 'título1'

//--- Vincula o atributo criado (atributo) ao elemento criado (título)
título.setAttributeNode(atributo)
// console.log(título) // o título já está com o atributo id="título1"

//-- Cria um nó do tipo texto, e coloca dentro de h1
// const texto = document.createTextNode('criar nós no DOM')
// título.appendChild(texto)
// console.log(título) // o título já está com o texto

//-- Adiciona atributo ou texto - forma 2 (menos verboso)
título.setAttribute('title', 'title inserido dinamicamente')
título.setAttribute('style', 'color:red;')
// obs.: existe uma forma específica de adicionar style, mas dá pra colocar assim também
// console.log(título) // o título já está com os atributos title e style, assim como seus valores

título.textContent = 'texto inserido com textContent'
// console.log(título) // o título já está com o novo texto

//- ADICIONA nó no documento (torna visível para o usuário) e MOVE também

//-- appendChild - insere no final do elemento de referência

//--- Insere no final do documento
// document.body.appendChild(título)

//--- Insere no final da div container
// document.querySelector('.container').appendChild(título)

//-- append e prepend
/* 
Vantagens:
. Aceitam um segundo parâmetro um nó (que pode ser texto) que será inserido depois

! obs.: não funcionam no ie
*/
//--- Insere no final da div container, depois do último filho
// document.querySelector('.container').append(título)
// document.querySelector('.container').append(título, 'texto novo')

//--- Insere no início da div container, antes do primeiro filho
// document.querySelector('.container').prepend(título)
// document.querySelector('.container').prepend(título, 'texto novo')

//-- insertBefore
/* 
Recebe dois parâmetros:
. filho novo
. nó de referência
*/
const título2 = document.createElement('h1')
título2.textContent = 'título 2 -------------------------------------'

/* 
Abaixo,
Insere título 2 antes da ul (logo depois de "Lista")
*/

// Menos organizado:
// document.querySelector('.container').insertBefore(título2, document.querySelector('ul'))

// Mais organizado:
const listaDeFora = document.querySelector('ul') //--- <<=== a referência
// document.querySelector('.container').insertBefore(título2, listaDeFora)

//! Inserindo no começo da div container de forma que o ie11 entenda (com o mesmo efeito do prepend)
// const container = document.querySelector('.container')
// container.insertBefore(título2, container.firstChild)
// container.insertBefore(título2, listaDeFora)

/* 
!! IMPORTANTE (8:15): mover vs. criar cópia (clonar nó)
Quando vc manipula um elemento que já se encontra no DOM (appendChild, insertBefore, ..), vc ta movendo ele de lugar. 
--- Movendo:
Exemplo 1.
*/

const container = document.querySelector('.container')

// container.insertBefore(título2, listaDeFora)
// container.insertBefore(título2, container.firstChild)

/* 
//--- Movendo a lista de dentro:
Abaixo, vamos MOVER a ul de dentro e colocar logo pra depois do <h2>Lista</h2>
*/

const listaDeDentro = document.querySelector('ul ul')
const h2 = document.querySelector('h2') // <= o próximo sibling de h2 será a referência

// container.insertBefore(listaDeDentro, h2.nextElementSibling) //! Move node

/* 
--- Criando um clone de listaDeDentro, e movendo o clone:
Sintaxe:
nó.cloneNode(true)
Abaixo, vamos CLONAR a ul de dentro e colocar logo pra depois do <h2>Lista</h2>
*/

const listaDeDentroClone = listaDeDentro.cloneNode(true) // o TRUE faz com que todos os filhos de ul (que estão dentro de ul) também sejam clonados

container.insertBefore(listaDeDentroClone, h2.nextElementSibling) //! Move o clone do node

//-- after e before
/* 
Acessados a partir do filho.
Não funcionam no ie.
Aceitam 2 parâmetros.
Aceitam tanto TEXTO quanto NÓ.

Vamos acessar o seguinte parágrafo (para servir de referência):
<p>aaaaaaaa <a href="#">link</a> bbbbbb </p>

*/
const span1 = document.createElement('span')
span1.textContent = 'span dinâmica, inserida com after/before'

const segundoParágrafo = container.firstElementChild.nextElementSibling
// console.log(segundoParágrafo)

// segundoParágrafo.after('texto inserido com o after') //! insere texto
// segundoParágrafo.after('texto inserido com o after',' --> outro texto') //! insere texto

// segundoParágrafo.after(span1) //! insere nó DEPOIS de segundoParágrafo
// segundoParágrafo.before(span1) //! insere nó ANTES de segundoParágrafo

//-- insertAdjacent...()
/* 
Primeiro parâmetro: posição que eu quero inserir;
Segundo parâmetro: o que eu quero inserir.

Posições (SEGUNDO PARÂMETRO):
beforebegin: insere antes da div class="container2"
afterbegin: insere 
beforeend: insere 
afterend: insere 

PRIMEIRO PARÂMETRO: string com código HTML

*/

const container2 = document.querySelector('.container2')

//--- insertAdjacentHTML()

// container2.insertAdjacentHTML('beforebegin', '<b> TEXTO INSERIDO 1 </b>')
// container2.insertAdjacentHTML('afterbegin', '<b> TEXTO INSERIDO 2</b>')
// container2.insertAdjacentHTML('beforeend', '<b> TEXTO INSERIDO 3</b>')
// container2.insertAdjacentHTML('afterend', '<b> TEXTO INSERIDO 4</b>')

//--- insertAdjacentText()

// container2.insertAdjacentText('beforebegin', '<b> não renderiza HTML 1 </b>')
// container2.insertAdjacentText('afterbegin', '<b> não renderiza HTML</b>')
// container2.insertAdjacentText('beforeend', '<b> não renderiza HTML 3</b>')
// container2.insertAdjacentText('afterend', '<b> não renderiza HTML 4</b>')

//!! CUIDADO: por questão de segurança, nunca insira DIRETAMENTE um código no segundo argumento um código que venha da interface do usuário, ou de um banco de dados. Deve tratar antes.

//--- insertAdjacentElement() <- precisa criar um nó antes

const textoÊnfase = document.createElement('em')
textoÊnfase.textContent = 'texto com ênfase inserido com insertAdjacentElement'

// container2.insertAdjacentElement('beforeend', textoÊnfase)

//- REMOVE nó do documento (torna visível para o usuário) e move também
/* 

Abaixo, vamos remover a lista maior (listaDeFora), de fora.

MÉTODOS. elementoAserRemovido.
.remove() - não funciona no IE11.
.parentElement.removeChild(elementoAserRemovido) - funciona no IE11.
.replaceChild()

*/

//--- 2 formas de remover elemento
// Forma 1: usando o .remove() (não funciona no IE11)
// listaDeFora.remove() //! remove nó

// Forma 2: acessa o pai, e partir do pai remove a lista; não precisa nem saber quem é o pai (funciona no IE11)
// listaDeFora.parentElement.removeChild(listaDeFora) //! remove nó

//--- 
/* 
Acessado a partir do pai.
Abaixo, vamos selecionar o h1, e substituir pelo título2.
A partir do pai, vamos dar um replaceChild no primeiro filho (h1).
*/

const pai = document.body

// const novoFilho = container.querySelector('p') //! move o original
const novoFilho = container.querySelector('p').cloneNode(true) //! move o clone
const velhoFilho = document.querySelector('h1')

pai.replaceChild(novoFilho, velhoFilho) //! substitui nó. IMPORTANTE: COMO novoFilho já estava no DOM, ele foi, na verdade, foi MOVIDO. Se não quisesse mover o orignal, mas um CLONE, deveria definir com o .cloneNode(true) [const novoFilho = container.querySelector('p').cloneNode(true)]


