<template>
  <header class="profile-header">
    <router-link to="/">
      <div class="logo">
        <img class="profile-header-logo" src="../assets/img/logo.svg" alt="Логотип">
      </div>
    </router-link>
    <div class="profile">
      <a href="/admin">МАРИНА АКУЛОВА</a>
      <img src="../assets/img/icon-white.svg" class="icon" href="/team"></img>
    </div>
  </header>
</template>

<script setup>

</script>

<style scoped>
  .icon {
    width: 34px;
    height: 34px;
    border: 1px solid white ;
    border-radius: 100%;
  }

  .profile {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-right: 35px ;
  }

  .profile-header {
    position: relative;
    width: 100%;
    height: 65px;
    display: flex;
    font-weight: bold;
    background-color: rgba(74, 74, 74, 1);
    margin-bottom: 50px;
    justify-content: flex-end;
    border: solid 1px rgba(74, 74, 74, 1);
    border-radius: 36px;
    align-items: center;
  }

  .profile-header-logo {
    position: absolute;
    left: 30px;
    top: 13px;
  }

  .profile-header a {
    margin-right: 33px;
    font-size: 20px;
    color: rgba(255, 255, 255, 1);
  }
</style>
