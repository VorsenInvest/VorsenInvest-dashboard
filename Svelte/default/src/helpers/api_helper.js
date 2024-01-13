import axios from "axios";
import { browser } from "$app/environment";
import { goto } from '$app/navigation';

// // content type
// console.log("token")
// const token = JSON.parse(localStorage.getItem("authUser")) ? JSON.parse(localStorage.getItem("authUser")).token : null;
// if (token)
//   axios.defaults.headers.common["Authorization"] = "Bearer " + token;
let token = '';

if(browser) {
  let authUser = localStorage.getItem('authUser');
  if (authUser) {
    authUser = JSON.parse(authUser);
    token = authUser.token;
  }else{
    goto("/authentication/login");
  }
};
// console.log(token,'token')
// if(token)
// axios.defaults.headers.common["Authorization"] = "Bearer " + token;

// // intercepting to capture errors
// axios.interceptors.response.use(
//   function (response) {
//     return response.data ? response.data : response;
//   },
//   function (error) {
//     // Any status codes that falls outside the range of 2xx cause this function to trigger
//     let message;
//     switch (error.status) {
//       case 500:
//         message = "Internal Server Error";
//         break;
//       case 401:
//         message = "Invalid credentials";
//         break;
//       case 404:
//         message = "Sorry! the data you are looking for could not be found";
//         break;
//       default:
//         message = error.message || error;
//     }
//     return Promise.reject(message);
//   }

// );

// if(token) {
// axios.defaults.headers.common["Authorization"] = "Bearer " + token;
// }

const setAuthorization = (token) => {
  axios.defaults.headers.common["Authorization"] = "Bearer " + token;
};

const axiosAPI = axios.create({
  baseURL: import.meta.env.VITE_PUBLIC_BASE_PATH,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': "Bearer " + token
  }
});

let username = 'admin@themesbrand.com';
let password = '123456';

const apiRequest = (method, url, request) => {
  console.log("method, url, request", method, url, request)
  //using the axios instance to perform the request that received from each http method
  return axiosAPI({
    method,
    url,
    data: request,
    body: JSON.stringify({ email: username, password: password }),
  }).then(res => {
    return Promise.resolve(res.data);
  })
    .catch(err => {
      return Promise.reject(err);
    });
};

// function to execute the http get request
const get = (url, request) => apiRequest("get", url, request);

// function to execute the http delete request
const deleteRequest = (url, request) => apiRequest("delete", url, request);

// function to execute the http post request
const post = (url, request) => apiRequest("post", url, request);

// function to execute the http put request
const put = (url, request) => apiRequest("put", url, request);

// function to execute the http path request
const patch = (url, request) => apiRequest("patch", url, request);

const getLoggedinUser = () => {
  const user = localStorage.getItem("authUser");
  if (!user) {
    return null;
  } else {
    return JSON.parse(user);
  }
};

const API = {
  get,
  delete: deleteRequest,
  post,
  put,
  patch,
  setAuthorization,
  getLoggedinUser
};

export default API;