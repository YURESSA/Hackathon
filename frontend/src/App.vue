<template>
  <router-view />
  <IconButton @click="openTelegram" class="tg-bot"><img src="./assets/img/icons8-телеграм.svg" alt=""></IconButton>
</template>

<script setup>
import IconButton from './components/UI/iconButton.vue';

function openTelegram(){
  window.open('https://t.me/hahahahahahahahahahton_Bot', '_blank')
}
</script>

<style scoped>
.tg-bot{
  position: fixed;
  bottom: 20px;
  right: 40px;
}
</style>
