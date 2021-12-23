<template>
<div :style="opacity">
    <GeneralHeader>
<div class="container-fluid mt-3 p-0">
<div class="row d-flex justify-content-center p-0">
    <div class="col-md-4 pe-md-4 ps-md-4 rounded mt-2">
    <h2 class="text-primary text-center mb-5">Sign in - Admin</h2>

  <form @submit.prevent="signIn" role="form">
  <div class="form-row border pt-2 pe-4 ps-4 pb-4 rounded">
<div class="form-group col">

  <section v-if="alert!=''">
      <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
  </section>

</div>
    <div class="form-group mt-4 col">
        <label for="userid" class="text-muted pb-2">Email address</label>
        <input type="hidden" v-model="token" required>
      <input type="email" class="form-control form-control" v-model="userid" placeholder="Enter email" id="userid" required maxlength="100" minlength="10">
    </div>

    <div class="form-group mt-4 col">
        <label for="pwd" class="text-muted pb-2">Password (Surname)</label>
        <small class="float-end pb-2"><a href="/site/forgotpassword" class="text-left">Forgot?</a></small>
      <div class="input-group">
        <input :type="pass_type" class="form-control form-control" v-model="pwd" placeholder="Password" id="pwd" required maxlength="50" minlength="3">
        <small class="input-group-text">
        <input class="form-check-input d-none" type="checkbox" id="showpass"
           v-model="toggle"
           true-value="yes"
          false-value="no" @change="showpassword">
        <label class="form-check-label" for="showpass">
        <small> <i class="bi-eye"></i> </small>
        </label>
        </small>
      </div>
    </div>

    <div class="form-group mt-2 col">
        <input class="form-check-input" type="checkbox" id="rememberme"
           v-model="rememberme_val"
           true-value="yes"
          false-value="no" @change="rememberme">
        <label class="form-check-label" for="rememberme">
        <small class="ps-2"> Remember me </small>
        </label>
    </div>


      <div class="form-group mt-5 col">
     <div class="row">
       <div class="col-md-12">
         <button type="submit" name="signin" class="btn btn-primary form-control" :disabled="isDisabled">{{button}}</button></div>
     </div>
    </div>
   

  </div>
</form>
<!-- <div class="p-2">
      <p class="text-center">Not registered yet? <a href="/site/newaccount" class="text-right">
        Create an Account
      </a></p>
</div> -->
    </div>
</div>

</div>
  </GeneralHeader>
</div>
</template>
<script>
import axios from 'axios'
export default {
data(){
  return{
            info:[],
            alert:'',
            progress:null,
            userid:null,
            pwd:'',
            classname:'',
            token:'',
            btntxt: 'Sign in',
            button: 'Sign in',
            isDisabled: false,
            toggle:null,
            pass_type:'password',
            opacity_enable:'opacity:0.7; pointer-events: none;',
            opacity_disable:'opacity:1; pointer-events:All;',
            opacity:'',
         }

},
created(){
this.tokenize()
},

  methods:{
  tokenize: function(){
        this.$Progress.start()
      this.isDisabled = true
    axios.get('/auth/tokenize/',{
    params:{
      'token': Math.random(9, 9999)
    }
  }).then(response => {
      if(response.data.status==response.data.statusmsg){
      this.token=response.data.key
      axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
      this.$Progress.finish()
      this.isDisabled = false
      }else{
      this.$Progress.finish()
      this.isDisabled = false
        this.classname='alert-danger p-2'
      this.alert=localStorage.getItem('error')
        this.opacity = this.opacity_enable
      } 
    
  }).catch(()=>{
      this.$Progress.fail()
      this.isDisabled = false
      this.classname='alert-danger p-2'
      this.alert=localStorage.getItem('error')
      this.opacity = this.opacity_enable

  })
  },

        signIn(){
          this.button='Please wait...'
          this.$Progress.start()
          this.isDisabled = true
          this.opacity = this.opacity_enable

          const fd = new FormData();
          fd.append('userid', this.userid)
          fd.append('pwd', this.pwd)
          fd.append('csrfmiddlewaretoken', this.token)
          axios.post('/auth/sign_in/', fd)
          .then(response => {
            if(response.data.status==response.data.statusmsg){
            this.classname=response.data.classname
            this.alert=response.data.msg
            this.button=this.btntxt
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            setTimeout(function(){
            window.location.href=response.data.redirect
            },2000)
            }else{
            this.alert=response.data.msg
            this.classname=response.data.classname
            this.button=this.btntxt
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
          
        }).catch(()=>{
            this.alert=localStorage.getItem('error')
            this.classname='alert-danger p-2'
            this.button=this.btntxt
            this.$Progress.fail()
            this.isDisabled = false
            this.opacity = this.opacity_disable

        })
    },
    showpassword: function(){
      if(this.toggle=="yes"){
      this.pass_type = 'text'
      }else{
      this.pass_type = 'password'
      }
    },
    
   


},
// End of methods

}

</script>
