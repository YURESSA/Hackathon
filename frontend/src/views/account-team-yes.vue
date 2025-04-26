<template>
  <AccountTeamNo v-if="!data || !data.length"/>
  <div class="page-wrapper" v-else>
    <Header class="header-profile"></Header>
    <div class="data-team">
      <div class="section-about">
        <h2 class="data-title">ДАННЫЕ О КОМАНДЕ</h2>
        <div class="team-info">
          <span class="team-name">{{data[0].team_name}}</span>
          <div class="members">
            <span class="members-count">{{membersCount}} из 5 участников</span>
            <IconButton @click="exitFromTeam"><img src="../assets/img/exit.svg"></IconButton>
          </div>
        </div>
      </div>
      <!-- Список участников -->
      <div class="section-members">
        <h2 class="members-title">Список участников</h2>
        <div class="members-list">
          <div class="member-item" v-for="user in data[0].members" :key="user.username">
            <p class="member-name">{{ user.full_name }}</p>
            <IconButton class="delete-btn"><img src="../assets/img/delete.svg" alt="Удалить"></IconButton>
          </div>
          <div class="button-interact">
            <Button class="button-jem" @click="changeRole" text="Добавить участника"></Button>
            <Button class="button-find" text="Найти участника команды"></Button>
          </div>
        </div>
      </div>
      <!-- Материалы проекта -->
      <div class="section-materials">
        <h2 class="materials-title">МАТЕРИАЛЫ ПРОЕКТА</h2>
        <div class="materials-list">
          <Input class="name-list-item" v-model="githubLink" placeholder="ПРИКРЕПИТЬ ССЫЛКУ НА GITHUB"></Input>
          <Input class="name-list-item" v-model="figmaLink" placeholder="ПРИКРЕПИТЬ ССЫЛКУ НА FIGMA"></Input>
          <Input class="name-list-item" v-model="presentationLink" placeholder="ПРИКРЕПИТЬ ССЫЛКУ НА ПРЕЗЕНТАЦИЮ"></Input>
          <Input class="name-list-item" v-model="hostLink" placeholder="ПРИКРЕПИТЬ ССЫЛКУ НА ХОСТИНГ"></Input>
          <Input class="name-list-item" v-model="artifactsLink" placeholder="ПРИКРЕПИТЬ ССЫЛКУ НА АРТЕФАКТЫ"></Input>
        </div>
        <div class="actions">
          <Button class="save-btn" @click="saveData" text="СОХРАНИТЬ"></Button>
          <Button class="cancel-btn" @click="cancel" text="ОТМЕНИТЬ"></Button>
        </div>
      </div>
    </div>
  </div>

  <Modal @close="modalOpen = false" v-if="modalOpen">
    <AddToTeam :team-name="data[0].team_name"/>
  </Modal>
</template>

<script setup>
  import Header from '@/components/header.vue';
  import Button from '@/components/UI/Button.vue';
  import IconButton from '@/components/UI/iconButton.vue';
  import Input from '@/components/UI/Input.vue';
  import AccountTeamNo from './account-team-no.vue';
  import Modal from '@/components/modal.vue';
  import AddToTeam from '@/components/addToTeam.vue';
  import { useDataStore } from '@/stores/counter.js';

  import { onMounted, ref, computed, watch } from 'vue';

  const store = useDataStore();
  const data = computed(() => store.getUserTeam);
  const membersCount = computed(() => {
    if (!data.value || !data.value.length || !data.value[0].members) return 0;
    return data.value[0].members.length;
  });

  function changeRole(){
    modalOpen.value = true;
  }

  onMounted(() => {
    store.fetchMyTeam();
  })

  const modalOpen = ref(false);


// Реактивные ссылки с проверками
const githubLink = ref('');
const figmaLink = ref('');
const presentationLink = ref('');
const hostLink = ref('');
const artifactsLink = ref('');

