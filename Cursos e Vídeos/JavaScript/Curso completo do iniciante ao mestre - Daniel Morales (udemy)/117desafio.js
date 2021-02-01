/* 

TAREFAS DO DESAFIO:

// 1. Crie um nova li com texto "item 2" e a inclua na ul de div com class .alvo

// 2. Mova a última li de original para alvo (mas antes da primeira li). Em outras palavras, a última li da original deve virar a primeira li de alvo

// 3. Altere o texto da primeira li de .alvo para "item 0"

// 4. Clone a ul de .original e a inclua na primeira li de .alvo

// 5. Remova a ultima li (item2) da lista inserida na etapa anterior

// 6. Remova as duas li's que sobraram na ul original


 */

const ulAlvo = document.querySelector('.alvo ul')
const ulOriginal = document.querySelector('.original ul')

//- 1. Crie um nova li com texto "item 2" e a inclua na ul de div com class .alvo

const li = document.createElement('li')
li.textContent = 'item 2'

ulAlvo.appendChild(li)

//- 2. Mova a última li de original para alvo (mas antes da primeira li). Em outras palavras, a última li da original deve virar a primeira li de alvo
// SINTAXE: nó_pai.insertBefore(elemento_inserido, referência)
ulAlvo.insertBefore(ulOriginal.lastElementChild, ulAlvo.firstElementChild)

//- 3. Altere o texto da primeira li de .alvo para "item 0"
// obs.: também pode ser feito com .firstChildElement()

// console.log(ulAlvo.children)
// console.log(ulAlvo.children[0])

ulAlvo.children[0].textContent = 'item 0'

//- 4. Clone a ul de .original e a inclua na primeira li de .alvo

const ulClone = ulOriginal.cloneNode(true)

ulAlvo.firstElementChild.appendChild(ulClone)

//- 5. Remova a ultima li (item2) da lista inserida na etapa anterior

// console.log(ulClone)

ulClone.removeChild(ulClone.lastElementChild)

//- 6. Remova as duas li's que sobraram na ul original

ulOriginal.innerHTML = ''

