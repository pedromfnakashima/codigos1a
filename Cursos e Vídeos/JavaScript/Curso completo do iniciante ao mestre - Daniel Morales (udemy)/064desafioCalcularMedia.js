
/* 
Construir uma função para calcular a média
Requisitos:
Pode receber um ou mais valores numéricos;
Deve retornar um único número;
Deve gerar um erro se receber um parâmetro não número;
Deve retornar zero caso não receba nenhum parâmetro.
Exemplos:
calcularMedia() // 0
calcularMedia(2,6) // 4
calcularMedia(2,6,1,1,2,6) // 3
calcularMedia('2','6') // Error

Conta que faz entrevistas.

*/

(function () {
    function calcularMedia() {
        let total = 0
        let qtd =  arguments.length
        for (let i=0; i<qtd; i+=1) {
            if (typeof arguments[i] !== 'number') {
                throw Error('Apenas números!')
            }
            total += arguments[i]
        }
        // Curto circuito: A linha abaixo diz que se for not a number, ou false, ou zero, retorna 0
        return (total / qtd) || 0

    }

    // let média = calcularMedia(2,4,6)
    // let média = calcularMedia(2,'4',6)
    // let média = calcularMedia(2,4,[6,1,2,5])
    let média = calcularMedia()
    console.log(média)

})()



