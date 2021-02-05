class AlunoModel {
  // constructor(aluno) {
  //   this.nome = aluno.nome
  // }
  constructor({ nome, _id, notas } = { notas: {} }) {
    this.nome = nome;
    this.notas = { ...notas };

    this._id = _id !== undefined ? _id : this.generateId();

    /* maxId começa com zero; cada vez que a classe é instanciada, o maxId é atualizado com o último id */
    if (this._id > AlunoModel.maxId) {
      AlunoModel.maxId = this._id;
    }

    this.media = {};

    for (let materia in this.notas) {
      this.media[materia] = average(...this.notas[materia]);
    }
  }

  generateId() {
    return AlunoModel.maxId + 1;
  }
}

AlunoModel.maxId = 0;
