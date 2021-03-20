/* Usei o snippet do vsCode rfc */
import React from 'react';
// Mostre os dados da aplicação, como aprensetado no vídeo
// Não utilize CSS externo, use o style para mudar as cores
// Se a situação estiver ativa pinte de verde, inativa vermelho
// Se o gasto for maior que 10000 mostre uma mensagem
const luana = {
  cliente: 'Luana Lopes',
  idade: 27,
  compras: [
    { nome: 'Notebook', preco: 'R$ 2500' },
    { nome: 'Geladeira', preco: 'R$ 3000' },
    { nome: 'Smartphone', preco: 'R$ 1500' },
  ],
  ativa: true,
};

const mario = {
  cliente: 'Mario Medeiros',
  idade: 31,
  compras: [
    { nome: 'Notebook', preco: 'R$ 2500' },
    { nome: 'Geladeira', preco: 'R$ 3000' },
    { nome: 'Smartphone', preco: 'R$ 1500' },
    { nome: 'Guitarra', preco: 'R$ 3500' },
  ],
  ativa: false,
};

export default function App2() {
  const dados = mario;

  const total = dados.compras
    .map((item) => Number(item.preco.replace('R$ ', '')))
    .reduce((a, b) => a + b);
  // console.log('total :>> ', total);

  return (
    <div>
      <p>Nome: {dados.cliente}</p>
      <p>idade: {dados.idade}</p>
      <p>
        {/* As chaves depois da 'Situação' serve apenas para renderizar um espaço */}
        Situação:{' '}
        <span
          style={{ color: dados.ativa ? 'green' : 'red', fontWeight: 'bold' }}
        >
          {dados.ativa ? 'Ativa' : 'Inativa'}
        </span>
      </p>
      <p>Total: R$ {total}</p>
      {/* A solução abaixo (operador ternário) traz um <p></p> vazio no caso de ternário falso */}
      <p>{total > 10000 ? 'Você está gastando muito (ternário)' : ''}</p>
      {/* A solução abaixo (curto-circuito) traz um <p></p> vazio no caso de ternário falso */}
      <p>{total > 10000 && 'Você está gastando muito (curto-circuito)'}</p>
      {/* A solução abaixo (JSX dentro de JSX) NÃO traz um <p></p> vazio no caso de ternário falso */}
      {total > 10000 && <p>Você está gastando muito (JSX dentro de JSX)</p>}
    </div>
  );
}
