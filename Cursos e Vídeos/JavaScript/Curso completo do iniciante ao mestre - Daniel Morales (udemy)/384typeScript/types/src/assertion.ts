const teste = document.getElementById('teste') as HTMLButtonElement;

// teste.addEventListener('click', e => console.log(e))
teste.addEventListener('click', (e: MouseEvent) => console.log(e)); // mesma coisa que o código acima

export { teste };
