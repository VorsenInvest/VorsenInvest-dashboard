import axios from "axios";
import MockAdapter from "axios-mock-adapter";
import * as url from "../url_helper";
import todoTaskList from '../../common/data/todoData'

// let users = [
//     {
//       uid: 1,
//       username: "admin",
//       role: "admin",
//       password: "123456",
//       email: "admin@themesbrand.com",
//       token : null
//     },
//   ];
  
  const fakeBackend = () => {
    const mock = new MockAdapter(axios, { onNoMatch: "passthrough" });
      // To do
      mock.onGet('/todo').reply(() => {
        return new Promise((resolve, reject) => {
          setTimeout(() => {
            if (todoTaskList.todoTaskList) {
              // Passing fake JSON data as response
              resolve([200, todoTaskList.todoTaskList]);
            } else {
              reject([400, "Cannot get To do data"]);
            }
          });
        });
      });
  }

  export default fakeBackend;