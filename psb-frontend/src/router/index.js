import Vue from 'vue';

import Router from 'vue-router';

import MainPage from '@/components/MainPage';

Vue.use(Router);

const routes = [

   {
     path: '/',
     name: 'MainPage',
     component: MainPage,
   },
]