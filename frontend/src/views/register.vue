<template>
  <div class="login-wrapper">
    <div class="login">
      <h3>ВХОД НА IT-ДЖЕМ "ИТы герой" 2025</h3>
      <form ref="userForm" method="post" @submit="handleSubmit" autocomplete="off">
        <label for="full_name">*ВАШЕ ФИО</label>
        <Input autocomplete="off" class="form-input" name="full_name"></Input>
        <label for="project_role">*РОЛЬ В КОМАНДЕ</label>
        <Input autocomplete="off" class="form-input" type="text" name="project_role"></Input>
        <label for="university">*ВУЗ</label>
        <Input autocomplete="off" class="form-input" type="text" name="university"></Input>
        <label for="study_info">*КУРС И НАПРАВЛЕНИЕ ОБУЧЕНИЯ</label>
        <Input autocomplete="off" class="form-input" type="text" name="study_info"></Input>
        <label for="email">*Адрес электронной почты</label>
        <Input autocomplete="off" class="form-input" type="text" name="email"></Input>
        <label for="phone">*номер телефона</label>
        <Input autocomplete="off" class="form-input" type="text" name="phone"></Input>
        <label for="username">*ник в телеграм</label>
        <Input autocomplete="off" class="form-input" type="text" name="username"></Input>
        <label for="password">*Пароль</label>
        <Input autocomplete="off" class="form-input" type="password" name="password"></Input>
        <Button class="form-input" type="submit" text="Зарегестрироваться"></Button>
      </form>
      <p>уже есть аккаунт? <router-link to="/login">Вход</router-link></p>
    </div>
  </div>
</template>

<script setup>
import Input from '@/components/UI/Input.vue';
import Button from '@/components/UI/Button.vue';
import axios from 'axios';
import { ref } from 'vue';
import {useRouter} from 'vue-router';
import {baseUrl} from '../stores/counter.js'
import { useDataStore } from '@/stores/counter';

const userForm = ref(null);
const router = useRouter();

function handleSubmit(event) {
  event.preventDefault();
  const formData = new FormData(userForm.value);
  const jsonData = Object.fromEntries(formData.entries());
  const dataStore = useDataStore();

  axios.post(`${baseUrl}/api/user/register`, jsonData, {
    headers: {
      'Content-Type': 'application/json' // Указываем JSON-формат
    }
  })
  .then(response => {
    dataStore.token = response.data.access_token;
    console.log(response)
    router.push('/login');
  })
  .catch(error => {
    console.error('Ошибка входа:', error.response?.data || error.message);
  });
}
</script>

<style scoped>
.login-wrapper{
  background-image: url('../assets/img/background.png');
  background-size: cover;
  min-width: 100%;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 30px;

  width: 70%;
  min-height: 720px;
  max-width: 1000px;

  padding: 40px;
  border-radius: 56px;
  border: 3px solid white;
  background-color: rgba(255, 255, 255, 0.40);
}

form{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
label{
  width: 100%;
  align-items: start;
  text-transform: uppercase;
  padding-left: 15px;
}

.form-input{
  margin-bottom: 20px;
}

Button{
  margin-top: 30px;
}

a{
  color: #D5D0F8;
}

p{
  text-transform: uppercase;
}
</style>
