<template>
  <div class="page-wrapper">
    <header>
      <nav>
        <a>ПРОФИЛЬ</a>
        <a>КОМАНДА</a>
      </nav>
      <h1>IT-Джем  «ИТы Герой»</h1>
    </header>
    <div class="find-teams">
      <h2>ПОИСК КОМАНДЫ</h2>
      <div class="buttons">
        <Button text="НАЙТИ КОМАНДУ" class="button buttons_find-teams"></Button>
        <Button text="НАЙТИ УЧАСТНИКА В КОМАНДУ" class="button buttons_find-member"></Button>
      </div>
    </div>
    <div class="block-find">
      <h3 class="title-find">УЧАСТНИКИ БЕЗ КОМАНДЫ</h3>
      <ul class="table-criteria">
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">ФИО</p>
          <p class="table-criteria-item-grade">ПОЧТА</p>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">аа</p>
          <p class="table-criteria-item-grade">ss12</p>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">ff</p>
          <p class="table-criteria-item-grade">aqwe</p>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">ddd</p>
          <p class="table-criteria-item-grade">qwevb</p>
        </li>
        <Button class="open-button" text="Развернуть"></Button>
      </ul>
    </div>
    <div class="block-find">
      <h3 class="title-find">КОМАНДЫ БЕЗ УЧАСТНИКОВ</h3>
      <ul class="table-criteria">
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">ФИО</p>
          <p class="table-criteria-item-grade">ПОЧТА</p>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">аа</p>
          <p class="table-criteria-item-grade">ss12</p>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">ff</p>
          <p class="table-criteria-item-grade">aqwe</p>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">ddd</p>
          <p class="table-criteria-item-grade">qwevb</p>
        </li>
        <Button class="open-button" text="Развернуть"></Button>
      </ul>
    </div>
  </div>
</template>

<script setup>
  import Button from '@/components/UI/Button.vue';
</script>

<style scoped>
  .block-find {
    margin-bottom:116px;
  }
  .open-button {
    text-transform: uppercase;
    margin: 30px auto 47px;
    background-color: rgba(213, 213, 213, 1);
  }

  .table-criteria-item-grade {
    width: 855px;
    padding-bottom: 10px;
    font-size: 32px;
    color: rgba(74, 74, 74, 1);
    font-weight: bold;
    text-align: start;
  }

  .table-criteria-item-count {
    font-weight: bold;
    text-align: center;
    width: 25%;
    font-size: 32px;
    color: rgba(74, 74, 74, 1);
    border-right: 1px solid rgba(74, 74, 74, 1);
  }

  .table-criteria-item:last-child {

    border:none;
  }

  .table-criteria-item{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0;
    padding: 0;
    border-bottom: 1px solid rgba(74, 74, 74, 1);

  }

  .table-criteria {
    list-style: none;
    margin: 0 auto;
    width: 1280px;
    padding-bottom: 47px;

    max-width: 1220px;
  }

  .table-criteria {
    list-style: none;
  }
  .table-criteria {
    background-color: rgba(249, 249, 249, 1);
    border-radius: 36px;
  }
  .title-find {
    font-size: 32px;
    color: rgba(74, 74, 74, 1);
    margin-bottom: 32px;
  }
  .buttons_find-member {
    background-color: rgba(226, 243, 153, 1);
  }
  .button {
    width: 494px;
    height: 78px;
  }
  .buttons {
    display: flex;
    font-size: 36px;
    text-transform: uppercase;
    width: 1020px;
    justify-content: space-between;
    margin: 0 auto;
  }

  h2 {
    text-align: center;
    margin-bottom: 32px;
  }
  .find-teams {
    margin: 32px auto 113px;
  }

  h1 {
    font-size: 128px;
    color: white;
    text-align:center;
  }

  nav {
    display: flex;
    justify-content: end;
    font-size: 20px;
    color: white;
    gap: 50px;
  }
  header {
    padding: 30px 30px;
    margin: 0 auto;
    height: 497px;
    background-color: rgba(74, 74, 74, 1);
    background-image: url("../assets/images/background2.png");
    background-repeat: no-repeat;
    background-size: cover;
    border-radius: 36px;
  }
  .page-wrapper{
    max-width: 1220px;
    margin: 30px auto;
  }
</style>
