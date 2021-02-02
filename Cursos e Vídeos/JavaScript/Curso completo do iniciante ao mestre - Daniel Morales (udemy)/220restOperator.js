/* 
220. rest operator
Tem que ser colocado, obrigatoriamente, como o último parâmetro.
*/

function teste(n1, n2, ...ns) {
  console.log('n1 :>> ', n1);
  console.log('n2 :>> ', n2);
  console.log('ns :>> ', ns);
  console.log('typeof ns :>> ', typeof ns);
  console.log('ns.map :>> ', ns.map);
}

teste(1, 2, 3, 4, 5);
