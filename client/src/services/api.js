import axios from 'axios';
const API_BASE_URL = 'http://localhost:5000/api';

/**
 * 
 * @param {*} email 
 * @param {*} password 
 */
export const isLogin = (email, password) => {
  axios
    .post(`${API_BASE_URL}/validate/login`, { 
      email: email, 
      password: password
    }).then(response => {
      viewData(response);
      return response.data;
    }).catch(err => {
      // TODO: Handle error methodology.
      console.log(err);
    });
};

/**
 * 
 * @param {*} userID 
 */
export const fetchUser = (userID) => {
  axios
    .post(`${API_BASE_URL}/fetch/user/`, {
      userID: userID
    }).then(response => {
      viewData(response);
      return response.data;
    }).catch(err => {
      // TODO: Handle error methodology.
      console.log(err);
    });
};

/**
 * 
 * @param {*} userID 
 * @param {*} networkID 
 */
export const fetchNetwork = async (userID, networkID) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/fetch/network`, { userID, networkID });
    console.log('Network response:', response); // Add this line for debugging
    return { data: response.data }; // Wrap the response data in an object
  } catch (error) {
    console.error('Error in fetchNetwork:', error);
    throw error; // Re-throw the error to be caught in the component
  }
};

/**
 * 
 * @param {*} userID 
 */
export const createNetwork = (userID) => {
  axios
    .post(`${API_BASE_URL}/create/network`, {
      userID: userID
    }).then(response => {
      viewData(response);
      return response.data;
    }).catch(err => {
      // TODO: Handle error methodology.
      console.log(err);
    });
};

/**
 * 
 * @param {*} userID 
 * @param {*} connID 
 */
export const fetchConnection = (userID, connID) => {
  axios
    .post(`${API_BASE_URL}/fetch/connection/`, { 
      userID: userID,
      connID: connID
    }).then(response => {
      viewData(response);
      return response.data;
    }).catch(err => {
      // TODO: Handle error methodology.
      console.log(err);
    });
};

/**
 * TODO: 
 * @param {*} userID 
 * @param {*} connectionID 
 * @param {*} networkID 
 */
export const updateConnection = (userID, connectionID, networkID) => {
  axios
    .post(`${API_BASE_URL}/update/connection`, { 
      userID: userID,
      connectionID: connectionID,
      networkID : networkID
    }).then(response => {
      viewData(response);
      return response.data;
    }).catch(err => {
      // TODO: Handle error methodology.
      console.log(err);
    });
};

/**
 * 
 * @param {*} userID 
 * @param {*} networkID 
 * @param {*} email 
 * @param {*} fname 
 * @param {*} lname 
 * @param {*} source 
 * @param {*} target 
 */
export const createConnection = (userID, networkID, email, fname, lname, source, target) => {
  axios
    .post(`${API_BASE_URL}/create/connection`, {
      userID: userID,
      networkID: networkID,
      email: email,
      fname: fname,
      lname: lname,
      source: source, 
      target: target
    }).then(response => {
      viewData(response);
      return response.data;
    }).catch(err => {
      // TODO: Handle error methodology.
      console.log(err);
    });
};

/**
 * 
 * @param {*} userID 
 * @param {*} networkID 
 * @param {*} connectionID 
 */
export const fetchConnectionMenu = async (userID, networkID, connectionID) => {
  axios
    .post(`${API_BASE_URL}/fetch/connection-menu`, {
      userID: userID, 
      networkID: networkID, 
      connectionID: connectionID
    }).then(response => {
      viewData(response);
      return response.data;
    }).catch(err => {
      // TODO: Handle error methodology.
      console.log(err);
    });
}

/**
 * 
 * @param {*} response 
 */
const viewData = (response) => {
    console.log(response.data);
    console.log(response.status);
    console.log(response.statusText);
    console.log(response.headers);
    console.log(response.config);
};
