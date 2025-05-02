<template>
  <button>{{ text }}</button>
</template>

<script setup>
import { defineProps } from 'vue';
defineProps({
  text: String,
})
</script>

<style scoped>
  button{
    width: 400px;
    height: 40px;

    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px 0;
    border: none;
    background-color: #D5D0F8;
    border-radius: 36px;

    font-family: 'Manrope';
    font-weight: bold;
    font-size: 20px;
    color: #4A4A4A;

    transition: all 0.25s ease;
    cursor: pointer;
  }

  button:active{
    background-color: #bbb0f8b9!important;
  }

  button:hover{
    background-color: #bbb0f8;
  }

  button:disabled{
    background-color: rgb(229, 213, 226);
    border: 1px solid #4A4A4A;
    cursor: auto;
  }
</style>
