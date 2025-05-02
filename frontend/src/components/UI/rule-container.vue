<template>
  <div class="rule">
    <h3>Кейс <br> объявляется <br> в день старта</h3>
    <h2>01</h2>
    <slot></slot>
  </div>
</template>

<style scoped>
.rule{
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: #E2F399;
  width: 40%;
  height: 30%;
  padding: 60px 30px;
  color: #4A4A4A;
  border-radius: 36px;
}

img{
  width: 245px;
  height: 245px;
}

h2{
  text-align: end;
}
</style>
