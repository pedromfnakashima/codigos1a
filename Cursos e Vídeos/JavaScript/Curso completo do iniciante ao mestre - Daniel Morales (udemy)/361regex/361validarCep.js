const regex = /^\d{5}-?\d{3}$/g;
const isCEPValid = (cep) => regex.test(cep);

console.log('isCEPValid("12345-678") :>> ', isCEPValid('12345-678'));
console.log('isCEPValid("12345-6789") :>> ', isCEPValid('12345-6789'));
