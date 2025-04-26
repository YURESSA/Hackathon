<template>
  <button class="icon-button">
    <slot></slot>
  </button>
</template>

<script setup>

</script>

<style scoped>
.icon-button {
  width: max-content;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  border: none;
  background-color: transparent;
  border-radius: 10px;
  transition: all 0.25s ease;
  cursor: pointer;
}

.icon-button:hover {
  background-color: rgba(196, 174, 174, 0.514);
}

.icon-button:active{
  background-color: rgba(196, 174, 174, 0.267);
}

.icon-button img {
  width: 27px;
  height: 27px;
}
</style>
