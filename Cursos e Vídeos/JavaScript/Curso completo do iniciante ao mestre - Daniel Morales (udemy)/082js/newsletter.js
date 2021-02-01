/* 
TAREFAS
-Acrescentar evento de clique no botão editar, tirar o disable.
-Quando clicar fora, voltar com o disable no input

ETAPAS
-Acrescentar evento de clique no botão editar, tirar o disable.
-- Colocar o atributo onclick="editarEmail()" no button
-- Pegar o elemento id="txtEmail" do DOM, colocado na variável txtEmail, e remover o atributo disable, setando o atributo txtEmail.disabled para false, da seguinte forma: txtEmail.disabled = false
-Quando clicar fora, voltar com o disable no input
-- Colocar o atributo onblur="disableEmail()" no input
-- Pegar o elemento id="txtEmail" do DOM, colocado na variável txtEmail, e remover o atributo disable, setando o atributo txtEmail.disabled para false, da seguinte forma: txtEmail.disabled = true

*/

const txtEmail = document.getElementById("txtEmail")

function editarEmail() {
    txtEmail.disabled = false
    // a opção abaixo faz já colocar o foco no campo quando clica
    txtEmail.focus()

}

function disableEmail() {
    txtEmail.disabled = true
}








