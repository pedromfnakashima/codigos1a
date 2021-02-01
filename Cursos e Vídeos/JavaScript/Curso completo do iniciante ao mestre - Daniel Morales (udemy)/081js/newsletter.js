

const txtEmail = document.getElementById('txtEmail')
// txtEmail, no momento em que o código é executado, é vazio. No entanto, o momento em que eu quero recuperar o valor, é o momento em que o usuário clicar no botão.

const msgFeedback = document.getElementById('newsletterFeedback')

// let email = txtEmail.value
/* 
No momento em que o JS é parseado pelo browser, email recebe o valor padrão. Se não há, recebe uma string vazia ''.
Para resolver esse problema, definimos a variável email dentro da função cadastrarEmail
*/

function cadastrarEmail() {
    // console.log('cadastrar email')
    let email = txtEmail.value
    msgFeedback.innerHTML = `O email ${email} foi cadastrado com sucesso`
}


