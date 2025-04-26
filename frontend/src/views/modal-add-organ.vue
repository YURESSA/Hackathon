<template>
  <div class="add-orgn">
    <IconButton class="button-close"><img src="../assets/img/close.svg"></IconButton>
    <h3>добавить нового организатора</h3>
      <form>
        <label for="full_name">*ВАШЕ ФИО</label>
        <Input autocomplete="off" class="form-input" name="full_name"></Input>
        <label for="email">*Адрес электронной почты</label>
        <Input autocomplete="off" class="form-input" type="text" name="email"></Input>
        <label for="phone">*номер телефона</label>
        <Input autocomplete="off" class="form-input" type="text" name="phone"></Input>
        <label for="username">*ник в телеграм</label>
        <Input autocomplete="off" class="form-input" type="text" name="username"></Input>
        <label for="password">*Пароль</label>
        <Input autocomplete="off" class="form-input" type="password" name="password"></Input>
        <Button class="form-input" type="submit" text="добавить организатора"></Button>
      </form>
  </div>
</template>

<script setup>
  import IconButton from '@/components/UI/iconButton.vue';
  import Button from '@/components/UI/Button.vue';
  import Input from '@/components/UI/Input.vue';
</script>

<style scoped>
  .button-close {
    margin-left: 650px;
    padding-top: 0px;
  }

  h3 {
    text-transform: uppercase;
    text-align: center;
  }
  .add-orgn {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    width: 676px;
    margin: 0 auto;
    border-radius: 36px;
    padding: 50px;
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
    height: 78px;
    text-transform: uppercase;
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
