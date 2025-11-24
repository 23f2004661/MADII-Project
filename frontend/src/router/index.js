import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import Userdashboard from '../components/Userdashboard.vue';
import Admindashboard from '../components/Admindashboard.vue';
import User from '../components/User.vue';
import Book from '../components/Book.vue';
import Createlot from '../components/Createlot.vue';
import Editlot from '../components/Editlot.vue';
import CheckStatus from '../components/Check_Status.vue';
import Userhistory from '../components/Userhistory.vue';
import Release from '../components/Release.vue';
import SummaryUser from '../components/SummaryUser.vue';
import SummaryAdmin from '../components/SummaryAdmin.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  {path: '/register', component: Register},
  {path: '/user',component: Userdashboard},
  {path: '/admin',component: Admindashboard},
  {path: '/admin/users',component: User},
  {
    path: '/user/book/:id',
    name: 'Book',
    component: Book,
    props: true
  },
  {path: '/admin/createlot',component: Createlot},
  {path: '/admin/editlot/:id',component: Editlot},
  {path: '/admin/check_status/:id',component: CheckStatus},
  {path: '/user/history',component: Userhistory},
  {path: '/user/release', component: Release},
  {path: '/user/summary', component: SummaryUser},
  {path: '/admin/summary', component: SummaryAdmin}
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
