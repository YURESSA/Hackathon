<template >
  <div class="page-wrapper">
    <Header class="header-profile"></Header>
    <div class="account-team-no">
      <div class="jem-info">
        <h1 class="jem-title">IT-ДЖЕМ  «ИТы Герой»</h1>
        <h2 class="jem-description">Присоединитесь к команде или создайте свою</h2>
        <div class="jem-buttons">
          <Button class="button-jem button-create" @click="openModal" text="СОЗДАТЬ КОМАНДУ"></Button>
          <Button class="button-jem button-find" text="НАЙТИ КОМАНДУ"></Button>
        </div>
      </div>
    </div>
    <Modal @close="modalOpen = false" v-if="modalOpen">
      <CreateTeam/>
    </Modal>
  </div>
</template>

<script setup>
  import Header from '@/components/header.vue';
  import Button from '@/components/UI/Button.vue';
  import Modal from '@/components/modal.vue';
  import CreateTeam from '@/components/createTeam.vue';
  import { ref } from 'vue';

  const modalOpen = ref(false)

  function openModal(){
    modalOpen.value = true;
  }
</script>

<style scoped>
  .page-wrapper {
    width: 100%;
    margin: 0;
    padding: 0;
    background-image: url('../assets/img/background.png');
    background-repeat: no-repeat;
    background-size: cover;
    padding-top: 30px;
  }

  .header-profile {
    max-width: 1280px;
    margin: 0 auto;
  }

  .account-team-no {
    font-family: Arial, sans-serif;
    max-width: 1280px;
    margin: 0 auto;
    background-color: rgba(255, 255, 255, 1);
    border-radius: 36px;
  }

  .jem-info {
    border-radius: 34px;
    margin-top: 30px;
    min-width: 1220px;
    min-height: 717px;
    padding-top: 40px;
  }

  .jem-title {
    margin-top: 40px;
    color: rgba(74, 74, 74, 1);
    font-size: 128px;
    margin: auto;
    margin-bottom: 100px;
    text-align: center;
  }

  .jem-description {
    text-align: center;
    text-transform: uppercase;
    color: rgba(74, 74, 74, 1);
    font-size: 36px;
    margin-bottom: 50px;
  }

  .jem-buttons {
    display: flex;
    width: 1020px;
    margin: 0 auto;
    justify-content: space-between;
  }

  .button-jem {
    width: 494px;
    height: 78px;
    align-items: center;
    font-weight: bold;
  }

  .button-find {
    background-color: rgba(226, 243, 153, 1);
  }
</style>

