<template>
  <body class="page-wrapper">
  <div class="account-member">
    <Header >
    </Header>

    <div class="member-data">
      <h3>ДАННЫЕ УЧАСТНИКА</h3>

      <div class="member-info">
          <div class="member-info-icon">
            <img src="../assets/img/user.png" alt="">
          </div>
          <p class="member-info-name">{{ data.full_name }}</p>
      </div>

      <div class="member-details">
        <div class="detail-row detail-row-team">
          <p class="detail-label">Команда</p>
          <p class="detail-value" v-if="teamData.length > 0 && teamData[0].team_name">{{ teamData[0].team_name }}</p>
          <p class="detail-value" v-else>Вы пока не в команде</p>
        </div>

        <div class="detail-row detail-row-role button-div-class">
          <div class="role-content">
            <p class="detail-label">Роль в команде</p>
            <p class="detail-value">{{ data.project_role }}</p>
          </div>
          <IconButton class="btn">
            <img src="../assets/img/pencil.svg" @click="changeRole" alt="">
          </IconButton>
        </div>
      </div>
      <div class="find-team">
        <RouterLink to="/find-team" v-if="teamData.length === 0 || !teamData[0]?.team_name"><Button class="button-jem" text="Найти команду"></Button></RouterLink>
      </div>
      <Modal @close="modalOpen = false" v-if="modalOpen">
        <AccontMemberChangeRole />
      </Modal>
    </div>
  </div>
</body>
</template>

<script setup>
import Header from '@/components/header.vue';
import IconButton from '@/components/UI/iconButton.vue';
import Button from '@/components/UI/Button.vue';
import AccontMemberChangeRole from './accont-member-change-role.vue';
import Modal from '@/components/modal.vue';
import { useDataStore } from '@/stores/counter.js';
import { onMounted, computed, ref } from 'vue';

const store = useDataStore();
const data = computed(() => store.getProfile);
const teamData = computed(() => store.getUserTeam);




const modalOpen = ref(false);

console.log(data)

onMounted(() => {
  store.fetchProfile();
  store.fetchMyTeam();
})

function changeRole(){
  modalOpen.value = true;
}
</script>

<style scoped>

  .find-team{
    display: flex;
    justify-content: center;
    margin-top: 80px;
  }

  .button-jem {
    width: 494px;
    height: 78px;
    align-items: center;
    font-weight: bold;
    cursor: pointer;
  }


  .page-wrapper {
    margin: 30px auto;

    max-width: 1280px;
  }

  .account-member {
    font-family: Arial, sans-serif;

    background-color: rgba(255, 255, 255, 1);
  }

  .profile-header a {
    margin-right: 33px;
    font-size: 20px;
    color: rgba(255, 255, 255, 1);
  }

  .member-data h3 {
    font-size: 32px;
    margin-bottom: 30px;
    color: rgba(74, 74, 74, 1);
    margin-bottom: 30px;
  }

  .member-info {
    background-color: rgba(249, 249, 249, 1);
    border-radius: 34px;
    width: 100%;
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 50px;
    padding: 25px 0;
  }

  .member-info-icon {
    display: flex;
    align-items: center;
  }

  .member-info-name {
    line-height: 140%;
    color: rgba(74, 74, 74, 1);
    font-size: 32px;
    font-weight: bold;
    align-items: center;
  }

  .member-details {
    display: flex;
    justify-content: space-between;
  }

  .detail-row {
    background-repeat: no-repeat;
    font-weight: bold;
    min-width: 600px;
    min-height: 196px;
    border-radius: 36px;

    padding-left: 30px;
  }

  .btn{
    display: flex;
    align-items: start!important;
    margin: 40px 30px!important;
    width: max-content;
    height: max-content;
  }

  .detail-row-team {
    background-image: url('../assets/img/star-top.png');
    background-position: 260px -20px;
    background-color: rgba(226, 243, 153, 1);
  }

  .role-content{
    max-width: max-content;
  }

  .button-div-class{
    display: flex;
    justify-content: space-between;
  }

  .detail-row-role {
    background-image: url('../assets/img/star-bottom.png');
    background-position: 260px 50px;
    background-color: rgba(233, 230, 255, 1);
  }

  .detail-label {
    color: rgba(74, 74, 74, 1);
    font-size: 16px;
    margin-top: 40px;
    margin-bottom: 8px;
  }

  .detail-value {
    color: rgba(74, 74, 74, 1);
    font-size: 32px;
  }

  a{
    max-width: max-content;
  }
</style>

