import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

export default new Router({
mode: 'history',
base: process.env.BASE_URL,
routes:[
{
    path: '*',
    name:'error404',
    meta:{title:'404-page...'},
    component: ()=> import('./views/PageNotFound.vue'),
},

{
    path: '/',
    name:'home',
    meta:{title:'Home'},
    component: ()=> import('./views/Home.vue'),
},


{
    path: '/site/signin',
    name:'signin',
    meta:{title:'user Sign in'},
    component: ()=> import('./auth/Signin.vue'),
},

{
    path: '/site/signinuser',
    name:'signinuser',
    meta:{title:'user Sign in'},
    component: ()=> import('./auth/signin_user.vue'),
},

{
    path: '/site/search',
    name: 'search',
    meta: {title:'user Sign in'},
    component: ()=> import('./api/search.vue'),
},


{
    path: '/secure/dashboard',
    name:'dashboard',
    meta:{title:'Dashboard'},
    component: ()=> import('./secure/Dashboard.vue'),
},

{
    path: '/site/auth-check',
    name:'validation',
    meta:{title:'Loggin...'},
    component: ()=> import('./auth/Auth-check.vue'),
},


{
    path: '/site/logout',
    name:'logout',
    meta:{title:'Admin account'},
    component: ()=> import('./auth/Logout.vue'),
},

{
    path: '/site/newpassword/:email/:id',
    name:'newpassword',
    meta:{title:'New password'},
    component: ()=> import('./secure/Newpassword.vue'),
},

{   
    path: '/site/forgotpassword/',
    name:'forgotpassword',
    meta:{title:'Forgot password'},
    component: ()=> import('./auth/ForgotPassword.vue'),
},

// Priviledges
{
    path: '/secure/adminnewmenu',
    name:'adminnewmenu',
    meta:{title:'Admin new menu'},
    component: ()=> import('./forms/adminnewmenu.vue'),
},


{
    path: '/secure/usernewmenu',
    name:'usernewmenu',
    meta:{title:'user new menu'},
    component: ()=> import('./forms/usernewmenu.vue'),
},
{
    path: '/secure/usermenus',
    name:'usermenus',
    meta:{title:'Menu'},
    component: ()=> import('./api/usermenus.vue'),
},

// end
{
    path: '/secure/adminaccount',
    name:'adminaccount',
    meta:{title:'Admin account'},
    component: ()=> import('./forms/adminaccount.vue'),
},
{
    path: '/secure/adminrecord',
    name:'adminrecord',
    meta:{title:'Admin record'},
    component: ()=> import('./api/adminrecord.vue'),
},



// end
{
    path: '/secure/useraccount',
    name:'useraccount',
    meta:{title:'Admin account'},
    component: ()=> import('./forms/useraccount.vue'),
},
{
    path: '/secure/userrecord',
    name:'userrecord',
    meta:{title:'Record'},
    component: ()=> import('./api/userrecord.vue'),
},

{
    path: '/secure/uploadbulkuser/:title/:id',
    name:'uploadbulkuser',
    meta:{title:'Upload'},
    component: ()=> import('./formupload/uploadbulkuser.vue'),
},

{
    path: '/secure/uploadusers',
    name:'uploadusers',
    meta:{title:'Upload biodata'},
    component: ()=> import('./formupload/uploadusers.vue'),
},
{
    path: '/secure/uploadcontent',
    name:'uploadcontent',
    meta:{title:'Upload content'},
    component: ()=> import('./formupload/uploadcontent.vue'),
},
{
    path: '/secure/contents',
    name:'contents',
    meta:{title:'Content'},
    component: ()=> import('./api/contents.vue'),
},
{
    path: '/secure/uploadcategory',
    name:'uploadcategory',
    meta:{title:'Upload content'},
    component: ()=> import('./formupload/uploadcategory.vue'),
},


{
    path: '/secure/itemcategory',
    name:'itemcategory',
    meta:{title:'Categories'},
    component: ()=> import('./forms/itemcategory.vue'),
},

{
    path: '/secure/uploaditems',
    name:'uploaditems',
    meta:{title:'Items'},
    component: ()=> import('./formupload/uploaditems.vue'),
},

{
    path: '/secure/items',
    name:'items',
    meta:{title:'Items'},
    component: ()=> import('./api/items.vue'),
},
// end
]
})