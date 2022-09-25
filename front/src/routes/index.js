import { createRouter, createWebHistory } from "vue-router";
import MainPage from "../components/MainPage.vue";
import RecPage from "../components/RecPage.vue";

const routes = [
  { path: "/", component: MainPage },
  { path: "/rec", component: RecPage },
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
