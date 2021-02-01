/* 
O que é o DOM?
É uma API disponibilizada nos browser que permite editar o que é mostrado na tela.
Formas:
 */
document.
    getElementById()
    getElementsByTagName()
    getElementsByClassName()
    querySelector()
    querySelectorAll()

// Obs.: Dentro do querySelector ou do querySelectorAll precisa passar da mesma forma como formataria com o CSS.

//- getElementById
/* 
Ex 1. (no console do Chrome):
 */
document.getElementById('título1')
document.getElementById('título1').textContent
document.getElementById('título1').textContent = 'Novo texto!!'

//- querySelector
/* 
Dentro do querySelector ou do querySelectorAll precisa passar da mesma forma como formataria com o CSS.

querySelector SEMPRE vai retornar um único objeto, o primeiro encontrado. Por isso, não se passa com ele o índice [i].

Ex 2. (no console do Chrome):
 */
document.querySelector('#título1')
document.querySelector('#título1').textContent = 'Editado com o querySelector'
document.querySelector('h1')

//- getElementsByClassName
/*
 gera algo parecido com um array (mas não é array - é array-like).  Precisa consultar passando índice da forma [i].
 
Ex 3. (no console do Chrome):
*/
document.getElementsByClassName('parágrafo2')
document.getElementsByClassName('parágrafo2')[0]
document.getElementsByClassName('parágrafo2')[1]
document.getElementsByClassName('parágrafo2')[0].textContent
document.getElementsByClassName('parágrafo2')[0].textContent = 'Editado pelo getElementsByClassName'
document.getElementsByClassName('parágrafo2')[1].textContent = 'aaaaa'

//-querySelectorAll
/*
Também gera algo parecido com um array (mas não é array - é array-like).  Dentro do querySelector ou do querySelectorAll precisa passar da mesma forma como formataria com o CSS. Precisa consultar passando índice da forma [i].

querySelectorAll SEMPRE vai retornar um objeto array-like. Por isso, se passa com ele o índice [i].

Ex 4. (no console do Chrome):
*/
document.querySelectorAll('.parágrafo2')
document.querySelectorAll('.parágrafo2')[0]
document.querySelectorAll('.parágrafo2')[1]
document.querySelectorAll('.parágrafo2')[0].textContent
document.querySelectorAll('.parágrafo2')[0].textContent = 'bbbbbb'

document.querySelectorAll('h1')[0]
document.querySelectorAll('h1')[0].textContent = 'xxxxxxxxxxxxx'

//-getElementsByTagName

/* 
Também gera algo parecido com um array (mas não é array - é array-like).
Ex 5. (no console do Chrome):
*/
document.getElementsByTagName('p')
document.getElementsByTagName('p')[0]
document.getElementsByTagName('p')[1]
document.getElementsByTagName('p')[1].textContent

//-- Colocando elementos dentro de variável
/* 
É possível colocar dentro de variável com o let e const; e depois, manipular (navegar pelo DOM) normalmente como um objeto.
Ex 6. (no console do Chrome):
*/
let teste = document.getElementById('idmain')
teste.getElementsByTagName('p')
teste.getElementsByTagName('p')[0]
teste.getElementsByTagName('p')[0].textContent = 'cccccccccc'

let h1 = document.querySelector('h1')
h1.textContent
h1.textContent = 'abcd'

//-- Pegando objetos que estão entranhados dentro do DOM com o querySelector e o querySelectorAll
/* 
querySelector SEMPRE vai retornar um único objeto, o primeiro encontrado. Por isso, não se passa com ele o índice [i].
Ex 7. (no console do Chrome):
*/
document.querySelector('#idmain p')
document.querySelector('#idmain p').textContent
document.querySelector('#idmain p').textContent = 'ddddddddddd'

/* 
querySelectorAll SEMPRE vai retornar um objeto array-like. Por isso, se passa com ele o índice [i].
Ex 8. (no console do Chrome):
*/
document.querySelectorAll('#idsection p')
document.querySelectorAll('#idsection p')[0]
document.querySelectorAll('#idsection p')[0].textContent = 'eeeeeeeee'



document.querySelector('h1').textContent = 'editado com JS'













