import { createRouter, createWebHistory } from 'vue-router'

import App from './App.vue'
import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'

const routes = [{
  path: '/',
  name: 'root',
  component: App
},

{
  path: '/user/logIn',
  name: "logIn",
  component: LogIn
},
{
  path: '/user/signUp',
  name: "signUp",
  component: SignUp
},

{
  path: '/historias_clinicas',
  name: 'historias_clinicas',
  component: () => import('./views/HistoriaClinicaViews.vue')
},

{
  path: '/crear_historia_clinica',
  name: 'crear_historia',
  component: () => import('./views/crearHistoriaClinica.vue')
}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

