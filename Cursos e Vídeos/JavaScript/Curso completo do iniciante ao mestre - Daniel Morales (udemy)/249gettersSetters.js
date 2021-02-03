/* 
249. getters e setters

Sem função auto invocável
*/
// let tipo = '';
// // const tiposPermitidos = { mamífero: true, anfíbio: true, réptil: true };
// const tiposPermitidos = ['mamífero', 'anfíbio'];

// const cachorro = {
//   name: 'rex',
//   get tipo() {
//     return tipo;
//   },
//   set tipo(_tipo) {
//     // if (tiposPermitidos[_tipo]) { /* padrão objeto */
//     if (tiposPermitidos.indexOf(_tipo) >= 0) { /* padrão array */
//       tipo = _tipo;
//     }
//   },
// };

// console.log('cachorro.tipo :>> ', cachorro.tipo);
// // cachorro.tipo = 'abc';
// cachorro.tipo = 'mamífero';
// console.log('cachorro.tipo :>> ', cachorro.tipo);

/* IIFE para evitar sujar escopo global */
(function () {
  let tipo = '';
  // const tiposPermitidos = { mamífero: true, anfíbio: true, réptil: true };
  const tiposPermitidos = ['mamífero', 'anfíbio'];

  const gato = {
    name: 'mingal',
    get tipo() {
      return tipo;
    },
    set tipo(_tipo) {
      // if (tiposPermitidos[_tipo]) { /* padrão objeto */
      if (tiposPermitidos.indexOf(_tipo) >= 0) {
        /* padrão array */
        tipo = _tipo;
      }
    },
  };
  // window.gato = gato; /* funciona no chrome, mas não no node */
  this.gato = gato; /* funciona no node; this é o objeto global */
})();

// console.log('gato.tipo :>> ', gato.tipo);
// // cachorro.tipo = 'abc';
// gato.tipo = 'anfíbio';
// console.log('gato.tipo :>> ', gato.tipo);
