
<template>
<div :style="opacity">
<AdminHeader>
<div class="container p-0">
<div class="row">
<div class="col-6">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"> Update address </h5>
</div>
</div>
<div class="col-6 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" role="group" aria-label="First group" @click="$router.go(-1)"><button class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> </button></div>
</div>

</div>
</div>
</div>
  <section v-if="alert!=''">
      <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
  </section>
<section v-if="record==true">
<div class="container p-0">
<div class="border">
<div class="row">
<div class="col-md-12">
    <div class="p-2">
        <section v-if="formSuccess == 0">
<form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="p-2 pt-0">
                    <div class="row m-md-0">
            <div class="col-md-12 mt-1">
                <div class="m-1 mt-3">
                    <label for="address_one" class="pb-1 text-dark">Address</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-map"></i></span>
                    <input type="text" v-model="address_one"  minlength="10" maxlength="300" id="address_one" class="form-control" required placeholder="Contact address">
                </div>
                    <small class="form-text text-muted"></small>
                </div>
            </div>

                       <div class="col-md-12">
                <div class="m-1 mt-3">
                    <label for="address_two" class="pb-1 text-dark">Alternative (optional)</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-map"></i></span>
                    <input type="text" v-model="address_two"  minlength="0" maxlength="300" id="address_two" class="form-control" placeholder="Contact address">
                </div>
                    <small class="form-text text-muted"></small>
                </div>
            </div>

           <div class="col-md-6 mt-2 text-center">
           </div>
           <div class="col-md-6 mt-2 text-center d-flex justify-content-end">
                <div class="m-1 mt-3">
                    <label for=""></label>
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary form-control">{{submit}}</button>
                </div>
                </div>
                    <small class="pb-2 text-danger text-center">{{error_btn}}</small>
            </div>

                </div>
                </fieldset>
        </form>
            </section>
         
          <section v-else-if="formSuccess == 1" >
        <div class="container mt-5 mb-4">
            <div class="row">

            <div class="col-12 mt-2 d-flex justify-content-center">
            <div class="btn-group">
                <button class="btn btn-primary m-2" @click="$router.go(-1)"><i class="bi-check"> </i> Successful! Close page </button>
                </div>
            </div>
            </div>
        </div>
          </section>
           <section v-else>
        <div class="container mt-5 mb-4">
            <div class="row">

            <div class="col-12 mt-2 d-flex justify-content-center">
            <div class="btn-group">
                <button class="btn btn-warning m-2" @click="$router.go(-1)"> Close this page </button>
                <button class="btn btn-primary m-2" @click="$router.go(0)">Try again</button>

                </div>
            </div>
            </div>
        </div>
          </section>
    </div>

</div>
</div>
</div>
</div>
</section>
<section v-else>
<div class="container">
    <div class="row">
    <div class="col-12 mt-2 d-flex justify-content-center">
    <div class="btn-group">
        <button class="btn btn-warning m-2" @click="$router.go(-1)"> Close this page </button>
        </div>
    </div>
    </div>
</div>
</section>

</AdminHeader>

</div>
</template>

<script>
import axios from 'axios'
export default {
    data (){
        return{
        
        formSuccess: 0,
        auth_check: false,
        token: '',
        alert: null,
        keyid_validate: this.$route.params.id,
        emailid: this.$route.params.title,
        alertmodal: null,
        error: '',
        info: [],
        checked: true,
        address_one: null,
        address_two: null,
        loader: false,
        selectDefault:"Select",
        classname: '',
        submit: 'Update',
        submittxt:'update',
        isDisabled: false,
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
        error_btn: null,
        errormodal: null,
        record:false,
        norecord: '',
    }
    },

    created(){
    this.tokenize()
    this.preview()
    }, 

    methods:{
    showForm: function(){
        this.formSuccess = 0
    },

   preview: function(){
        this.norecord = 'Synchronizing...'
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/userdata/getinfo/', {
            params:{
                'keyid': this.keyid_validate,
                'emailid': this.emailid
            },
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.norecord=''
            this.record = true
            this.info = response.data.result
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable 
            this.address_one = this.info['user_address_one']
            this.address_two = this.info['user_address_two']
            }else{
            this.record = false
            this.classname=''
            this.alert=response.data.msg
            this.norecord=response.data.msg
            this.classname=response.data.classname
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        }).catch(()=>{
            this.record = false
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
            this.norecord=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = false
            this.opacity = this.opacity_disable
        })
    },

    formCheck: function(e){
       this.$confirm("Are you sure you want to update this?, click Ok to continue or Cancel to go back?").then(() => {
            this.submit="Please wait.."
            this.update()
            });
    e.preventDefault();
    },
    update: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        this.submit='Please wait..'
        const form = new FormData();
        form.append('address_one', this.address_one)
        form.append('address_two', this.address_two)
        form.append('keyid', this.keyid_validate)
        form.append('emailid', this.emailid)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/user/updateaddress/', form)
        .then(response => {
        if(response.data.status==response.data.statusmsg){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.formSuccess = 1
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.formSuccess = 2

        }
    }).catch(()=>{
        this.classname='alert-danger p-2'
        this.alert=localStorage.getItem('error')
        this.submit=this.submittxt
        this.$Progress.fail()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.formSuccess = 2

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


    },


    }
</script>