// Обновляем ссылки при изменении data
watch(data, (newData) => {
  if (newData?.length > 0 && newData[0]?.artifacts) {
    const artifacts = newData[0].artifacts;
    githubLink.value = artifacts.github_url || '';
    figmaLink.value = artifacts.figma_url || '';
    presentationLink.value = artifacts.presentation_url || '';
    hostLink.value = artifacts.hosting_url || '';
    artifactsLink.value = artifacts.extra_links || '';
  }
}, { immediate: true });


  function saveData(){
    const store = useDataStore();

    const teamName = data.value[0].team_name;
    const jsonData = {
      "github_url": githubLink.value,
      "figma_url": figmaLink.value,
      "hosting_url": hostLink.value,
      "presentation_url": presentationLink.value,
      "extra_links": artifactsLink.value
    }

    store.PutTeamData(jsonData, teamName).then(() => {
      window.location.reload();
    });
  }

  function cancel(){
    const github = data.value[0].artifacts.github_url;
    const figma = data.value[0].artifacts.figma_url;
    const presentation = data.value[0].artifacts.presentation_url;
    const host = data.value[0].artifacts.hosting_url;
    const artifacts = data.value[0].artifacts.extra_links;


    githubLink.value = github;
    figmaLink.value = figma;
    presentationLink.value = presentation;
    hostLink.value = host;
    artifactsLink.value = artifacts;
  }

  function exitFromTeam(){
    const teamName = data.value[0].team_name;
    store.DeletFromTeam(teamName).then(() => {
      window.location.reload();
    });
  }

</script>

<style scoped>
  .section-materials {
    margin-bottom: 45px;
  }

  .button-interact{
    display: flex;
    flex-direction: column;
    width: 100%;
    align-items: center;
    gap: 25px;
    margin-top: 50px;
  }

  .button-jem {
    width: 494px;
    height: 78px;
    align-items: center;
    font-weight: bold;
    cursor: pointer;
  }

  .button-find {
    background-color: rgba(226, 243, 153, 1);
    text-transform: uppercase;
    width: 494px;
    height: 78px;
    font-weight: bold;
  }

  .actions {
    display: flex;
    width: 1020px;
    justify-content: space-between;
    margin: auto;
    margin-bottom: 35px;
  }

  .save-btn {
    height: 78px;
  }

  .cancel-btn {
    height: 78px;
    background-color: white;
    border: 1px solid rgba(74, 74, 74, 1);
  }

  .name-list-item:last-child {
    margin-bottom: 30px;
  }

  .name-list-item {
    margin-bottom: 20px;
    height: 78px;
  }

  .materials-title {
    font-size: 32px;
    color: rgba(74, 74, 74, 1);
    text-transform: uppercase;
    margin-top: 15px;
    margin-bottom: 30px;
  }

  .member-name {
    font-size: 32px;
    line-height: 140%;
    margin: 0;
    padding: 0;
    margin-top: 20px;
  }
  .member-item {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(74, 74, 74, 0.5);
  }

  .members-list {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
  }

  .members-title {
    margin-top: 30px;
    font-size: 16px;
    color: rgba(74, 74, 74, 1);
    text-transform: uppercase;
  }
  .section-members {
    margin-top: 30px;
    margin-bottom: 70px;
  }

  .members {
    display: flex;
    justify-content: space-between;
    min-width: 366px;
  }

  .team-name {
    font-size: 32px;
    font-weight: bold;
    color: rgba(74, 74, 74, 1);
  }

  .members-count {
    font-size: 32px;
    font-weight: bold;
    color: rgba(74, 74, 74, 1);
    justify-content: end;
    line-height: 140%;
  }

  .page-wrapper {
    background-image: url('../assets/img/background.png');
    background-repeat: no-repeat;
    background-size: cover;
    margin: 0;
    padding: 0;
    width: 100%;
    padding-top: 30px;
    min-height: 96vh;
  }

  .header-profile {
    max-width: 1280px;
    margin: 0 auto;
    margin-bottom: 20px;
  }

  .data-team {
    margin: 0 auto;
    margin-top: 40px;
    max-width: 1280px;
  }

  .data-title {
    font-size: 32px;
    font-weight: bold;
    color: rgba(74, 74, 74, 1);
    margin-bottom: 80px;
  }

  .team-info {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(174, 174, 174, 1);
  }
</style>
