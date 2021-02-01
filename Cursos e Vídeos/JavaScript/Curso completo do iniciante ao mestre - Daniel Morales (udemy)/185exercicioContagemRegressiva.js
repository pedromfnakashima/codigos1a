/* 

*/

(function () {
  const dateEventDOM = document.querySelector('.hero-content h1 span')
    .innerText;
  // console.log('dateEventDOM :>> ', dateEventDOM);

  const dateEvent = getDate(dateEventDOM);
  // console.log('dateEvent :>> ', dateEvent);

  const today = new Date();

  // Transforma tudo pra timestamp e subtrai
  let left = dateEvent.getTime() - today.getTime();

  const ONE_MINUTE = 60 * 1000;
  const ONE_HOUR = 60 * ONE_MINUTE;
  const ONE_DAY = 24 * ONE_HOUR;

  const daysLeft = parseInt(left / ONE_DAY);
  left = left - daysLeft * ONE_DAY;

  const hoursLeft = parseInt(left / ONE_HOUR);
  left = left - hoursLeft * ONE_HOUR;

  const minutesLeft = parseInt(left / ONE_MINUTE);
  left = left - minutesLeft * ONE_MINUTE;

  const secondsLeft = parseInt(left / 1000);
  // console.log('[daysLeft, hoursLeft, minutesLeft, secondsLeft] :>> ', [
  //   daysLeft,
  //   hoursLeft,
  //   minutesLeft,
  //   secondsLeft,
  // ]);

  addLeftTime(daysLeft, hoursLeft, minutesLeft, secondsLeft);

  function addLeftTime(d, h, m, s) {
    const p = document.createElement('p');
    p.textContent = `Contagem regressiva: ${d} dias, ${h} horas, ${m} minutos, ${s} segundos.`;
    document.querySelector('.hero-content').appendChild(p);
  }

  function getDate(str) {
    const [date, hour] = str.split(' ');
    // debugger;
    const [day, month, year] = date.split('/');
    const [h, m] = hour.split('H');
    return new Date(year, month - 1, day, h, m);
  }
})();
