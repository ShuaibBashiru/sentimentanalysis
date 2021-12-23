import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'
import App from './App'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueSimpleAlert from "vue-simple-alert";
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(VueSimpleAlert, { reverseButtons: true });

import VueProgressBar from 'vue-progressbar'

Vue.use(VueProgressBar, {
  color: 'blue',
  failedColor: 'red',
  height: '2px'
})

import AccountActive from './auth/Active'
import MenuHeader from './layout/MenuHeader'
Vue.component('AccountActive', AccountActive)
Vue.component('MenuHeader', MenuHeader)

import GeneralHeader from './layout/GeneralHeader'
import GeneralFooter from './layout/GeneralFooter'
Vue.component('GeneralHeader', GeneralHeader)
Vue.component('GeneralFooter', GeneralFooter)

import AdminHeader from './layout/BackendHeader'
Vue.component('AdminHeader',AdminHeader)

import PanelHeader from './layout/GeneralHeader'
Vue.component('PanelHeader',PanelHeader)


import ProfileLayout from './layout/profileLayout'
Vue.component('ProfileLayout',ProfileLayout)

Vue.use(VueAxios, axios, Vuex)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')