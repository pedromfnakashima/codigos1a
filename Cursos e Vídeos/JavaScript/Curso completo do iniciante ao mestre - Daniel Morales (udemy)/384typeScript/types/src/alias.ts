function add2(x: number, y?: number) {
  if (y === undefined) {
    return null;
  }
  return x + y;
}

// console.log(add2(4));
const teste2 = add2(10);

type testeAlias = number | string | boolean;

// let teste3: number | string | boolean;
let teste3: testeAlias;
teste3 = 10;
teste3 = 'teste 3';
teste3 = true;

// let teste4: number | string | boolean
let teste4: testeAlias;
teste4 = 10;

type User = {
  nome: string;
  idade?: number | null;
};

const joao: User = {
  nome: 'joao',
  idade: null,
};

const maria: User = {
  nome: 'maria',
  idade: null,
};

type Sizes = '12 px' | '16 px' | '24 px';

const small: Sizes = '12 px';
// const normal : Sizes = '20 px'
const normal: Sizes = '16 px';

export default 1; // linha sem sentido, só para não gerar erros nas variáveis duplicadas
