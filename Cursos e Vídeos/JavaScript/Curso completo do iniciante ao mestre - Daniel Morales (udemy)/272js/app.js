const alunos = [
  {
    _id: 0,
    nome: 'chico melato',
    notas: {
      portugues: [1, 1, 2, 2],
      matematica: [2, 2, 2, 2],
      historia: [2, 2, 3, 3],
      ciencias: [3, 3, 3, 3],
    },
  },
  {
    _id: 1,
    nome: 'talita lima',
    notas: {
      portugues: [4, 4, 4, 4],
      matematica: [4, 4, 5, 5],
      historia: [5, 5, 6, 6],
      ciencias: [7, 7, 8, 9],
    },
  },
];

const alunosService = new AlunosService();

// Calcula a média por matéria de cada aluno e cria uma propriedade chamada média
alunos.forEach((aluno) => {
  alunosService.add(new AlunoModel(aluno));
});

const alunosView = new AlunosView(
  document.querySelector('[data-table-alunos]')
);

const alunosController = new AlunosController(alunosService, alunosView);

// document.querySelector('form').addEventListener('submit', function (e) {
//   e.preventDefault();
//   const nome = document.getElementById('first_name').value;
//   const newAluno = {
//     _id: 0,
//     nome,
//     notas: {
//       portugues: [1, 1, 2, 2],
//       matematica: [2, 2, 2, 2],
//       historia: [2, 2, 3, 3],
//       ciencias: [3, 3, 3, 3],
//     },
//   };
//   // console.log('nome :>> ', nome);
//   newAluno.media = {};

//   for (let materia in newAluno.notas) {
//     newAluno.media[materia] = average(...newAluno.notas[materia]);
//   }

//   alunos.push(newAluno);

//   render();
// });
