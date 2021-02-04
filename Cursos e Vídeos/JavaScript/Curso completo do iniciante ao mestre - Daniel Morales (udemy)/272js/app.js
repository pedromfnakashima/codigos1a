// Calcula a média por matéria de cada aluno e cria uma propriedade chamada média
alunos.forEach((aluno) => {
  aluno.media = {};

  for (let materia in aluno.notas) {
    aluno.media[materia] = average(...aluno.notas[materia]);
  }
});

console.log('alunos :>> ', alunos);

// Inserir no thead 'nome' e cada uma das matérias
const htmlHeader = document.createElement('tr');
htmlHeader.innerHTML = '<td>Nome</td>';

let htmlheaderMaterias = Object.keys(alunos[0].notas)
  .map((materia) => {
    // console.log('materia :>> ', materia);
    return `<td>${materia}</td>`;
  })
  .join('');
console.log('htmlheaderMaterias :>> ', htmlheaderMaterias);

htmlHeader.innerHTML += htmlheaderMaterias;

document.querySelector('[data-table-alunos] thead').appendChild(htmlHeader);

// Percorrer cada aluno e gerar o html para incluir no tbody
alunos.forEach((aluno) => {});
