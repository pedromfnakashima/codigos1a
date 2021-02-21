import axios from 'axios';

const teste = 'teste 4';

const arrowFn = (n) => n * n;

console.log('arrowFn(2) :>> ', arrowFn(2));

const getAddress = async (cep) => {
  let url = `https://viacep.com.br/ws/${cep}/json`;
  try {
    const resposta = await axios.get(url);
    const json = resposta.data;
    return json;
  } catch {
    throw e;
  }
};

console.log('--------------');
getAddress('79032-370').then((data) => console.log('data :>> ', data));
