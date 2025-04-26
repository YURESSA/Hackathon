<template>
  <div class="page-wrapper">
    <HeaderAdmin class="header-profile"></HeaderAdmin>
    <div class="teams">
      <h1 class="teams-title">Список команд, доступных для оценивания</h1>
      <ul class="case-list">
        <li class="grade-list-item">
          <p class="team">sss</p>
          <p class="case">Кейс  №1</p>
        </li>
        <li class="grade-list-item">
          <p class="team">wwww</p>
          <p class="case">Кейс  №2</p>
        </li>
        <li class="grade-list-item">
          <p class="team">qwer</p>
          <p class="case">Кейс  №2</p>
        </li>
        <li class="grade-list-item">
          <p class="team">,mnbb</p>
          <p class="case">Кейс  №3</p>
        </li>
      </ul>
    </div>
    <div class="teams">
      <h1 class="teams-title teams-title-grade">Оценённые команды:</h1>
      <ul class="teams-total-list">
        <li class="teams-total-item">
          <p class="item">sss</p>
          <p class="item">Кейс  №2</p>
          <div class="total">
            <p class="item">11/50</p>
            <IconButton class="button-arrow"><img src="../assets/img/arrow.svg"></IconButton>
          </div>
        </li>
        <li class="teams-total-item">
          <p class="item">wwww</p>
          <p class="item">Кейс  №1</p>
          <div class="total">
            <p class="item">30/50</p>
            <IconButton class="button-arrow"><img src="../assets/img/arrow.svg"></IconButton>
          </div>
        </li>
        <li class="teams-total-item">
          <p class="item">dddd</p>
          <p class="item">Кейс  №3</p>
          <div class="total">
            <p class="item">40/50</p>
            <IconButton class="button-arrow"><img src="../assets/img/arrow.svg"></IconButton>
          </div>

        </li>
      </ul>
    </div>
    <ModalGradeTeam/>
  </div>
</template>

<script setup>
  import HeaderAdmin from '@/components/header-admin.vue';
  import IconButton from '@/components/UI/iconButton.vue';
  import ModalGradeTeam from './modal-grade-team.vue';
</script>

<style scoped>
  /* .button-arrow {
    width: 23px;
    height: 13px;
  } */
  .total {
    display: flex;
    align-items: center;
  }
  .item {
    min-width: 120px;
  }

  .teams-total-item {
    border-bottom: 1px solid rgba(74, 74, 74, 1);
    height: 78px;
    display: flex;
    margin-bottom: 20px;
    padding: 0px 50px;
    justify-content: space-between;
    font-size: 32px;
    font-weight: bold;
    align-items: center;
  }
  .teams-total-list {
    list-style: none;
    padding: 0;
  }
  .teams-title-grade {
    margin-bottom: 60px;
  }
  .grades-teams {
    margin: 0 auto;
    margin-top: 20px;
    width: 1280px;
    color: rgba(74, 74, 74, 1);
    padding-top: 42px;
  }
  .team {
    text-transform: uppercase;
  }

  .grade-list-item {
    height: 78px;
    border: 2px solid rgba(74, 74, 74, 1);
    border-radius: 34px;
    display: flex;
    margin-bottom: 20px;
    padding: 0px 50px;
    justify-content: space-between;
    font-size: 32px;
    font-weight: bold;
    align-items: center;
  }
  .case-list {
    list-style: none;
    padding: 0;
  }

  .teams-title {
    text-transform: uppercase;
    font-size: 32px;
    margin-bottom: 26px;
  }
  .teams {
    margin: 0 auto;
    padding-top: 20px;
    margin-top: 20px;
    width: 1280px;
    color: rgba(74, 74, 74, 1);
    padding-bottom: 86px;
    margin-bottom: 15px;
  }
  .page-wrapper {
    width: 100%;
    margin: 0;
    padding: 0;
    background-image: url('../assets/img/background.png');
    background-size: cover;
    padding-top: 30px;
    min-height: 97vh;
  }

  .header-profile {
    max-width: 1280px;
    margin: 0 auto;
  }
</style>
