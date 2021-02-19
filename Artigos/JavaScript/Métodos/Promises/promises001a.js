/* 
Artigo.
JavaScript: Armadilhas do Async/Await em loops
https://oieduardorabelo.medium.com/javascript-armadilhas-do-asyn-await-em-loops-1cdad44db7f0

Pesquisa no google (async await fetch promise.all): https://www.google.com/search?q=async+await+fetch+promise.all&safe=strict&rlz=1C1SQJL_enBR879BR879&sxsrf=ALeKk03bRimrpC8f7oAZ9psdWbHnMADsPQ:1613686732094&ei=zOcuYIumBa3D5OUPh5CpyAM&start=0&sa=N&ved=2ahUKEwiLvMfDu_TuAhWtIbkGHQdICjk4ChDy0wN6BAgFEDo&biw=1207&bih=892
*/

const urls = [
  'https://jsonplaceholder.typicode.com/todos/1',
  'https://jsonplaceholder.typicode.com/todos/2',
  'https://jsonplaceholder.typicode.com/todos/3',
];

async function getTodos() {
  for (const [idx, url] of urls.entries()) {
    const todo = await fetch(url);
    console.log(`Received Todo ${idx + 1}:`, todo);
  }

  console.log('Finished!');
}
getTodos();
