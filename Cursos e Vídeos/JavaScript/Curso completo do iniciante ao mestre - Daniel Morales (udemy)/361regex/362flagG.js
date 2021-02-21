/* Com problema (com a flag g) */
// const regex = /^\d{5}-?\d{3}$/g;
/* Sem problema (sem a flag g) */
const regex = /^\d{5}-?\d{3}$/;

const isCEPValid = (cep) => regex.test(cep);

const elfocus = () => console.log('deu focus (clicou no campo)');
const elblur = (e) => {
  const cep = e.target.value;
  console.log('deu blur (clicou fora do campo)');
  console.log('isCEPValid(cep) :>> ', isCEPValid(cep));
};

const el = document.getElementById('cep');
el.addEventListener('focus', elfocus);
el.addEventListener('blur', elblur);
