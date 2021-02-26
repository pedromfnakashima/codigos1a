// function add(x: number, y: number): number {
function add(x: number, y: number) {
  return x + y;
}

const multiply = (x: number, y: number) => {
  return x * y;
};

const subtract: (x: number, y: number) => number = (x, y) => x - y;
let teste = subtract(3, 1);

/* ex. 2
criar uma função que retorna se o usuário é ou não admin  */

type User = {
  name: string;
  id: number;
};

type LevelAdmin = 'teacher' | 'coordinator' | 'manager';

type Admin = {
  isAdmin: true;
  level: LevelAdmin;
};

type UserAdmin = User & Admin;

let pedro: UserAdmin = {
  name: 'pedro',
  id: 0,
  isAdmin: true,
  level: 'teacher',
};

type IsAdmin = (user: User) => boolean;

/* a função
as = assertion
faz conversão de tipos
*/
const isAdmin: IsAdmin = (user) => !!(user as UserAdmin).isAdmin;

isAdmin(pedro);

let maria: User = {
  name: 'maria',
  id: 1,
};

console.log(isAdmin(maria));

export default 2;
