import f_myMod1, {
  myMod1_nomeada,
  PI,
  obj,
  nome,
  idade,
} from './302modules/mod1.js';

console.log('app rodando');

const myMod = f_myMod1();
console.log('myMod :>> ', myMod);

const myMod1_nomeada_ = myMod1_nomeada();
console.log('myMod1_nomeada_ :>> ', myMod1_nomeada_);

console.log('PI :>> ', PI);

console.log('obj :>> ', obj);

console.log('nome :>> ', nome);
console.log('idade :>> ', idade);
