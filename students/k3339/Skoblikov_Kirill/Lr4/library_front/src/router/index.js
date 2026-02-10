import { createRouter, createWebHistory } from 'vue-router';
import Main from "@/pages/MainPage.vue";
import Register from "@/pages/RegisterFormPage.vue";
import Login from "@/pages/LoginFormPage.vue";

const routes = [
  {
    path: "/",
    component: Main
  },
  {
    path: "/register",
    component: Register
  },
  {
    path: "/login",
    component: Login
  },
]

const router = createRouter({
  routes,
  history: createWebHistory(import.meta.env.BASE_URL),
})

export default router;
