import React from 'react';

const App1 = () => {
  const nome = 'Pedro';
  const random = Math.random();
  const ativo = true;
  const titulo = <h3>Esse é um título de h3</h3>;
  function mostrarNome(sobrenome) {
    return `Pedro ${sobrenome}`;
  }
  const carro = {
    marca: 'Ford',
    rodas: 4,
  };
  const estiloH1 = {
    color: 'blue',
    fontSize: '20px',
    fontFamily: 'Helvetica',
  };
  const estiloP = {
    color: 'blue',
    fontSize: '2rem',
  };
  return (
    <React.Fragment>
      {/* PARTE 1 */}
      {/* <a className="ativo" href="https://origamid.com" title="isso é um site">
        Origamid
      </a> */}
      {/* PARTE 2 */}
      {/* <label htmlFor="nome">Nome</label>
      <input type="text" id="nome" /> */}
      {/* PARTE 3 */}
      <p>{nome}</p>
      <p>{random * 1000}</p>
      <p className={ativo ? 'ativo' : 'inativo'}>Terceiro parágrafo</p>
      {titulo}
      {/* True ou False não é mostrado */}
      <p>{true}</p>
      {/* A linha abaixo é mostrada */}
      <p>{true ? 'verdadeiro' : 'falso'}</p>
      {/* Número é mostrado */}
      <p>{4}</p>
      {/* Funções executadas são mostradas */}
      <p>{mostrarNome('Nakashima')}</p>
      {/* Datas são mostradas */}
      <p>{new Date().getFullYear()}</p>
      {/* Também é possível passar um objeto */}
      <p>{carro.marca}</p>
      <p>{carro['rodas']}</p>
      {/* É possível estilizar passando um objeto dentro das chaves do JS */}
      <h3 style={estiloH1}>Título h3 estilizado</h3>
      <p style={{ color: 'green', fontSize: '30px' }}>
        Parágrafo estilizado. É possível estilizar um elemento, mas palavras
        compostas devem ser escritas com camel case. Essa é uma forma de colocar
        estilos que sejam dinâmicos de acordo com o javaScript, ou com alguma
        animação. Valores (de chavel-valor) devem ser sempre escritos como
        string. Ao contrário do CSS, os elementos de estilo não são separados
        por ponto-e-vírgula, mas sim com vírgulas. Passamos um objeto dentro das
        chaves do JS.
      </p>
      <p style={estiloP}>Esse é um estilo dinâmico</p>
    </React.Fragment>
  );
};

export default App1;
