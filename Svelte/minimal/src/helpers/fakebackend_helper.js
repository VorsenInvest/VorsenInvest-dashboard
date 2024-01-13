import Api from "./api_helper";
import axios from "axios";

export const getLeads = async () => {
    try {
      const response = await Api.get("/apps/lead");
      return response.data;
    } catch (error) {
      console.error(error);
    }
};

export const addNewLead = async (lead) => {
    try {
      const response = await Api.post("/apps/lead", lead);
      return response.data;
    } catch (error) {
      console.error(error);
    }
};

export const updateLead = async (lead) => {
  try {
    const response = await Api.patch("/apps/lead" + '/' + lead._id, lead);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const deleteLead = async (lead) => {
  try {
    const response = await Api.delete("/apps/lead" + '/' + lead);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getProducts = async () => {
    try {
      const response = await Api.get("/apps/product");
      return response.data;
    } catch (error) {
      console.error(error);
    }
};

export const addNewProduct = async (product) => {
    try {
      const response = await Api.post("/apps/product", product);
      return response.data;
    } catch (error) {
      console.error(error);
    }
};

export const updateProduct = async (product) => {
  try {
    const response = await Api.patch("/apps/product" + '/' + product._id, product);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const deleteProducts = async (product) => {
  try {
    const response = await Api.delete("/apps/product" + '/' + product._id, product);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getOrders = async () => {
  try {
    const response = await Api.get("/apps/order");
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const addNewOrder = async (order) => {
  try {
    const response = await Api.post("/apps/order", order);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const updateOrder = async (order) => {
  try {
    const response = await Api.patch("/apps/order" + '/' + order._id, order);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const deleteOrder = async (order) => {
  try {
    const response = await Api.delete("/apps/order" + '/' + order._id, order);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getCustomer = async () => {
  try {
    const response = await Api.get("/apps/customer");
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const addNewCustomer = async (customer) => {
  try {
    const response = await Api.post("/apps/customer", customer);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const updateCustomer = async (customer) => {
  try {
    const response = await Api.patch("/apps/customer" + '/' + customer._id, customer);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const deleteCustomer = async (customer) => {
  try {
    const response = await Api.delete("/apps/customer" + '/' + customer._id, customer);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getSellers = async () => {
  try {
    const response = await Api.get("/sellers");
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getTaskList = async () => {
  try {
    const response = await Api.get("/apps/task");
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const addNewTask = async (task) => {
  try {
    const response = await Api.post("/apps/task", task);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const updateTask = async (task) => {
  try {
    const response = await Api.patch("/apps/task" + '/' + task._id, task);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const deleteTask = async (task) => {
  try {
    const response = await Api.delete("/apps/task" + '/' + task);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getContacts = async () => {
  try {
    const response = await Api.get("/apps/contact");
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

export const addNewContact = async (contact) => {
  try {
    const response = await Api.post("/apps/contact", contact);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const updateContact = async (contact) => {
  try {
    const response = await Api.patch("/apps/contact" + '/' + contact._id, contact);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const deleteContact = async (contact) => {
  try {
    const response = await Api.delete("/apps/contact" + '/' + contact);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getCompanies = async () => {
  try {
    const response = await Api.get("/apps/company");
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

export const addNewCompanies = async (company) => {
  try {
    const response = await Api.post("/apps/company", company);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const updateCompanies = async (company) => {
  try {
    const response = await Api.patch("/apps/company" + '/' + company._id, company);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const deleteCompanies = async (company) => {
  try {
    const response = await Api.delete("/apps/company" + '/' + company);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getTicketsList = async () => {
  try {
    const response = await Api.get("/apps/ticket");
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

export const addNewTicket = async (ticket) => {
  try {
    const response = await Api.post("/apps/ticket", ticket);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const updateTicket = async (ticket) => {
  try {
    const response = await Api.patch("/apps/ticket" + '/' + ticket._id, ticket);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const deleteTicket = async (ticket) => {
  try {
    const response = await Api.delete("/apps/ticket" + '/' + ticket);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getTodos = async () => {
  // try {
  //   var response = [];
  //   await axios.get("/todo").then(function (todo) {
  //     response = todo.data
  //     return Promise.resolve(todo.data);
  //   }).catch(err => {
  //     return Promise.reject(err);
  //   });
  //   return response;
  // } catch (error) {
  //   console.error(error);
  // }
  try {
    const response = await Api.get("/apps/todo");
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

export const addTodos = async (todo) => {
  try {
    await axios.get("/add/todo").then(function (todo) {
      response = todo.data
      return Promise.resolve(todo.data);
    }).catch(err => {
      return Promise.reject(err);
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};