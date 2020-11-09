import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import { component } from 'vue/types/umd';
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/data',
    name: 'Data',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Data.vue')
  },
  {
    path:'/admin',
    name: 'Admin',
    component:()=>import('../views/AdminPanel.vue')
  },
  {
    path:'/predictions',
    name:'Predictions',
    component:()=>import('../views/Predictions.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
