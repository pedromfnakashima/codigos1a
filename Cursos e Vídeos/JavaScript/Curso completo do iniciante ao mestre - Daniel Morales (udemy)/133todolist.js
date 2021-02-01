/* 
ETAPAS
1. 
*/

//- 1.

(function () {
  'use strict';

  // 1. ARMAZENAR O DOM EM VARIÁVEIS
  const itemInput = document.getElementById('item-input');
  const todoAddForm = document.getElementById('todo-add');
  const ul = document.getElementById('todo-list');
  const lis = ul.getElementsByTagName('li'); // = coleção viva (atualiza quando adciona uma li a ul)

  // 3. Criar estrutura de dados; serão geradas as lis a partir de arrTasks, para depois serem inseridas na tela;

  function getSavedData() {
    let tasksData = localStorage.getItem('tasks');
    // console.log(tasksData);
    // console.log(typeof tasksData); // <= string

    tasksData = JSON.parse(tasksData); //! convert de string json para objeto
    // console.log(tasksData);
    // console.log(typeof tasksData); // <= object

    return tasksData && tasksData.length
      ? tasksData
      : [
          {
            name: 'task 1',
            createdAt: Date.now(),
            completed: false,
          },
          {
            name: 'task 2',
            createdAt: Date.now(),
            completed: false,
          },
        ];
  }
  // função setNewData recupera arrTasks e vai armazenar no local storage
  let arrTasks = getSavedData();
  function setNewData() {
    localStorage.setItem('tasks', JSON.stringify(arrTasks)); //! precisa usar o JSON.stringfy porque toda informação salva no localStorage é salva como string; por isso precisa converter para string json
  }

  setNewData();

  //2.6 função que adiciona o listener no li
  // function addEventLi(li) {
  //   li.addEventListener('click', function () {
  //     console.log('this', this);
  //     // console.log('this.textContent', this.textContent);
  //     // console.log('this.innerText', this.innerText);
  //     // console.log('this.innerHTML', this.innerHTML);
  //     // console.log('this.outerHTML', this.outerHTML);
  //   });
  // }

  // 3.2 função que retorna uma li a partir de uma entrada de arrTasks; cada output será usando em renderTasks
  function generateLiTask(obj) {
    // debugger; //! DEBUGGER é muito útil para verificar o valor de variáveis problemáticas; parece que ele para a execução do código naquele ponto e permite verificar o valor atribuído a uma variável em um momento específico da execução.
    const li = document.createElement('li');
    const p = document.createElement('p');
    const checkButton = document.createElement('button');
    const editButton = document.createElement('i');
    const deleteButton = document.createElement('i');

    li.className = 'todo-item';

    checkButton.className = 'button-check';
    checkButton.innerHTML = `
      <i class="fas fa-check ${
        obj.completed ? '' : 'displayNone'
      }" data-action="checkButton"></i>`; //! idem do de baixo
    checkButton.setAttribute('data-action', 'checkButton'); //! atributo data-action adicionado p/ deixar robusta a delegação de eventos, a alterações na classe; ver função clickedUl;

    li.appendChild(checkButton);

    p.className = 'task-name';
    p.textContent = obj.name;
    li.appendChild(p);

    editButton.className = 'fas fa-edit'; // pode ser feito com .classList.add() //! o professor falou prefere que quando está criando o elemento, fazer com .classname =
    editButton.setAttribute('data-action', 'editButton'); //! atributo data-action adicionado p/ deixar robusta a delegação de eventos, a alterações na classe; ver função clickedUl;
    li.appendChild(editButton);

    const containerEdit = document.createElement('div');
    containerEdit.className = 'editContainer';
    const inputEdit = document.createElement('input');
    inputEdit.setAttribute('type', 'text');
    inputEdit.className = 'editInput';
    inputEdit.value = obj.name; //! faz com que o DOM gerado já venha com o valor da task
    containerEdit.appendChild(inputEdit);

    const containerEditButton = document.createElement('button');
    containerEditButton.className = 'editButton';
    containerEditButton.textContent = 'Edit';
    containerEditButton.setAttribute('data-action', 'containerEditButton'); //! atributo data-action adicionado p/ deixar robusta a delegação de eventos, a alterações na classe; ver função clickedUl;
    containerEdit.appendChild(containerEditButton);

    const containerCancelButton = document.createElement('button');
    containerCancelButton.className = 'cancelButton';
    containerCancelButton.textContent = 'Cancel';
    containerCancelButton.setAttribute('data-action', 'containerCancelButton'); //! atributo data-action adicionado p/ deixar robusta a delegação de eventos na classe; ver função clickedUl;
    containerEdit.appendChild(containerCancelButton);

    li.appendChild(containerEdit);

    deleteButton.classList.add('fas', 'fa-trash-alt'); // pode ser feito com .classname=
    deleteButton.setAttribute('data-action', 'deleteButton');
    li.appendChild(deleteButton);

    //2.5 Adiciona o listenner no li
    // addEventLi(li);

    return li;
  }

  // 3.3 Função que olha pra arrTasks, gera as lis, e iclui as lis na lista; limpa toda a ul, e depois acrescenta as lis novamente usando o restulado de de generateLiTask
  function renderTasks() {
    ul.innerHTML = ''; // limpa a lista
    // Para cada entrada de arrTasks, adiciona uma li criada por generateLiTask
    arrTasks.forEach((taskObj) => {
      ul.appendChild(generateLiTask(taskObj));
    });
  }

  //2.4 função que adiciona uma tarefa na arrTasks
  function addTask(task) {
    arrTasks.push({
      name: task,
      createdAt: Date.now(),
      completed: false,
    });

    setNewData();
  }

  // 4.1 cria a função
  function clickedUl(e) {
    const dataAction = e.target.getAttribute('data-action');
    console.log(e.target);

    if (!dataAction) return;

    // FAZ BUSCA NO DOM POR UM PAI DO ELEMENTO CLICADO QUE SEJA li
    let currentLi = e.target;
    while (currentLi.nodeName !== 'LI') {
      currentLi = currentLi.parentElement;
    }
    // console.log(currentLi);

    // verifica, na htmlCollection lis, qual é o índice da li clicada (currentLi)
    const currentLiIndex = [...lis].indexOf(currentLi);
    // console.log(currentLiIndex);

    const actions = {
      editButton: function () {
        // console.log('é edit button no objeto');
        const editContainer = currentLi.querySelector('.editContainer');

        // toda vez que abre um container, fecha os demais:
        [...ul.querySelectorAll('.editContainer')].forEach((container) => {
          container.removeAttribute('style');
        });

        editContainer.style.display = 'flex'; // antes, estava display none
      },
      deleteButton: function () {
        // console.log('é delete button no objeto');
        arrTasks.splice(currentLiIndex, 1);
        // console.log(arrTasks); // mostra que arrTasks tem 1 elemento a menos
        renderTasks(); // função que olha pra arrTasks e renderiza navamente as lis; //! Linha equivalente: currentLi.remove() ou (brownsers mais antigos) currentLi.parentElement.removeChild(currentLi)
        setNewData();
      },
      containerEditButton: function () {
        // recupera o valor do input
        const val = currentLi.querySelector('.editInput').value;
        // debugger;
        // atualiza a fonte de dados
        arrTasks[currentLiIndex].name = val;
        renderTasks();
        setNewData();
      },
      containerCancelButton: function () {
        currentLi.querySelector('.editContainer').removeAttribute('style');
        // zera o valor original do input
        currentLi.querySelector('.editInput').value =
          arrTasks[currentLiIndex].name;
      },
      checkButton: function () {
        // atualiza a fonte de dados - inverte o valor da chave 'completed' - se era false, vira true; se era true, vira false
        arrTasks[currentLiIndex].completed = !arrTasks[currentLiIndex]
          .completed;

        // remove ou acrescenta a classe displayNone que está na tag i

        if (arrTasks[currentLiIndex].completed) {
          currentLi.querySelector('.fa-check').classList.remove('displayNone');
        } else {
          currentLi.querySelector('.fa-check').classList.add('displayNone');
        }

        setNewData();
        renderTasks();
      },
    };

    // console.log(e.target);
    // console.log(e.target.getAttribute('data-action'));

    // if (e.target.getAttribute('data-action') === 'editButton') {
    //   console.log('é edit button no if');
    // }

    if (actions[dataAction]) {
      actions[dataAction]();
    }
  }

  // 2. Adicionar o evento de submit no formulário
  todoAddForm.addEventListener('submit', function (e) {
    e.preventDefault();
    console.log(itemInput.value); // <= valor digitado pelo usuário
    // ul.innerHTML += `
    //       <li class="todo-item">
    //         <p class="task-name">${itemInput.value}</p>
    //       </li>`;
    // 2.3 adiciona li à ul?
    addTask(itemInput.value);
    // 3.4 renderiza tasks (printa na tela) com a lista atualizada
    renderTasks();
    // 2.1 Limpar o input
    itemInput.value = '';
    // 2.2 Coloca o focus novamente no input
    itemInput.focus();

    //---- Loop nas lis. Mostrar no console sempre que clicar numa li
    // [...lis].forEach((li) => {
    //   addEventLi(li);
    // });
  });

  // 4. Adiciona evento de clique na ul inteira
  ul.addEventListener('click', clickedUl);

  renderTasks(); //! função que olha pra array de dados (arrTasks), e printa na tela as informações da array
})();
