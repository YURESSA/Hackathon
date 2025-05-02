<template>
  <div class="modal-wrapper" @click.self="closeModal">
    <slot></slot>
  </div>
</template>

<script setup>
const emit = defineEmits(['close'])

const closeModal = () => {
  emit('close')
}
</script>

<style scoped>
.modal-wrapper{
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(63, 58, 58, 0.733);
}
</style>
