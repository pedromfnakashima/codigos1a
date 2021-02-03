/* 
252. Desafio: getters e setters
Crie um objeto pessoa.
Deve ter uma propriedade get chamada usuarios que deve armazenar uma array de strings.
Deve ter uma propriedade get chamada usuario que deve retornar o último usuário da array.
Sempre que alterar o usuário (set), não deve substituir, mas sim colocar num array, se já não existir na array usuarios.
Deve ter uma propriedade get usuarios para recuperar o histórico de usuários.

254. evite exportar referências
Alternativa 1.
Object.freeze(usuarios)
. o array vai estar congelado e não ser possível fazer alterações
Alternativa 2.
. retornar uma cópia do array.
return [...usuarios]
ou (jeito antigo)
retunr [].concat(usuarios)

*/

/*  */

(function () {
  let usuarios = [];
  this.pessoa = {
    get usuario() {
      if (usuarios.length) {
        return usuarios[usuarios.length - 1];
      }
    },
    set usuario(_usuario) {
      if (usuarios.indexOf(_usuario) < 0) {
        usuarios.push(_usuario);
      }
    },
    get usuarios() {
      return [...usuarios]; //! retorna uma cópia do array usuários
    },
  };
})();

pessoa.usuario = 'teste1';
console.log('pessoa.usuario :>> ', pessoa.usuario);
pessoa.usuario = 'teste2';
console.log('pessoa.usuario :>> ', pessoa.usuario);
console.log('pessoa.usuarios :>> ', pessoa.usuarios);
teste = pessoa.usuarios;
teste = ['sou hacker'];
console.log('pessoa.usuarios :>> ', pessoa.usuarios); // continua sendo o array original, porque não tem set usuarios
teste = pessoa.usuarios;
teste.pop();
console.log('pessoa.usuarios :>> ', pessoa.usuarios); // alterou pois aponta para o mesmo local
delete teste[0];
console.log('pessoa.usuarios :>> ', pessoa.usuarios); // alterou pois aponta para o mesmo local
