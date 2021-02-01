
/* 

*/

function clicou(ev) {
    console.log('O click que foi atribuído a', ev.target.tagName, 'está atualmente em', ev.currentTarget.tagName);
}

document.querySelector('main').addEventListener('click', clicou)

document.querySelector('div').addEventListener('click', clicou)


