<template>
    <div>
    <GeneralHeader/>
<section v-if="loader==false"></section>
<section v-else>
   <div class="container-fluid">
       <br clear="all/">
       <br clear="all/">
       <br clear="all/">
       <br clear="all/">
       <br clear="all/">

       <div class="row mt-5">
           <div class="col-md-4 mx-auto text-center">
                 <section v-if="alert!=''">
      <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
  </section>
               <section v-if="error_found==true">
                   <a href="/site/signin/" class="btn btn-primary">Sign in again</a>
               </section>

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
        message: 'Please wait a moment..',
        statusMsg: null,
        error_found: false,
        loader:true,
        classname: 'text-primary',
        pagename: this.$route.name,
        alert: 'Please wait a moment..'

    }
},
created(){
   this.auth_check(); 
},
    methods:{
            auth_check: function(){
                this.$Progress.start()
            axios.get('/auth/auth_check/', {
                params: {
                    'pagename': this.pagename
                }
            })
        .then(response => {
            if(response.data.status==response.data.statusmsg){
                this.$Progress.finish()
                this.alert = response.data.msg
                this.classname = response.data.classname
                this.error_found = false
                localStorage.setItem("userdata", response.data.userdata);  
                setTimeout(function(){
                window.location.href=response.data.redirect
                },2000)
            }else{
                this.$Progress.finish()
                this.alert = response.data.msg
                this.classname = response.data.classname
                this.error_found = true
                 setTimeout(function(){
                window.location.href='/site/logout'
                },3000)
            }
        }).catch(()=>{

            this.$Progress.finish()
                this.alert = localStorage.getItem('error')
                this.classname = 'alert-danger'
            this.error_found = true
               setTimeout(function(){
                window.location.href='/site/logout'
                },3000)
            

        })
    },

}
}
</script>