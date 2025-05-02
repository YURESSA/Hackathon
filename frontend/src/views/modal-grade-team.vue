<template>
  <div class="teams">
    <div class="page-wrapper">
    <div class="teams">
      <ul class="table-criteria">
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">1 критерий</p>
          <p class="table-criteria-item-grade">6</p>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">2 критерий</p>
          <p class="table-criteria-item-grade">4</p>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">3 критерий</p>
          <p class="table-criteria-item-grade">2</p>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">4 критерий</p>
          <p class="table-criteria-item-grade">10</p>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">5 критерий</p>
          <p class="table-criteria-item-grade">8</p>
        </li>
      </ul>
      <div class="grade">
        <p class="result">ИТОГО:</p>
        <p class="result-grade">30</p>
      </div>
      <div class="connection-feedback">
        <p class="text">Ваше решение выделилось креативным подходом и хорошей технической реализацией. Отличная работа с API и чистый код!
        Однако не хватило глубины проработки бизнес-модели – как решение будет монетизироваться или масштабироваться? Также в презентации можно было бы ярче показать пользовательский сценарий.</p>
        <IconButton class="button-pensil">
          <img class="icon-pensil" src="../assets/img/pensil.png">
        </IconButton>
      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
  import IconButton from '@/components/UI/iconButton.vue';
</script>

<style scoped>
  .input-field {
    height: 68px;
    background-color: rgba(246, 247, 248, 1);
    border: none;
    text-transform: uppercase;
  }



  .grade {
    margin-top: 35px;
    border: 1px solid rgba(74, 74, 74, 1);
    border-radius: 34px;
    display: flex;
    justify-content: space-between;
    padding: 0px 47px;
    height: 78px;
    font-size: 32px;
    color: rgba(74, 74, 74, 1);
    font-weight: bold;
    align-items: center;
    margin-bottom: 60px;
  }

  .button-pensil {
    position:absolute;
    right: 2%;
    top: 10%;
  }

  .text {
    width: 1153px;
    margin: 0 auto;
    font-size: 20px;
    color: rgba(74, 74, 74, 0.5);
  }
  .connection-feedback {
    display: flex;
    align-items: center;
    position: relative;
    height: 224px;
    background-color: rgba(146, 146, 146, 0.2);
    border-radius: 34px;
  }
  .table-criteria-item-grade {
    font-size: 32px;
    padding-bottom: 10px;
    max-width: 5%;
    font-weight: bold;
    text-align: center;
  }

  .table-criteria-item-count {
    font-size: 32px;
    color: rgba(74, 74, 74, 1);
  }

  .table-criteria-item:last-child {
    border:none;
  }

  .table-criteria-item{
    font-size: 20px;
    color: rgba(74, 74, 74, 1);
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
    padding: 0;
  }

  .case {
    font-size: 32px;
    color: rgba(74, 74, 74, 1);
    text-transform: uppercase;

  }

  .teams-title {

    font-size: 32px;
    color: rgba(74, 74, 74, 1);
    text-transform: uppercase;
  }

  .titles {
    padding-top: 40px;
    margin: auto;
    width: 1280px;
    display: flex;
    justify-content: space-between;
  }

  .teams {

    max-width: 1280px;
    margin: 0 auto;
  }

  .page-wrapper {
    margin: 30px auto;
    max-width: 100%;
    background-repeat: no-repeat;
    background-position: right top;
  }

  .header-profile {
    max-width: 1280px;
    margin: 0 auto;
  }
</style>
