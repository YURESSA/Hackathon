<template>
  <div class="page-wrapper">
    <Header class="main-header"></Header>
    <main>
      <div class="title-wrapper">
        <img class="star-image" src="../assets/img/big-star.svg" alt="">
        <div class="title">
          <p>
            25-26 АПРЕЛЯ 2025 <br>
            ЕКАТЕРИНБУРГ
          </p>
          <h1>
            <img src="../assets/img/litle-star.svg" alt="">
            IT-ДЖЕМ <br>
            «ИТы Герой»
          </h1>
        </div>
      </div>
      <div class="hacaton-info">
        <div class="star-img">
          <img src="../assets/img/litle-star-fill.svg" alt="">
        </div>
        <div class="info-content">
          <p class="size__36">IT-Джем — это аналог хакатона, где команды за 1-2 дня создают MVP по кейсу, который объявляют в начале. Название отсылает к музыкальным джем-сейшнам: здесь так же ценятся импровизация, драйв и неформальная атмосфера</p>
        </div>
      </div>
      <h2>Этапы хакатона "ИТы Герой"</h2>
      <div class="time-line">
        <div class="day-line">
          <div class="data-title">
            <div class="data">25 апреля</div>
            <p class="size-36">Первый день</p>
          </div>
          <ul>
            <li>Открытие дня - в 11.00</li>
            <li>В течение всего дня (с 10 до 20 ч.) будет поддержка в ТГ- <br>
              чате и в телемосте (ссылку скинем в чат)</li>
          </ul>
        </div>
        <div class="day-line">
          <div class="data-title">
            <div class="data">26 апреля</div>
            <p class="size-36">Второй день</p>
          </div>
          <div class="data-time-line">
            <ul>
              <li>10:30 - Welcome-кофе</li>
              <li>11:00  - 11:15 - Открытие</li>
              <li>11:15   - 13:15 - Защита первого потока. Кейс 1</li>
              <li>13:15  -13:30 - кофе-брейк</li>
              <li>13:30 - 15:30 - Защита второго потока. Кейс 2</li>
              <li>15:30 - 15:45 - кофе-брейк</li>
              <li>15:45 - 17:45 - Защита третьего потока. Кейс 3</li>
              <li>17:45 - 18:00 - Подведение итогов и награждение</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="hacaton-rules">
        <h2>Правила IT-Джема</h2>
        <div class="rules">
          <div class="rules-content-first">
            <h3>Кейс <br> объявляется <br> в день старта</h3>
            <h2>01</h2>
            <img src="../assets/img/rule-star-big.svg" class="star-up" alt="">
            <img src="../assets/img/rule-star-small.svg" class="star-down" alt="">
          </div>
          <div class="all-rules">
            <div class="rule">
              <h3>Визуал-дашборд</h3>
              <h2>02</h2>
            </div>
            <div class="rule black-rule">
              <h3>MVP (минимально <br> рабочий прототип)</h3>
              <h2>03</h2>
              <img src="../assets/img/rule-star-small.svg" alt="">
            </div>
            <div class="rule white-rule">
              <h3>Дедлайн презентация до 10:00 <br> 26 апреля</h3>
              <h2>04</h2>
            </div>
            <div class="rule sereniv-rule">
              <h3>Презентация (2-5 <br> минут)</h3>
              <h2>05</h2>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import Header from '@/components/header.vue';

</script>


<style scoped>
  .page-wrapper{
    padding: 1rem;
  }

  .data-title{
    display: flex;
    align-items: center;
    gap: 20px;
  }

  main{
    display: flex;
    flex-direction: column;
    gap: 80px;
  }
  .main-header{
    position: absolute;
    width: 95%;
    background: none;
    z-index: 10;
  }

  .star-image{
    position: absolute;
    top: 0px;
  }

  .hacaton-rules{
    display: flex;
    flex-direction: column;
    gap: 30px;
    margin-bottom: 50px;
  }

  .title-wrapper{
    width: 97%;
    height: 700px;

    display: flex;
    align-items: flex-end;

    background-color: #4A4A4A;
    background-image: url('../assets/img/main-background.svg');
    background-size: cover;
    overflow: hidden;
    border-radius: 30px;

    padding: 25px 30px;

    color: white;
  }

  h1{
    position: relative;
  }

  h1 > img{
    position: absolute;
    top: 10px;
    right: 50px;
  }

  .hacaton-info{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 50px;
  }

  .info-content > p{
    text-transform: uppercase;
    line-height: 140%;
    text-align: center;
  }

  .time-line{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 80px;

  }

  h2{
    text-align: center;
    text-transform: uppercase;
  }

  .day-line{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    text-transform: uppercase;
    gap: 30px;
    width: 80%;
  }

  .data{
    color: white;
    padding: 10px 30px;
    background-color: #D5D0F8;
    border-radius: 36px;
  }

  ul, ol {
    list-style-type: none;
    padding-left: 0; /* Дополнительно убираем отступ слева */
  }

  li:not(:last-of-type){
    padding-bottom: 10px;
  }

  .rules{
    display: flex;
    gap: 20px;
    width: 100%;
  }

  .rules > *{
    flex-grow: 1;
  }

  .rules-content-first{
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: #4A4A4A;
    /* max-width: 40%; */
    padding: 60px 30px;
    height: 550px;
    color: white;
    border-radius: 36px;
  }

  .rules-content-first > h2{
    text-align: end;
  }

  .star-up{
    position: absolute;
    top: 0px;
    right: 0px;
  }

  .star-down{
    position: absolute;
    bottom: 0px;
    left: 0px;
  }

  .all-rules{
    display: flex;
    flex-wrap: wrap;
    width: 60%;
    gap: 20px;
  }

  .rule{
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: #E2F399;
  width: 44%;
  height: 30%;
  padding: 60px 30px;
  color: #4A4A4A;
  border-radius: 36px;
}

  .rule > h2{
    text-align: end;
  }

  .rule > img{
    position: absolute;
    bottom: -100px;
    left: -20px;
    width: 245px;
    height: 245px;
  }

  .black-rule{
    background-color: #4A4A4A;
    color: white;
  }

  .sereniv-rule{
    background-color: #BAB6D7;
    color: white;
  }

  .white-rule{
    background-color: #F6F6F6;
    color: #4A4A4A;
  }
</style>
