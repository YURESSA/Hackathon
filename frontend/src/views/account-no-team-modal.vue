<template id="create-team">
  <div class="container-create-team">
    <IconButton class="close-button"><img src="../assets/img/close.svg"></IconButton>
    <div class="form-name-team">
      <span class="name-team">*НАЗВАНИЕ КОМАНДЫ</span>
      <Input class="input-team"></Input>
      <Button class="button-team" text="СОЗДАТЬ КОМАНДУ"></Button>
    </div>
  </div>
</template>

<script setup>
  import Button from '@/components/UI/Button.vue';
  import Input from '@/components/UI/Input.vue';
  import IconButton from '@/components/UI/iconButton.vue';
</script>

<style scoped>
  .container-create-team {
    position: relative;
    max-width: 538px;
    height: 340px;
    margin: 30px auto;
    box-shadow: 0 4px 12px rgba(74, 74, 74, 0.2);
    border-radius: 34px;
  }

  .close-button {
    width: 23px;
    height: 23px;
    position: absolute;
    background-color: rgba(237, 237, 237, 0.54);
    right: 36px;
    top: 36px;
  }

  .form-name-team {
    position: absolute;
    top: 102px;
    width: 494px;
    right: 36px;
  }

  .name-team {
    color: rgba(74, 74, 74, 1);
    font-size: 20px;
  }

  .input-team {
    margin-top: 10px;
  }

  .button-team {
    color: rgba(74, 74, 74, 1);
    font-size: 16px;
    margin: 0 auto;

    margin-top: 30px;
  }

</style>
