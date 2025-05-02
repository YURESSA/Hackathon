<template>
  <div class="create-case">
    <IconButton class="button-close"><img src="../assets/img/close.svg"></IconButton>
    <h1 class="create-case-title">Создать кейс</h1>
    <form ref="userForm" method="post" @submit="handleSubmit" autocomplete="off">
      <label for="login">*название</label>
        <Input class="form-input" name="username"></Input>
      <label for="password">*краткое описание кейса</label>
        <Input type="password" name="password"></Input>
        <input
      type="file"
      id="file-input"
      ref="fileInput"
      class="visually-hidden"
      @change="handleFileSelect"
    >
    <!-- Кастомная кнопка -->
    <label for="file-input" class="custom-file-button">
      <span class="button-text">ПРИКРЕПИТЬ ПОДРОБНОЕ ТЗ</span>
    </label>
    </form>
    <Button text="ДОБАВИТЬ КЕЙС" class="button-save"></Button>
  </div>
</template>

<script setup>
  import IconButton from '@/components/UI/iconButton.vue';
  import Input from '@/components/UI/Input.vue';
  import Button from '@/components/UI/Button.vue';
</script>

<style scoped>
    .button-save {

    width: 494px;
    margin: 0 auto;
    font-size: 20;
    height: 70px;
  }
    .visually-hidden {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }

  /* Стили для кастомной кнопки */
  .custom-file-button {
    display: inline-flex;
    align-items: center;
    padding: 10px 20px;

    /* Полный сброс стилей кнопки */
    background: none;
    border: none;
    margin: 20px 0;
    font: inherit;
    cursor: pointer;
    outline: inherit;
    width: 97%;
    /* Кастомные стили */
    background-color: white;
    color: #4A4A4A;
    border-radius: 36px;
    border: 1px solid #4A4A4A;
    font-size: 16px;
    transition: background-color 0.3s ease;
  }

  .custom-file-button:hover {
    background-color: white;
  }

  .button-text {
    pointer-events: none; /* Чтобы клик работал на label, а не только на тексте */
  }
  label{
    font-size: 20px;
    text-transform: uppercase;
    width: 100%;
    align-items: start;
    padding-left: 15px;
  }

  form {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 20px;
  }
  .create-case-title {
    /* margin-top: 60px; */
    font-size: 32px;
    text-transform: uppercase;
  }
  .button-close {
    position: absolute;
    top: 5%;
    right: 2%;
    /* padding: 36px; */
  }
  .create-case {
    padding: 36px;
    position: relative;
    max-width: 1220px;
    height: 600px;
    margin: 0 auto;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border-radius: 17px;
  }
</style>




