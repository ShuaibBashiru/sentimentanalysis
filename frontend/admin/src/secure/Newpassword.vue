<template>
<div :style="opacity">
    <GeneralHeader/>
<section v-if="record==true">
    <br clear="all">
<div class="col-md-9 mt-5 ms-auto">
<div class="container">
<div class="border">
<div class="row">
<div class="col-md-8">
    <div class="p-2">
            <form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="border p-2">
                <legend class="w-auto" style="float: none; padding: inherit;">Change password</legend>
            <div class="row">

            <div class="col-md-12">
                <div class="m-1 mt-2">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                    <label for="sname" class="pb-1 text-dark">Your email</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-briefcase"></i></span>
                    <input type="text" v-model="email" :disabled="isDisabled" id="email" class="form-control" required readonly placeholder="Email address">
                </div>
                
                </div>
            </div>


            <div class="col-md-6">
                <div class="m-1 mt-2">
                    <label for="sname" class="pb-1 text-dark">New password</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-map"></i></span>
                    <input type="password" v-model="password" :disabled="isDisabled" minlength="3" maxlength="50" class="form-control" required placeholder="Password">
                </div>
                <small class="text-danger">{{error}}</small>
                
                </div>
            </div>

            <div class="col-md-6">
                <div class="m-1 mt-2">
                    <label for="sname" class="pb-1 text-dark">Confirm password</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-person"></i></span>
                    <input type="text" v-model="cpassword" :disabled="isDisabled" minlength="3" maxlength="50" class="form-control" required placeholder="Confirm password">
                </div>
                <small class="form-text text-muted"></small>
                
                </div>
            </div>


            <div class="col-md-12 mt-2 text-center d-flex justify-content-end">
                <div class="m-1">
                    <label for=""></label>
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{submit}}</button>
                </div>
            </div>
            <small class="pb-2 text-danger text-center">{{error_btn}}</small>
            </div>

            <div class="col-md-12 mt-2">
                <div v-bind:class="classname">{{alert}}</div>
            </div>

                </div>
                </fieldset>
            </form>
                <div class="col-md-12 mt-4 d-flex justify-content-end">
                <p class=""><a href="/site/signin">Sign in instead</a></p>
            </div>
        
    </div>
</div>

</div>
</div>
</div>


</div>
</section>
<section v-else>
<div class="container">
    <div class="row">
    <div class="col-12 mt-5 d-flex justify-content-center">
    <p class="lead text-danger mt-2">{{norecord}}</p> <br clear="all/">
    </div>
    <div class="col-12 mt-3 d-flex justify-content-center">
    <!-- <p class="m-2" @click="$router.go(-1)" ><a href="#" class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </a></p> -->
    </div>
    </div>
</div>
</section>
</div>
</template>
<script>
import axios from 'axios'
export default {

    data (){
        return{
        keyid_validate: this.$route.params.id,
        email: this.$route.params.email,
        record: false,
        alert:null,
        token: null,
        password: null,
        cpassword: null,
        languageCode: null,
        phone: null,
        countryCode: null,
        account_type: null,
        gender: null,
        selectDefault:"Select",
        classname:null,
        submit:'Proceed',
        submittxt:'Proceed',
        isDisabled:false,
        error: null,
        error_btn: null,
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
    }
    },
    created(){
        this.preview()
    this.tokenize()
    },
    methods:{
        preview: function(){
        this.norecord = 'Synchronizing...'
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/validate_password_id/', {
            params:{
                'keyid': this.keyid_validate,
                'email': this.email
            },
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.norecord=''
            this.info = response.data.result
            this.keyid = this.info['keyid']
            this.record = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable 
            }else{
            this.record = false
            this.classname=''
            this.alert=''
            this.norecord=response.data.msg
            this.classname=response.data.classname
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        }).catch(()=>{
            this.record = false
            this.classname='alert-danger p-2'
            this.alert=''
            this.norecord=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = false
            this.opacity = this.opacity_disable
        })
    },


    formCheck: function(e){
        if (this.password!=this.cpassword) {
        this.error="Your password do not match";
        }else{
            this.error="";
        this.submit="Please wait.."
        this.update()
        }
    e.preventDefault();
    },
  update: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
    const form = new FormData();
        form.append('password', this.password)
        form.append('cpassword', this.cpassword)
        form.append('keyid', this.keyid)
        form.append('email', this.email)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/update_password/', form,{
        }).then(response => {
        if(response.data.status==response.data.statusmsg){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = true
        this.opacity = this.opacity_disable
        setInterval(function(){
        window.location.href=response.data.redirect
        },3000)
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        }
    }).catch(()=>{
        this.classname='alert-danger p-2'
        this.alert=localStorage.getItem('error')
        this.submit=this.submittxt
        this.$Progress.fail()
        this.isDisabled = false
        this.opacity = this.opacity_disable
    })  
    },


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
     this.classname='text-danger p-1 text-center'
      this.alert=localStorage.getItem('error')
      }
    
  }).catch(()=>{
      this.$Progress.fail()
      this.isDisabled = false
      this.classname='text-danger p-1 text-center'
      this.alert=localStorage.getItem('error')
  })
  },
    }


    }
</script>