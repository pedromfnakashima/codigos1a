export function sum() {
  // const numbers = Array.from(arguments)
  const numbers = [...arguments];
  return numbers.reduce(function (sum, atual) {
    return sum + atual;
  }, 0);
}
export function average() {
  return sum(...arguments) / arguments.length;
}
