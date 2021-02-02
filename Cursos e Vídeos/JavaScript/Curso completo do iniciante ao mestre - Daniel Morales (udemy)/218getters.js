/* 
218. iniciando com getters
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
    get posicao() {
      //-- o 'get' na frente permite acesso como se fosse propriedade; é equivalente ao @property do python
      console.log(`a posição atual de ${this.name} é ${posicao}`);
      return posicao;
    },
  };
}

const rex = criarCachorro('Rex');
rex.andar(10);
rex.andar(5);
console.log('rex.posicao :>> ', rex.posicao);

console.log('----------');

const toto = criarCachorro('Totó');
toto.andar(20);
toto.andar(-3);
console.log('toto.posicao :>> ', toto.posicao);
