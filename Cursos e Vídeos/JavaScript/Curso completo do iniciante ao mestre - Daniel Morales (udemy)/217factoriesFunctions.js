/* 
217. Factories Functions
Ex. 1.
*/

function criarCachorro(name) {
  let posicao = 0;
  return {
    name,
    latir() {
      console.log(this.name, 'está latindo');
    },
    andar(distancia) {
      posicao += distancia;
      console.log(this.name, 'andou ', distancia, ' m');
    },
    pegaPosicao() {
      console.log(`a posição atual de ${this.name} é ${posicao}`);
      return posicao;
    },
  };
}

const rex = criarCachorro('Rex');
rex.andar(10);
rex.andar(5);
rex.pegaPosicao();
// console.log('rex.pegaPosicao() :>> ', rex.pegaPosicao());

console.log('----------');

const toto = criarCachorro('Totó');
toto.andar(20);
toto.andar(-3);
toto.pegaPosicao();
// console.log('toto.pegaPosicao() :>> ', toto.pegaPosicao());
