import axios from 'axios';

const API_URL = 'http://localhost:8000/';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

const authAPI = {
  register(data) {
    return api.post('auth/users/', data);
  },

  login(data) {
    return api.post('auth/token/login/', data);
  },

  // Выход
  logout() {
    return api.post('auth/token/logout/');
  },

  // Получение информации о текущем пользователе
  getCurrentUser() {
    return api.get('auth/users/me/');
  },
};

export default authAPI;