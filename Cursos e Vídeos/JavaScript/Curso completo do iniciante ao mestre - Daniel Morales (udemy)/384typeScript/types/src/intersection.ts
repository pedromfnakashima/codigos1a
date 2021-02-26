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

export default 1;
