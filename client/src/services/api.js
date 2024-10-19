import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export const fetchNetworkData = (userID, networkID) => {
  return axios.get(`${API_BASE_URL}/fetch_network`);
};

export const fetchNodeDetails = (userId) => {
  return axios.get(`${API_BASE_URL}/fecth_user/${userId}`);
};

export const isLogin = (email, password) => {
  return axios.post(`${API_BASE_URL}/validate_login`, { email, password });
}; //JSON Object (vaildLogin: true/false, userID: int)

export const createConnection = (userID, networkID) => {
  return axios.post(`${API_BASE_URL}/create_connection`, { userID, networkID });
};

export const updateConnection = (connectionID, networkID) => {
  return axios.post(`${API_BASE_URL}/update_connection`, { connectionID, networkID });
};

export const createNetwork = (userID, networkID) => {
  return axios.post(`${API_BASE_URL}/create_network`, { userID, networkID });
};
