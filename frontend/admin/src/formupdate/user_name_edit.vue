
<template>
<div :style="opacity">
<ProfileLayout>
<div class="container">
<div class="row">
<div class="col-4">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"> User </h5>
</div>
</div>
<div class="col-8 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" role="group" aria-label="First group" @click="$router.go(-1)"><button class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </button></div>



</div>
</div>

</div>
</div>

<div class="container p-0">
<div class="border">
<div class="row">
<div class="col-md-12">
<!-- account -->

<div class="row">
<div class="col-md-12 mx-auto">
    <div class="p-2">
         <section v-if="formSuccess == 0">
           <form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="border p-2">
                <legend class="w-auto" style="float: none; padding: inherit;">Update Account</legend>
            <div class="row">
            <div class="col-md-6">
                <div class="m-1 mt-2">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                    <label for="sname" class="pb-1 text-dark">Surname</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-person"></i></span>
                    <input type="text" v-model="surname"  id="sname" minlength="3" maxlength="50" class="form-control" required placeholder="Surname">
                </div>
                <small class="form-text text-muted"></small>
                
                </div>
            </div>

            <div class="col-md-6">
                <div class="m-1 mt-2">
                    <label for="fname" class="pb-1 text-dark">Firstname</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-person"></i></span>
                    <input type="text" v-model="firstname"  minlength="3" maxlength="50"  class="form-control" required placeholder="Firstname">
                </div>
                <small class="form-text text-muted"></small>
                
                </div>
            </div>

            <div class="col-md-6">
                <div class="m-1 mt-2">
                    <label for="oname" class="pb-1 text-dark">Othername</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-person"></i></span>
                    <input type="text" v-model="othername"  id="oname" maxlength="50" class="form-control" placeholder="Othername (Optional)">
                </div>
                <small class="form-text text-muted"></small>
                </div>
            </div>

            <div class="col-md-6">
                <div class="m-1 mt-2">
                    <label for="email" class="pb-1 text-dark">Email</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-mailbox"></i></span>
                    <input type="email" v-model="email_one"  minlength="10" maxlength="100" id="email" class="form-control" required placeholder="Email address">
                </div>
                    <small class="form-text text-muted"></small>
                </div>
            </div>


            <div class="col-md-6">
                <div class="m-1 mt-2">
                <div class="row">
                    <div class="col-5">
                    <label for="code" class="pb-1 text-dark">Country code</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-telephone"></i></span>
                    <select class="form-select p-0" v-model="countryCode" id="code" required>
                       <option disabled value="" selected>Code</option>
                    <option value="+234">+234</option>
                    </select>
                    </div>
                    </div>
                <div class="col-7">
                    <label for="phone" class="pb-1 text-dark">Phone</label>
                <div class="input-group">
                    <input type="text" v-model="phone_one"  minlength="7" maxlength="15" id="phone" class="form-control" required placeholder="Number only">
                    </div>
                </div>
                    </div>
                    <small class="form-text text-muted"></small>
            
                </div>
            </div>

                        <div class="col-md-6">
                <div class="m-1 mt-2">
                <div class="row">
                    <div class="col-md-12">
                    <label for="gender" class="pb-1 text-dark">Gender</label>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-person"></i></span>
                    <select class="form-select p-0" v-model="gender"  id="gender" required>
                    <option disabled value="" selected>Select</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    </select>
                    </div>
                    </div>
      
                    </div>
                    <small class="form-text text-muted"></small>
                </div>
            </div>


            <div class="col-md-6">
                <div class="m-1 mt-2">
                    <label for="persionalId" class="pb-1 text-dark">Personal ID</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-file-person"></i></span>
                    <input type="text" v-model="persionalId"  maxlength="100" id="persionalId" class="form-control" placeholder="ID (Optional)">
                </div>
                <small class="text-muted">This can be used to create a personal identity</small>
                </div>
            </div>

           <div class="col-md-6 mt-2 text-center">
                <div class="m-1">
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
          <section v-else>
        <div class="container mt-5 mb-4">
            <div class="row">

            <div class="col-12 mt-2 d-flex justify-content-center">
                      <div class="btn-group">
                                       <button class="btn btn-warning m-2" @click="$router.go(0)">Try again</button><button class="btn btn-primary m-2" @click="$router.go(-1)"><i class="bi-check"> </i> Successful! Close page </button>

                </div>
            </div>
            </div>
        
    </div>
</div>

</div>

<!-- end account -->
</div>
</div>
</div>
</div>

</ProfileLayout>

<!-- modal -->
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
        alertmodal: null,
        keyid_validate: this.$route.params.id,
        keyid:'',
        error: '',
        info: [],
        checked: true,
        surname: null,
        firstname: null,
        othername: null,
        email_one: null,
        phone_one: null,
        countryCode: '',
        gender: '',
        persionalId: null,
        loader: false,
        selectDefault:"Select",
        classname: '',
        submit: 'Update',
        submittxt:'Update',
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
    validEmail: function (email) {
    var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
    },
    validDigit: function (digits) {
    var re = /^\d+$/;
    return re.test(digits);
    },
    formCheck: function(e){
        if (!this.validEmail(this.email_one)) {
        this.error_btn="Valid email required.";
        }else if(!this.validDigit(this.phone_one)){

        this.error_btn="Valid phone number required.";
        }else{
            this.error_btn="";
            this.$confirm("Are you sure you want to update this?, click Ok to continue or Cancel to go back?").then(() => {
            this.submit="Please wait.."
            this.update()
            });
        }
    e.preventDefault();
    },
    update: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        this.submit='Please wait..'
        const form = new FormData();
        form.append('surname', this.surname)
        form.append('firstname', this.firstname)
        form.append('othername', this.othername)
        form.append('email', this.email_one)
        form.append('phone', this.phone_one)
        form.append('countryCode', this.countryCode)
        form.append('gender', this.gender)
        form.append('countryCode', this.countryCode)
        form.append('persionalId', this.persionalId)
        form.append('keyid', this.keyid)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/user/update/', form)
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

     preview: function(){
        this.norecord = 'Synchronizing...'
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/user/validate_id/', {
            params:{
                'keyid': this.keyid_validate
            },
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.norecord=''
            this.info = response.data.result
            this.surname = this.info['surname']
            this.firstname = this.info['firstname']
            this.othername = this.info['othername']
            this.email_one = this.info['email_one']
            this.phone_one = this.info['phone_one']
            this.countryCode = this.info['countryCode']
            this.gender = this.info['gender']
            this.persionalId = this.info['persional_id']
            this.keyid = this.info['id']
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable 
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