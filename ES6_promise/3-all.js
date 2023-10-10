import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((data) => {
      console.log(data[1].body.firstName, data[1].body.lastName);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
