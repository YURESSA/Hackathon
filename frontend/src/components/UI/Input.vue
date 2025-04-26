<template>
  <input
  type="text"
  :value="modelValue"
  @input="$emit('update:modelValue', $event.target.value)">
</template>

<script setup>
defineProps(['modelValue'])
defineEmits(['update:modelValue'])
</script>

<style scoped>
input {
  box-sizing: border-box;
  border: 1px solid #4a4a4a;
  border-radius: 36px;
  width: 100%;
  height: 40px;
  padding: 5px 20px;
  font-size: 20px;
  transition: all 0.1s ease;
  outline: none;
}

input:hover {
  border: 3px solid #d5d0f8;
}

input:focus {
  border: 3px solid #d5d0f8;
}


</style>
