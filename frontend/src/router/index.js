import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import Userdashboard from '../components/Userdashboard.vue';
import Admindashboard from '../components/Admindashboard.vue';
import User from '../components/User.vue';
import Book from '../components/Book.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  {path: '/register', component: Register},
  {
    path: '/user',
    component: Userdashboard,
    children:[
      {path: 'book', component: Book}
    ]
  },
  {
    path: '/admin',
    component: Admindashboard,
    children:[
      {path: 'users', component: User}
    ]
  }
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
