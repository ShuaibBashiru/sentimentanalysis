<template>
<div :style="opacity">
<div class="container-fluid menuheader border-bottom borderStyle p-0 pb-1 pt-1 pb-md-1 pt-md-1">
<div class="row p-0 m-0">
<div class="col-md-12 p-0 m-0">
<nav class="navbar navbar-expand-lg">
<span class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbar" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<i class="bi-list"></i>
</span>

<a class="navbar-brand p-0 m-0 me-3 ms-md-2 text-success" href="/"><img src="" :width="appinfo.logoWidth" :height="appinfo.logoHeight"  alt=" "> &nbsp; {{appinfo.appname}}</a>

<ul class="navbar-nav p-0 m-3 mb-0 mt-0 d-md-none">
    <li class="nav-item"> <i class="bi-search" role="img" aria-label="search" style="font-size: 1.4rem; color: black;"></i> </li>
</ul>
<div class="collapse navbar-collapse" id="navbar">
<div class="pb-1 mt-2 menudivider d-md-none"></div>

    <ul class="navbar-nav m-0 p-0 ms-auto">
        <li class="nav-item m-3 mb-md-0 mt-md-0 me-md-3"> <a class="text-success" href="/site/contact"><i class="bi-question-circle" role="img" aria-label="Help" style="font-size: 1.2rem;"></i></a> </li>
        <li class="nav-item m-3 mb-md-0 mt-md-0 me-md-3"> <a class="text-success" href="/site/signin"><i class="bi-person" role="img" aria-label="Help" style="font-size: 1.2rem;"></i> Admin </a> </li>
    </ul>
</div>

</nav>
</div>
</div>
</div>

        <div class="container-fluid">
        <div class="row">
        <div class="col-md-12">
        <section v-if="ifUserHasAccess==true">
        <div class="ms-md-3 me-md-3 p-md-3">
            <slot></slot>
        </div>
        </section>
        <section v-else>
        <div class="container-fluid">
        <div class="row mt-5 text-center ">
        <div class="col-md-8 mt-5 mx-auto d-flex justify-content-center">
        <p class="mt-2 text-primary"><span>{{norecord}}</span></p>
        </div>
        </div>
        </div>
        </section>
        </div>
        </div>
        </div>

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
        webcontent:[],
        users:[],
        admin:[],
        settingMenu:[],
        mailing:[],
        loan:[],
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
        this.setStorage()
        },
        methods:{
        setStorage: function(){
        localStorage.setItem('error', this.networkerror)
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
        axios.get('/api/adminwebmenu/checkmenu/',{
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