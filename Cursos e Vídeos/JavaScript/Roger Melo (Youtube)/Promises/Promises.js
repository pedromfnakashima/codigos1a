/* 
Ex. 1
*/

// let randomNumber = 9;

// setTimeout(() => {
//   randomNumber += 100;
//   console.log('randomNumber :>> ', randomNumber);
// }, 2000);

// console.log('randomNumber :>> ', randomNumber);

/* 
Ex. 2
*/

// const aPromise = new Promise((resolve, reject) => {
//   const aNumber = 37;
//   resolve(aNumber);
//   // reject(aNumber);
// });

/* 2a */
// aPromise.then((value) => {
//   console.log('value :>> ', value);
// });

/* 2b */
// aPromise
//   .then((value) => value)
//   .then((value) => {
//     console.log('value :>> ', value);
//   });

/* 2c */
// aPromise
//   .then((value) => value)
//   .then((value) => {
//     console.log('value :>> ', value);
//   })
//   .catch((rejectValue) => {
//     console.log('rejectValue :>> ', rejectValue);
//   });

/* 
  Ex. 3
  */

const url = 'https://dog.ceo/api/breeds/image/random';
const dogImg = document.querySelector('[data-js="dog-img"]');
// console.log('dogImg :>> ', dogImg);

console.log('fetch(url) :>> ', fetch(url)); // Promise {<pending>}

/* 3a */

fetch(url)
  .then((dogData) => {
    if (!dogData.ok) {
      // if (dogData.ok) {
      throw new Error(`HTTP error, status ${dogData.status}`);
    }
    console.log('dogData :>> ', dogData); // Response {}
    return dogData.json();
  })
  .then(({ message }) => {
    // console.log('message :>> ', message);
    dogImg.setAttribute('src', message);
  })
  .catch((error) => {
    console.log('error.message :>> ', error.message);
  });

/* 3b */

// const validateHTTPStatus = (dogData) => {
//   if (!dogData.ok) {
//     // if (dogData.ok) {
//     throw new Error(`HTTP error, status ${dogData.status}`);
//   }
//   // console.log('dogData :>> ', dogData); // Response {}
//   return dogData.json();
// };

// const setDogImg = ({ message: url }) => {
//   // console.log('url :>> ', url);
//   dogImg.setAttribute('src', url);
// };

// const handleRequestError = (error) => {
//   console.log('error.message :>> ', error.message);
// };

// fetch(url).then(validateHTTPStatus).then(setDogImg).catch(handleRequestError);
