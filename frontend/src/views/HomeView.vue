<template>
  <div class="account-member">
    <div class="profile-header">
      <h1>Хуй</h1>
      <h2>КОМАНДА</h2>
    </div>

    <div class="member-data">
      <h3>ДАННЫЕ УЧАСНИКА</h3>

      <div class="member-info">
        <div class="member-name">
          <p>- {{ member.fullName }}</p>
        </div>

        <div class="member-details">
          <div class="detail-row">
            <span class="detail-label">Команда</span>
            <span class="detail-value">{{ member.team }}</span>
          </div>

          <div class="detail-row">
            <span class="detail-label">Роль экипажа</span>
            <span class="detail-value">{{ member.role }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      member: {
        fullName: 'Акулова Марина Денисовна',
        team: 'WAC&D',
        role: 'Тиминд'
      }
    }
  }
}
</script>

<style scoped>
.account-member {
  font-family: Arial, sans-serif;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.profile-header {
  margin-bottom: 30px;
  text-align: center;
}

.profile-header h1 {
  font-size: 24px;
  margin-bottom: 5px;
}

.profile-header h2 {
  font-size: 20px;
  color: #555;
}

.member-data h3 {
  font-size: 18px;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

.member-name {
  font-size: 16px;
  margin-bottom: 15px;
}

.detail-row {
  display: flex;
  margin-bottom: 10px;
}

.detail-label {
  font-weight: bold;
  width: 120px;
}

.detail-value {
  flex-grow: 1;
}
</style>

