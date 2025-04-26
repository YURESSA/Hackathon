<template>
  <div class="role-page">
    <h1 class="page-title">Добавление в команду</h1>
      <Input
        v-model="userInput"
        class="role-input"
        id="role"
        placeholder="Введите username участника"
      ></Input>
    <Button
      class="save-button"
      @click="saveChanges"
      :disabled="!userInput.trim()"
      text="Добавить"
    ></Button>
  </div>
</template>

<script setup>
  import Input from '@/components/UI/Input.vue';
  import Button from '@/components/UI/Button.vue';
  import { ref, defineProps } from 'vue';
  const userInput = ref('');
  import { useDataStore } from '@/stores/counter';
  const props = defineProps({
    teamName: String,
  })

  function saveChanges(){
    const store = useDataStore();
    const newUser = userInput.value;
    const teamName = props.teamName;

    const jsonData = {
      team_name: teamName,
      username: newUser
    };

    store.PutInTeam(jsonData, teamName).then(() => {
      window.location.reload(); // Полная перезагрузка страницы
    });
  }
</script>

<style scoped>
.page-wrapper {
  max-width: 600px;
  margin: 30px auto;
}

.page-title {
  margin-top: 40px;
  margin-bottom: 15px;
  font-size: 16px;
  color: rgba(146, 146, 146, 1);
}

.role-page {
  position: absolute;
  height: 196px;
  width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-image: url('../assets/img/star-bottom.png');
  background-position: 260px 100px;
  background-color: rgba(233, 230, 255, 1);
  background-repeat: no-repeat;
  border-radius: 36px;

  top: 50%;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
}

.role-input-container {
  position: relative;
  margin-bottom: 30px;
}

.role-input {
  width: 400px;
  padding: 15px 20px;
  border: 2px solid #D5D0F8;
  border-radius: 10px;
  font-size: 16px;
  outline: none;
  transition: border-color 0.3s ease;

}

.role-input:focus {
  border-color: #A59BF7;
}

.save-button {
  font-size: 16px;
  width: 248px;
  height: 42px;
  position: absolute;
  right: 15px;
  margin-top: 26px;
}
</style>
