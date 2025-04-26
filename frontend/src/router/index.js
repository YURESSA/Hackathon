import { createRouter, createWebHistory } from 'vue-router'
import { useDataStore } from '@/stores/counter'
import Main from '@/views/main.vue'
import AccountMember from '@/views/account-member.vue'
import Login from '@/views/login.vue'
import Register from '@/views/register.vue'
import FindTeam from '@/views/find-team.vue'
import AccountTeamYes from '@/views/account-team-yes.vue'
import AccountAdmin from '@/views/account-admin.vue'
import AccountJury from '@/views/account-jury.vue'
import JuryTeamList from '@/views/jury-team-list.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Main,
      meta: { requiresAuth: true }
    },
    {
      path: '/account',
      name: 'userAccount',
      component: AccountMember,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: { requiresAuth: false }
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
      meta: { requiresAuth: false }
    },
    {
      path: '/find-team',
      name: 'findTeam',
      component: FindTeam,
      meta: { requiresAuth: true }
    },
    {
      path: '/team-account',
      name: 'AccountTeam',
      component: AccountTeamYes,
      meta: { requiresAuth: true }
    },
    {
      path: '/admin',
      name: 'Admin',
      component: AccountAdmin,
      meta: { requiresAuth: true }
    },
    {
      path: '/jury',
      name: 'Jury',
      component: AccountJury,
      meta: { requiresAuth: true }
    },
    {
      path: '/jury-team-list',
      name: 'JuryTeamList',
      component: JuryTeamList,
      meta: { requiresAuth: true }
    }
  ],
})

router.beforeEach((to, from, next) => {
  const store = useDataStore()
  const isAuthenticated = !!store.token

  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login') // Защищённые маршруты
  } else if (
    (to.name === 'Login' || to.name === 'Register') &&
    isAuthenticated
  ) {
    next('/') // Блокируем вход/регистрацию для авторизованных
  } else {
    next() // Разрешаем переход
  }
})

export default router
