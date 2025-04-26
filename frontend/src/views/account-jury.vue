<template>
  <div class="page-wrapper">
    <Header class="header-profile"></Header>
    <div class="teams">
      <div class="titles">
        <h1 class="teams-title">команда BugSlayers</h1>
        <h1 class="case">кейс №3</h1>
      </div>
      <ul class="table-criteria">
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">1 критерий</p>
          <Input class="table-criteria-item-grade" placeholder="4"></Input>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">2 критерий</p>
          <Input class="table-criteria-item-grade" placeholder="2"></Input>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">3 критерий</p>
          <Input class="table-criteria-item-grade" placeholder="10"></Input>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">4 критерий</p>
          <Input class="table-criteria-item-grade" placeholder="6"></Input>
        </li>
        <li class="table-criteria-item">
          <p class="table-criteria-item-count">5 критерий</p>
          <Input class="table-criteria-item-grade" placeholder="8"></Input>
        </li>
      </ul>
      <Input class="input-field" placeholder="оставить обратную связь"></Input>
      <div class="grade">
        <p class="result">ИТОГО:</p>
        <p class="result-grade">30</p>
      </div>
      <Button text="СОХРАНИТЬ" class="button-save"></Button>
    </div>
  </div>
</template>

<script setup>
  import Header from '@/components/header.vue';
  import Button from '@/components/UI/Button.vue';
  import Input from '@/components/UI/Input.vue';
</script>

<style scoped>
  .button-save {
    width: 494px;
    margin:50px auto;
    font-size: 20;
    height: 78px;
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
  }

  .table-criteria-item-grade {
    padding-bottom: 10px;
    max-width: 5%;
    font-size: 20px;
    color: rgba(74, 74, 74, 1);
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
    background-image: url('../assets/img/star-top-right.png');
    background-repeat: no-repeat;
    background-position: right top;
  }

  .header-profile {
    max-width: 1280px;
    margin: 0 auto;
  }
</style>
