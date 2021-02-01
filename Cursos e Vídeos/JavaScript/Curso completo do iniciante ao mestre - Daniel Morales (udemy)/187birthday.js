function quantoFaltaPara(m, d) {
  const dataAtual = new Date();
  dataAtual.setHours(0);
  dataAtual.setMinutes(0);
  dataAtual.setSeconds(0);
  dataAtual.setMilliseconds(0);

  // define com o let porque vai ser redefinido dentro do if
  let anoAtual = dataAtual.getFullYear();

  const dataNiver = new Date(anoAtual, m - 1, d);

  // Sinal de + converte data p/ Time Stamp [equivalente a data.getTime()]
  const dataAtualTS = +dataAtual;
  const dataNiverTS = +dataNiver;

  // se o aniversário já passou, seta o ano p/ o próximo
  if (dataNiverTS < dataAtualTS) {
    dataNiver.setFullYear(++anoAtual);
    dataNiverTS = +dataNiver;
  }

  // número de milisegundos que cabem em um dia
  const UM_DIA = 24 * 60 * 60 * 1000;
  const diferenca = dataNiverTS - dataAtualTS;

  return parseInt(diferenca / UM_DIA);
}
