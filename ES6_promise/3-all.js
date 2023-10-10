import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((data) => {
      const { body } = data[0];
      const { firstName, lastName } = data[1];
      return { ...body, ...firstName, ...lastName };
    }
    )
    .catch(() => {
      console.log('Signup system offline');
    });
}
