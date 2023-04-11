import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // path: '/',
      path: '/home',
      name: 'home',
      // alias: '/home',
      // component: HomeView
      component: () => import('../views/HomeView.vue')
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // },
    {
      // path: '/login',
      path: '/',
      name: 'login',
      alias: '/login',
      // component: () => import('../views/LoginView.vue')
      component: LoginView
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('../views/SettingsView.vue')
    }
  ]
})

// router.beforeEach((to, from) => {
//   if (to.name !== 'login' && !localStorage.getItem('token')) {
//     return { name: 'login' }
//   }
// })

export default router
