<template>
  <div class="page-wrapper">
    <HeaderAdmin class="profile-header"></HeaderAdmin>
    <div class="organisators">
      <h1 class="organisators-title">ОРГАНИЗАТОРЫ</h1>
      <ul class="table">
        <li class="table-org-item">
          <p class="tabel-item header-tabel-item ">ФИО</p>
          <p class="tabel-item header-tabel-item">ПОЧТА</p>
          <p class="tabel-item header-tabel-item">ТГ АККАУНТ</p>
          <p class="tabel-item header-tabel-item">НОМЕР</p>
          <p class="tabel-item tabel-item_delete"></p>
        </li>
        <li class="table-org-item">
          <p class="tabel-item">фамилия имя отчетво</p>
          <p class="tabel-item">abcd@dd.ru</p>
          <p class="tabel-item">lox</p>
          <p class="tabel-item">89122351621</p>
          <p class="tabel-item tabel-item_delete"><IconButton class="button"><img img src="../assets/img/delete.svg"></IconButton></p>
        </li>
        <li class="table-org-item">
          <p class="tabel-item">фамилия имя отчетво</p>
          <p class="tabel-item">abcd@dd.ru</p>
          <p class="tabel-item">lox</p>
          <p class="tabel-item">89122351621</p>
          <p class="tabel-item tabel-item_delete"><IconButton class="button"><img img src="../assets/img/delete.svg"></IconButton></p>
        </li>
        <Button class="open-button" text="Развернуть"></Button>
      </ul>

    </div>
    <div class="buttons">
      <Button text="добавить организатора" class="button-add button-add_org"></Button>
      <Button text="добавить кейс" class="button-add button-add_case"></Button>
      <Button text="распределить кейсы" class="button-add button-distribute_case"></Button>
    </div>
  </div>
  <ModalCaseTeam/>
  <ModalAddOrgan/>
</template>

<script setup>
  import HeaderAdmin from '@/components/header-admin.vue';
  import Button from '@/components/UI/Button.vue';
  import IconButton from '@/components/UI/iconButton.vue';
  import ModalCaseTeam from './modal-case-team.vue';
  import ModalAddOrgan from './modal-add-organ.vue';
</script>

<style scoped>
  .button-add_case {
    background-color: rgba(226, 243, 153, 1);
  }
  .button-distribute_case{
    background-color: rgb(255, 89, 77);
  }
  .button-add {
    width: 495px;
    height: 78px;
    font-size: 20px;
    text-transform: uppercase;
    color: rgba(74, 74, 74, 1)
  }

  .buttons {
    width: 1020px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
  }

  .open-button {

    background-color: rgba(213, 213, 213, 1);
    margin: 30px auto 0;
  }

  .button {
    width: 50px;
  }

  .tabel-item_delete {
    width:70px !important;
  }

  .tabel-item {
    width: 300px;
    margin: auto;
    border-right: 1px solid rgba(174, 174, 174, 1);
    text-align: center;

  }
  .table-org-item {
    align-items: center;
    height: 64px;
    max-width: 1200px;
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(174, 174, 174, 1);
  }
  .table {
    list-style: none;
    padding-bottom: 47px;
    margin-bottom: 30px;
    background-color: rgba(249, 249, 249, 1);
    border-radius: 34px;
    margin-bottom: 0;
  }

  .organisators-title {
    font-size: 32px;
    color: rgba(74, 74, 74, 1);
  }

  .organisators {
    max-width: 1280px;
    margin: 30px auto;
  }

  .page-wrapper {

    background-repeat: no-repeat;
    margin: 0;
    padding: 0;
    background-position: right;
    width: 100%;
    padding-top: 30px;
  }

  .profile-header {
    max-width: 1280px;
    margin: 0 auto;
    margin-bottom: 20px;
  }
</style>


