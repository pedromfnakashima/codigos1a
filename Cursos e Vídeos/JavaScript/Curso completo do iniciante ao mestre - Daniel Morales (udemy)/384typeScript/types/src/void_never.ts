/* void
retorna, no máximo, undefined
*/

function showFeedback(message: string, type: string): void {
  alert(type.toUpperCase() + ': ' + message);
}

const feedback = showFeedback('ola', 'info'); /* seria undefined no clg */

/*  never
nunca retorna nada; pode ser usado p/ retornar erro
*/

function showError(message: string): never {
  throw new Error('função marcada com never nunca retorna nada');
}

const error = showError('mensagem de derro');
