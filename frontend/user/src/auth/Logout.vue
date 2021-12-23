<template>
    <div>
    <GeneralHeader/>
<section v-if="loader==false">
</section>
<section v-else>
   <div class="container-fluid">
       <br clear="all/">
       <br clear="all/">
       <br clear="all/">
       <br clear="all/">
       <br clear="all/">
       <div class="row mt-5">
           <div class="col-12 mt-5 d-flex justify-content-center">
<div class="lds-roller"><div></div><div></div><div></div></div>
           </div>
           <div class="col-12 mt-5 d-flex justify-content-center"><small></small></div>
       </div>

       <div class="row mt-5">
           <div class="col text-center">
               <p class="text-muted"><small>{{message}}</small></p>
           </div>
       </div>
   </div>
</section>

    </div>
</template>
<script>
import axios from 'axios'
export default {
data(){
    return{
        message: 'Checking session status...',
        statusMsg: null,
        error_found: false,
    }
},
created(){
   this.logout(); 
},
    methods:{
    logout: function(){
             this.$Progress.start()
          axios.get('/auth/logout/')
        .then(response => {
            if(response.data.status==response.data.statusmsg){
                this.alert = response.data.msg
                this.classname = response.data.classname
                this.error_found = false
                localStorage.removeItem('userdata');
                this.$Progress.finish()
                setTimeout(function(){
                window.location.href=response.data.redirect
                },2000)
            }else{
                this.alert = response.data.msg
                this.classname = response.data.classname
                this.error_found = false
                localStorage.removeItem('userdata');
                this.$Progress.finish()
                 setTimeout(function(){
                window.location.href='/site/signin'
                },2000)
            }
        }).catch(()=>{
            this.alert = localStorage.getItem('error')
            this.classname = 'alert-danger'
            this.error_found = true
            localStorage.removeItem("userdata");
            this.$Progress.finish()
            setTimeout(function(){
            window.location.href='/site/signin'
            },2000)

        })
    },

}
}
</script>