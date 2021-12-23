<template>
<div :style="opacity">
        <section v-if="accountActive==true">
<div class="container-fluid menuheader border-bottom borderStyle p-0 pb-1 pt-1 pb-md-1 pt-md-1">
<div class="row p-0 m-0">
<div class="col-md-12 p-0 m-0">
<nav class="navbar navbar-expand-lg">
<span class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbar" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<i class="bi-list"></i>
</span>

<a class="navbar-brand p-0 m-0 me-3 ms-md-2 siteStyle" href="/secure/dashboard"><img src="" :width="appinfo.logoWidth" :height="appinfo.logoHeight"  alt=" "> &nbsp; {{appinfo.appname}}</a>

<ul class="navbar-nav p-0 m-3 mb-0 mt-0 d-md-none">
    <li class="nav-item"> <i class="bi-search" role="img" aria-label="search" style="font-size: 1.4rem; color: black;"></i> </li>
</ul>
<div class="collapse navbar-collapse" id="navbar">
<div class="pb-1 mt-2 menudivider d-md-none"></div>

    <ul class="navbar-nav m-0 p-0 ms-auto">
        <li class="nav-item m-3 mb-md-0 mt-md-0 me-md-2"> <a v-bind:class="'gradient_txt' + appinfo.f_color" href="/site/logout"><i class="bi-power" role="img" aria-label="Help" style="font-size: 1.2rem;"></i></a> </li>
        <li class="nav-item m-3 mb-md-0 mt-md-0 me-md-3"> <a v-bind:class="'gradient_txt' + appinfo.f_color" href="/site/contact"><i class="bi-question-circle" role="img" aria-label="Help" style="font-size: 1.2rem;"></i></a> </li>
    </ul>
</div>

</nav>
</div>
</div>
</div>


        <div class="container-fluid">
        <div class="row">
        <div class="col-md-2 sidebar shadow mt-5">
        <div class="wrapper p-2 mt-3">
        <div class="row">
        <div class="col-md-12 mt-4 mb-2 text-center position-static">
        <div class="dp mt-2 mx-auto mb-1"></div>
        <big>Welcome, {{userdata['surname']}} </big>
        <big class="text-black"> </big>
        <small class="text-black">Administrator</small>
        </div>
        <div class="col-md-12 mt-5">
        <h5 class="pb-1"> <a href="/secure/dashboard"><strong>Dashboard</strong> </a></h5>
        </div>
        
        <div class="border-top"></div>
        <div class="col-md-12 mt-3">
        <ul class="list-unstyled ps-0 ms-1">
        <li class="mb-2">
        <p class="pb-0 mb-1 align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#webcontent" aria-expanded="false">
        <i class="bi-globe me-1"></i>    Menus
        <i class="bi-chevron-down  float-end"></i>
        </p>
        <div class="collapse" id="webcontent">
        <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small" v-for="(d, index) in webcontent" :key="index">
        <li> <router-link :to="'/secure/'+d['menuName']" class="link-dark nav-link"><i class="bi-dash"></i> {{d['menu_description']}} </router-link></li>
        </ul>
        </div>
        </li>  
        </ul>

        <div class="border-top my-3"></div>
        <ul class="list-unstyled ps-0 ms-1">
        <li class="mb-1">
        <p class=" pb-0 mb-1 align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#admin" aria-expanded="false">
        <i class="bi-person me-1"></i> Admin
        <i class="bi-chevron-down float-end"></i>
        </p>
        <div class="collapse" id="admin">
        <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small" v-for="(d, index) in admin" :key="index">
        <li> <router-link :to="'/secure/'+d['menuName']" class="link-dark nav-link"><i class="bi-dash"></i> {{d['menu_description']}} </router-link></li>
        </ul>
        </div>
        </li>  
        </ul>   

        </div>
        </div>

        </div>

        </div>
        <div class="col-md-10 offset-md-2">
        <section v-if="ifUserHasAccess==true">
        <div class="ms-md-3 me-md-3 p-md-3">
            <slot></slot>
        </div>
        </section>
        <section v-else>
        <div class="container-fluid">
        <div class="row mt-5 text-center ">
        <div class="col-8 mt-5 mx-auto d-flex justify-content-center">
        <p class="lead mt-2 text-primary"><span>{{norecord}}</span></p>
        </div>
        </div>
        </div>
        </section>
        </div>
        </div>
        </div>
        </section>
        <section v-else>
        <div class="container-fluid mt-5">
        <div class="row mt-5 text-center ">
        <div class="col-md-8 mt-5 mx-auto d-flex justify-content-center">
        <p class="mt-2 text-primary"><span>{{norecord}}</span></p>
        </div>
        </div>
        </div>
        </section>

