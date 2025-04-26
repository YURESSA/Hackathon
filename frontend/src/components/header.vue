<template>
  <header class="profile-header">
    <router-link to="/">
      <div class="logo">
        <img class="profile-header-logo" src="../assets/img/logo.svg" alt="Логотип">
      </div>
    </router-link>
    <div class="navigation">
      <n-dropdown :options="options" @select="handleSelect">
        <n-button>Профиль</n-button>
      </n-dropdown>
      <a href="/team-account">КОМАНДА</a>
    </div>
  </header>
</template>

<script setup>
import { useRouter } from 'vue-router'
import LogOutOutline from "@vicons/ionicons5/LogOutOutline"
import PersonCircleOutline from "@vicons/ionicons5/PersonCircleOutline"
import { NButton, NDropdown, NIcon } from 'naive-ui'
import { h } from "vue";
import { useDataStore } from "@/stores/counter";

const store = useDataStore();
const router = useRouter()

const renderIcon = (icon) => {
  return () => h(NIcon, null, { default: () => h(icon) });
};

const options = [
  {
    label: "Профиль",
    key: "profile",
    icon: renderIcon(PersonCircleOutline)
  },
  {
    label: "Выйти",
    key: "logout",
    icon: renderIcon(LogOutOutline)
  }
];

const handleSelect = async (key) => {
  switch(key) {
    case 'profile':
      await router.push('/account')
      break;
    case 'logout':
      await store.clearToken() // Ожидаем очистки токена
      await router.push('/login')
      break;
  }
};
</script>

<style scoped>
  .profile-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    font-weight: bold;
    background-color: rgba(74, 74, 74, 1);
    margin-bottom: 50px;
    border-radius: 36px;
    padding: 10px 30px;
  }

  .navigation{
    display: flex;
    gap: 30px;
  }

  .profile-header a {
    font-size: 20px;
    color: rgba(255, 255, 255, 1);
  }

:deep(.n-button__content){
  color: white;
  text-transform: uppercase;
  font-size: 20px;
  font-weight: bold;
}

:deep(.n-button__border, .--n-border-hover){
  border: none;
}
</style>

