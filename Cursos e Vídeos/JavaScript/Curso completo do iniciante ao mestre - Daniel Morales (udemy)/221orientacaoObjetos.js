/* 

Orientação a objetos em JS e a clássica
Em JavaScript, a POO se dá através de protótipos (prototypes).
Na POO, um objeto é criado a partir de uma classe.
Na POO, uma classe é uma especificação (um molde) para criar objetos.
Nunca geramos diretamente a classe, mas sim objetos gerados a partir daquela classe.
No JavaScript, herança ocorre por meio de seu protótipo.
A POO não é reutilização de código.
A conta poupança é parecida com a conta corrente. Precisamos fazer as duas contas herdarem uma classe menos específica. Classe genérica é abstrata, classe específica é concreta.
Faz sentido Cliente ser outra classe, com métodos e propriedades próprios?
HERANÇA:
Uma conta poupança É uma conta bancária.
Uma conta corrente É uma conta bancária.
ASSOCIAÇÃO:
Uma conta bancária TEM um cliente.
Uma conta bancária NÃO É um cliente.

ContaBancária é classe abstrata:
Errado!!!
let cb = new ContaBancária()
Cliente é classe concreta:
Certo!!!
let eu = new Cliente()

No JS, Prototype é a base para herança.

EXTENDS (ES6) VS PROTOTYPE (ES5)
Não se engane, extends é só um "açúcar sintático" para prototype. Por baixo dos panos, continua sendo prototype.

*/
