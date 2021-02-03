/* 
260. Congelar propriedades de um objeto.
-CONGELAMENTO RASO (A PRIMEIRA CAMADA DE PROPRIEDADES)
Métodos.
freeze
. não pode criar, nem atualizar, e nem remover propriedades
seal

preventExtensions

*/

const obj = {
  prop1: 'prop 1',
  prop2: 'prop 2',
};

objFreeze = { ...obj };
objSeal = { ...obj };
objPrevent = { ...obj };

//-- Object.freeze - não pode criar, nem atualizar, e nem remover propriedades
Object.freeze(objFreeze);
console.log('objFreeze :>> ', objFreeze);
delete objFreeze.prop1;
objFreeze.prop3 = 'teste';
console.log('objFreeze :>> ', objFreeze);

//-- Object.seal - não pode criar, pode atualizar, mas não pode remover propriedades
Object.seal(objSeal);
console.log('objSeal :>> ', objSeal);
delete objSeal.prop1;
objSeal.prop3 = 'teste';
objSeal.prop1 = 'novo valor de prop1';
console.log('objSeal :>> ', objSeal);

//-- Object.seal - não pode criar, pode alterar, pode remover props
Object.preventExtensions(objPrevent);
console.log('objPrevent :>> ', objPrevent);
delete objPrevent.prop2;
objPrevent.prop3 = 'teste';
objPrevent.prop1 = 'novo valor de prop1';
console.log('objPrevent :>> ', objPrevent);

/* 
261. deep freeze
- CONGELAMENTO PROFUNDO
próximo arquivo
*/
