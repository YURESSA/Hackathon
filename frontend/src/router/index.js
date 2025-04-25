import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AccountMember from '@/views/account-member.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/main',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/account',
      name: 'userAccount',
      component: AccountMember
    }
  ],
})

export default router
