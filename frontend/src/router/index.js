import Vue from "vue";
import VueRouter from "vue-router";
import Mobility from '../components/Mobility.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: "/mobility",
    name: "Mobility",
    component: Mobility,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
