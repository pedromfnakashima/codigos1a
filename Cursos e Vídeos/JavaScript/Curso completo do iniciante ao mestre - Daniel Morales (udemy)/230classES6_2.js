/* 
230. Por que métodos ficam no protótipo?
é melhor assim, porque se forem colocados nos objetos, ocupa muita memória, e o código se torna menos performático.

Factories.
Função construtora
Getter e setter.
*/

const cachorroProto = {
  latir() {
    console.log(`${this.name} está latindo`);
  },
  andar(distancia) {
    this.posicao += distancia;
    console.log(`${this.name} andou ${distancia} m.`);
  },
};

function criarCachorro(name) {
  let posicao = 0;

  const obj = {
    name,
    get posicao() {
      console.log(`A posição atual de ${this.name} é ${posicao} m.`);
      return posicao;
    },
    set posicao(newPosition) {
      console.log(`A nova posição de ${this.name} é ${newPosition} m.`);
      posicao = newPosition;
    },
  };

  Object.setPrototypeOf(obj, cachorroProto);

  return obj;
}

let dog1 = criarCachorro('cachorro 1');
let dog2 = criarCachorro('cachorro 2');

console.log('dog1.posicao :>> ', dog1.posicao);
console.log('dog1.andar(12) :>> ', dog1.andar(12));
console.log('dog1.posicao :>> ', dog1.posicao);
