import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export const fetchGraphData = () => {
  return axios.get(`${API_BASE_URL}/graph`);
};

export const fetchNodeDetails = (nodeId) => {
  return axios.get(`${API_BASE_URL}/node/${nodeId}`);
};