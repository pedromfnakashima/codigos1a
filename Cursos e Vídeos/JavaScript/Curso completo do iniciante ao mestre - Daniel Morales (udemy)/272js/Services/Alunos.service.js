import { AlunoModel } from './../Models/Aluno.model.js';

export class AlunosService {
  constructor() {
    this.alunos = [];
    this.updateListAlunosFromLocalStorage();
  }

  add(aluno) {
    if (!aluno instanceof AlunoModel) {
      throw TypeError('aluno must be a instance of AlunoModel');
    }
    this.alunos.push(aluno);
    this.updateLocalStorage();
  }

  edit(aluno) {
    aluno.generateAverage();
    this.updateLocalStorage();
  }

  searchById(id) {
    // console.log('this.alunos :>> ', this.alunos);
    return this.alunos.find((aluno) => aluno._id === id);
  }

  search(name) {
    return this.alunos.filter((aluno) => aluno.nome.indexOf(name) >= 0);
  }

  updateLocalStorage() {
    const alunos = JSON.stringify(this.alunos);
    localStorage.setItem('alunos', alunos);
  }

  updateListAlunosFromLocalStorage() {
    const local = localStorage.getItem('alunos');
    if (local) {
      const alunos = JSON.parse(local);
      alunos.forEach((aluno) => {
        this.add(new AlunoModel(aluno));
      });
    }
  }
}
