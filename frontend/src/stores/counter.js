import { defineStore } from 'pinia'
import axios from 'axios';

export const baseUrl = 'http://localhost:5000'

export const useDataStore = defineStore('data', {
  state: () => ({
    token: "",
    userInfo: [],
    UserTeam: [],
  }),
  actions:{
    setToken(token) {
      this.token = token
      localStorage.setItem('token', token)
    },
    clearToken() {
      this.token = ""
      localStorage.removeItem('token')
    },
    async fetchProfile() {
      try {
        const response = await axios.get(`${baseUrl}/api/user/profile`, {
          headers: {
            Authorization: `Bearer ${this.token}`
          }
        }); // получаю данные пользователя
        this.userInfo = response.data;
      } catch (error) {
          console.error('Ошибка при получении данных:', error);
      }
    },
    async fetchMyTeam() {
      try {
        const response = await axios.get(`${baseUrl}/api/user/my-teams`, {
          headers: {
            Authorization: `Bearer ${this.token}`
          }
        }); // получаю данные команды юзера
        this.UserTeam = response.data;
      } catch (error) {
          console.error('Ошибка при получении данных:', error);
      }
    },
    async PutChangeRole(newRoleData) {  // Принимаем данные для отправки
      try {
        const response = await axios.put(
          `${baseUrl}/api/user/profile`,  // URL
          newRoleData,  // Тело запроса (ваши данные в формате JSON)
          {  // Конфиг с заголовками
            headers: {
              'Authorization': `Bearer ${this.token}`,
              'Content-Type': 'application/json'  // Явно указываем JSON
            }
          }
        );

        console.log(response)
        this.userInfo.role_name = newRoleData.role_name;
      } catch (error) {
        console.error('Ошибка при изменении данных:', error);
        throw error;  // Пробрасываем ошибку для обработки в компоненте
      }
    },
    async PutInTeam(newTeamUser, teamName) {  // Принимаем данные для отправки
      try {
        const response = await axios.put(
          `${baseUrl}/api/user/teams/${teamName}`,  // URL
          newTeamUser,  // Тело запроса (ваши данные в формате JSON)
          {  // Конфиг с заголовками
            headers: {
              'Authorization': `Bearer ${this.token}`,
              'Content-Type': 'application/json'  // Явно указываем JSON
            }
          }
        );

        console.log(response)
      } catch (error) {
        console.error('Ошибка при изменении данных:', error);
        throw error;
      }
    },
    async PutTeamData(newTeamUser, teamName) {  // Принимаем данные для отправки
      try {
        const response = await axios.put(
          `${baseUrl}/api/user/teams/${teamName}/artifacts`,  // URL
          newTeamUser,  // Тело запроса (ваши данные в формате JSON)
          {  // Конфиг с заголовками
            headers: {
              'Authorization': `Bearer ${this.token}`,
              'Content-Type': 'application/json'  // Явно указываем JSON
            }
          }
        );

        console.log(response)
      } catch (error) {
        console.error('Ошибка при изменении данных:', error);
        throw error;
      }
    },
    async DeletFromTeam(teamName) {  // Принимаем данные для отправки
      try {
        const response = await axios.delete(
          `${baseUrl}/api/user/teams/${teamName}`, {  // Конфиг с заголовками
            headers: {
              'Authorization': `Bearer ${this.token}`,
              'Content-Type': 'application/json'  // Явно указываем JSON
            }
          }
        );

        console.log(response)
      } catch (error) {
        console.error('Ошибка при изменении данных:', error);
        throw error;
      }
    },
    async PostCreateTeam(newTeamUser) {  // Принимаем данные для отправки
      try {
        const response = await axios.post(
          `${baseUrl}/api/user/teams`,  // URL
          newTeamUser,  // Тело запроса (ваши данные в формате JSON)
          {  // Конфиг с заголовками
            headers: {
              'Authorization': `Bearer ${this.token}`,
              'Content-Type': 'application/json'  // Явно указываем JSON
            }
          }
        );
        console.log(response)
      } catch (error) {
        console.error('Ошибка при изменении данных:', error);
        throw error;
      }
    },
  },
  getters: {
    getProfile: (state) => state.userInfo,
    getUserTeam: (state) => state.UserTeam
  },
  persist: {
    key: 'data-store',
    storage: window.localStorage,
    paths: ['userInfo', 'UserTeam', 'token']
  }
})