</div>
</template>


<script>
import appsettings from '../json/myapp.json'
import axios from 'axios'
export default {
        data(){
        return {
        info:[],
        userdata:[],
        menus:[],
        webcontent:[
            {"menuName":'itemcategory', 'menu_description':'Add Category'},
            {"menuName":'items', 'menu_description':'Categories'},
            {"menuName":'contents', 'menu_description':'Feedback(s)'},
        ],
        users:[],
        admin:[
            {"menuName":'adminaccount', 'menu_description':'Account'},
        ],
        settingMenu:[],
        mailing:[],
        loan:[],
        payment:[],
        upload:[],
        "settings":appsettings.settings,
        "appinfo":appsettings.appinfo,
        networkerror:appsettings.error.networkerror,
        progress:null,
        accountActive:false,
        ifUserHasAccess:true,
        userid:null,
        page: '',
        pwd:'',
        classname:'',
        isDisabled: false,
        error_btn: null,
        errormodal: null,
        record:false,
        norecord: '',
        loader:false,
        loaderstatus:'',
        counter:'0',
        pagename: this.$route.name,
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
        }
        },

        mounted(){
        this.auth_check()
        this.listmenu()
        this.setStorage()
        },
        methods:{
        setStorage: function(){
        localStorage.setItem('error', this.networkerror)
        },
       
        auth_check: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/auth/auth_check/',{
        params: {
        'pagename': this.pagename
        }
        })
        .then(response => {
        if(response.data.status==response.data.statusmsg){
        this.userdata = response.data.userdata
        this.accountActive = true
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        localStorage.setItem("userdata", response.data.userdata);
        }else{
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.accountActive = false
        localStorage.removeItem('userdata');
        window.location.href='/site/logout'
        }
        }).catch(()=>{
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.accountActive = false
        this.alert = localStorage.getItem('error')
        localStorage.removeItem("userdata");
        window.location.href='/site/logout'
        })
        },

 listmenu: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/adminmenu/menus/',{
        params:{

        'pagename':this.pagename
        }
        })
        .then(response => {
        if(response.data.status == response.data.statusmsg){
        this.alert=''
        this.classname=''
        this.menus = response.data.result
        this.webcontent = response.data.webcontent
        this.users = response.data.users
        this.admin = response.data.admin
        this.mailing = response.data.mailing
        this.loan = response.data.loan
        this.payment = response.data.payment
        this.upload = response.data.upload
        this.settingMenu = response.data.settings
        this.accountActive = true
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        }else{
        this.alert=''
        this.classname=''
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        }

        }).catch(()=>{
        this.alert=''
        this.classname=''
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        })
        },

checkmenu: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/adminmenu/checkmenu/',{
        params:{
        'pagename':this.pagename
        }
        })
        .then(response => {
        if(response.data.status == response.data.statusmsg){
        this.norecord=response.data.msg
        this.alert=''
        this.classname=''
        this.ifUserHasAccess=response.data.ifUserHasAccess
        this.accountActive = true
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        }else{
        this.alert=''
        this.norecord=response.data.msg
        this.ifUserHasAccess=response.data.ifUserHasAccess
        this.classname=''
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        }

        }).catch(()=>{
        this.alert=''
        this.classname=''
        this.norecord=localStorage.getItem('error')
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        })
        },


        },

}
</script>