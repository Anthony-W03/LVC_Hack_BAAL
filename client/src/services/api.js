import axios from 'axios';
const API_BASE_URL = 'http://localhost:5000/api';

/**
 * 
 * @param {string} email 
 * @param {string} password 
 * @returns Json Object: {vaildLogin: boolean, userID: int}
 */
export const isLogin = (email, password) => {
  return axios.post(`${API_BASE_URL}/validate/login`, { email, password });
};

/**
 * 
 * @param {int} userId 
 * @returns Json Object: {'id': int, 'fname': string, 'lname': string, 'email': string}
 */
export const fetchUser = (userID) => {
  return axios.get(`${API_BASE_URL}/fetch/user/`, { userID });
};

/**
 * 
 * @param {int} userID 
 * @param {int} networkID 
 * @returns Json Object: {}
 */
export const fetchNetwork = (userID, networkID) => {
  return axios.get(`${API_BASE_URL}/fetch/network`, { userID, networkID });
};

/**
 * 
 * @param {int} userID
 * @returns Json Object: {}
 */
export const createNetwork = (userID) => {
  return axios.post(`${API_BASE_URL}/create/network`, { userID });
};


/**
 * 
 * @param {int} userId 
 * @returns Json Object: {'id': int, 'fname': string, 'lname': string, 'email': string}
 */
export const fetchConnection = (connID) => {
  return axios.get(`${API_BASE_URL}/fetch/connection/`, { connID });
};

/**
 * 
 * @param {int} connectionID 
 * @param {int} networkID 
 * @returns Json Object: {}
 */
export const updateConnection = (connectionID, networkID) => {
  return axios.post(`${API_BASE_URL}/update/connection`, { connectionID, networkID });
};

/**
 * 
 * @param {int} userID 
 * @param {int} networkID
 * 
 * @returns Json Object: {}
 */
export const createConnection = (networkID, email, fname, lname, source, target) => {
  return axios.post(`${API_BASE_URL}/create/connection`, { userID, networkID });
};

/**
 * 
 * @param {*} userID 
 * @param {*} networkID 
 * @param {*} connectionID 
 * @returns 
 */
export const fetchConnectionMenu = (userID, networkID, connectionID) => {
  return axios.get(`${API_BASE_URL}/fetch/connection-menu`, { userID, networkID, connectionID });
}
