import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

/**
 * 
 * @param {int} userID 
 * @param {int} networkID 
 * @returns 
 */
export const fetchNetworkData = (userID, networkID) => {
  return axios.get(`${API_BASE_URL}/fetch/network`);
};

/**
 * 
 * @param {int} userId 
 * @returns Json Object: {}
 */
export const fetchNodeDetails = (userId) => {
  return axios.get(`${API_BASE_URL}/fetch/user/${userId}`);
};

/**
 * 
 * @param {string} email 
 * @param {string} password 
 * @returns Json Object: {}
 */
export const isLogin = (email, password) => {
  return axios.post(`${API_BASE_URL}/validate/login`, { email, password });
}; //JSON Object (vaildLogin: true/false, userID: int)

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
 * @returns Json Object: {}
 */
export const createNetwork = (userID, networkID) => {
  return axios.post(`${API_BASE_URL}/create/network`, { userID, networkID });
};

/**
 * 
 * @param {int} userID 
 * @param {int} networkID 
 * @returns Json Object: {}
 */
export const createConnection = (userID, networkID) => {
  return axios.post(`${API_BASE_URL}/create/connection`, { userID, networkID });
};
