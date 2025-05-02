<template>
  <div class="login-wrapper">
    <div class="login">
      <h3>ВХОД НА IT-ДЖЕМ "ИТы герой" 2025</h3>
      <form ref="userForm" method="post" @submit="handleSubmit" autocomplete="off">
        <label for="login">*Логин</label>
        <Input class="form-input" name="username"></Input>
        <label for="password">*Пароль</label>
        <Input type="password" name="password"></Input>
        <Button class="form-input" type="submit" text="Войти"></Button>
      </form>
      <p>У вас нет аккаунта? <router-link to="/register">зарегестрироваться</router-link></p>
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
  const store = useDataStore();

  axios.post(`${baseUrl}/api/user/login`, jsonData, {
    headers: {
      'Content-Type': 'application/json' // Указываем JSON-формат
    }
  })
  .then(response => {
    store.setToken(response.data.access_token);
    router.push('/');
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

p{
  text-transform: uppercase;
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

  border-radius: 56px;
  border: 3px solid white;
  background-color: rgba(255, 255, 255, 0.40);
}

form{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
label{
  width: 100%;
  align-items: start;
  padding-left: 15px;
}

.form-input{
  margin-bottom: 30px;
}

Button{
  margin-top: 30px;
}

a{
  color: #D5D0F8;
}
</style>
