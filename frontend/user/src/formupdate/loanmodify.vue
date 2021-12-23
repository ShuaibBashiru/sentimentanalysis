
<template>
<div :style="opacity">
<AdminHeader>
<div class="container p-0">
<div class="row">
<div class="col-6">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"> Update loan </h5>
</div>
</div>
<div class="col-6 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" role="group" aria-label="First group" @click="$router.go(-1)"><button class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> </button></div>
<div class="btn-group m-2" role="group" aria-label="First group"><button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#popOver">Modify</button> </div>
</div>
</div>
</div>
</div>
<div v-bind:class="'alert '+ classname +' ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
<section v-if="record==true">
<div class="container p-0 mb-2">
    <div class="row">
        <div class="col-md-12">
    <div class="border rounded pb-2">
        <div class="row p-md-2 pt-1 pb-3 border-bottom m-0 mb-1 mt-1 hover-effect">
         <div class="row m-0 p-0">
                <div class="col-9 p-3 pt-0 pb-0">
                   <div class="row mt-md-4">
                        <div class="col-md-3 d-flex justify-content-start border-end"><p class="lead p-md-0 m-md-0" style="font-size:14px;">NAME</p></div>
                        <div class="col-md-7 d-flex justify-content-start"> <p class="text-muted p-md-0 m-md-0" style="font-size:14px;">  </p> {{info['surname']}} {{info['firstname']}} {{info['othername']}} </div>
                   </div>
                </div>
                <div class="col-3">
                    <div class="col-12 d-flex justify-content-end">
                        <div class="rounded" style="width:70px; height:70px;">
                        <img :src="require('../passport/avatar.png')"  class="img-responsive rounded" style="width:70px; height:70px;" alt="errror"/></div></div>
                </div>
            </div>
        </div>

        <div class="row p-md-2 border-bottom m-0 pt-md-3 pb-md-3 hover-effect">
            <div class="row m-0 p-0">
                <div class="col-9 p-3 pt-0 pb-0">
                   <div class="row">
                        <div class="col-md-3 d-flex justify-content-start border-end"><p class="lead p-md-0 pt-2 m-md-0" style="font-size:14px;">EMAIL</p></div>
                        <div class="col-md-7 d-flex justify-content-start"> <strong><p class="lead p-md-0 m-md-0" style="font-size:14px;">{{info['email_one']}} </p> </strong></div>
                   </div>
                </div>
                <div class="col-3">
                    <div class="col-12 d-flex justify-content-end"><i class="bi-envelope text-primary m-4 mt-0 mb-0"></i></div>
                </div>
            </div>
        </div>

        <div class="row p-md-2 m-0 pt-md-3 pb-md-3 hover-effect">
            <div class="row m-0 p-0">
                <div class="col-9 p-3 pt-0 pb-0">
                   <div class="row">
                        <div class="col-md-3 d-flex justify-content-start border-end"><p class="lead p-md-0 pt-2 m-md-0" style="font-size:14px;">PHONE</p></div>
                        <div class="col-md-7 d-flex justify-content-start"> <strong><p class="lead p-md-0 m-md-0" style="font-size:14px;"> {{info['phone_one']}} </p> </strong></div>
                   </div>
                </div>
                <div class="col-3">
                    <div class="col-12 d-flex justify-content-end"><i class="bi-person text-primary m-4 mt-0 mb-0"></i></div>
                </div>
            </div>
        </div>


    </div>
</div>
    </div>
</div>

<div class="container p-0 mb-2">
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
                <div class="row">
                    <div class="col-md-12">
                    <div class="row">
                        <div class="col-md-6"> <strong><p class="lead p-md-0 m-md-0" style="font-size:14px;">From: {{day_apply}}-{{month_apply}}-{{year_apply}} -- To: -- {{day_expire}}-{{month_expire}}-{{year_expire}} </p> </strong></div>
                   </div>
                    </div>

                    <div class="col-md-6">
                     <div class="m-1 mt-3">
                    <label for="amount" class="pb-1 text-dark">Loan amount</label>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-credit-card"></i></span>
                        <input type="text" maxlength="10" class="form-control" v-model="amount" id="amount" placeholder="Loan Amount" required>
                    </div>
                    </div>
                    </div>
                          
                    <div class="col-md-6">
                     <div class="m-1 mt-3">
                    <label for="extension" class="pb-1 text-dark">Extend date</label>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-calendar-event"></i></span>
                    <select class="form-select p-0" v-model="extension"  id="extension" required>
                    <option disabled value="" selected>Select</option>
                    <option value="continue">Continue loan</option>
                    <option value="renew">Renew loan</option>
                    </select>
                    </div>
                    </div>
                    </div>

                    <div class="col-md-6">
                     <div class="m-1 mt-3">
                    <label for="duration" class="pb-1 text-dark">Loan duration</label>

                    <section v-if="extension=='continue'">
                      <div class="input-group">
                    <span class="input-group-text"><i class="bi-calendar-event"></i></span>
                    <select class="form-select p-0" v-model="old_duration" id="duration" disabled>
                    <option disabled :value="old_duration" selected>{{old_duration}} Month(s) </option>
                    </select>
                      </div>
                    </section>
                    <section v-else>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-calendar-event"></i></span>
                    <select class="form-select p-0" v-model="duration" id="duration" required>
                    <option disabled value="" selected>Select</option>
                    <option value="6">6 months</option>
                    <option value="12">12 months</option>
                    <option value="18">18 months</option>
                    <option value="24">24 months</option>
                    </select>
                      </div>
                    </section>

          
                    </div>
                    </div>

                  <div class="col-md-6">
                     <div class="m-1 mt-3">
                    <label for="comment" class="pb-1 text-dark">User comment</label>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-pencil"></i></span>
                        <textarea v-model="comment" class="form-control" id="comment" cols="30" rows="1" placeholder="" readonly></textarea>
                    </div>
                    </div>
                    </div>

                  <div class="col-md-6">
                     <div class="m-1 mt-3">
                    <label for="admincomment" class="pb-1 text-dark">Support your update with comment</label>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-pencil"></i></span>
                        <textarea v-model="admin_comment"  class="form-control" id="admincomment" cols="30" rows="1" placeholder="Leave a comment"></textarea>
                    </div>
                    </div>
                    </div>

                    
                 <div class="col-md-6 text-center">
                <div class="m-1 mt-3">
                    <label for=""></label>
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary form-control">{{submit}}</button>
                </div>
                </div>
                    <small class="pb-2 text-danger text-center">{{error_btn}}</small>
            </div>

                    </div>
                </div>
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

<div class="modal fade" id="popOver" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
<form @submit.prevent="modify" class="needs-validation">

      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Update status</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
                   <div class="row">
              <div class="col-md-12">
                <input type="hidden" class="form-control d-none" v-model="token" required readonly>
                </div>
                <div class="col-md-12 m-1 mt-0 mb-1">
                     <section v-if="alertmodal!=''">
      <div v-bind:class="'alert '+ classnamemodal +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alertmodal}} </div>
  </section>
            </div>
            <div class="col-md-12">
                <div class="m-1">
                <div class="input-group">
                    <span class="input-group-text">Status</span>
                   <select v-model="listStatus" class="form-control" id="fitler" required>
                       <option disabled value="" selected>Select</option>
                       <option value="Approved">Approve</option>
                       <option value="Declined">Decline</option>
                       <option value="Cancelled">Cancel</option>
                   </select>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{errormodal}}</small>
                </div>
            </div>
                         <div class="col-md-12">
                     <div class="m-1 mt-3">
                    <label for="admin_comment" class="pb-1 text-dark">Support your action with comment</label>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-pencil"></i></span>
                        <textarea v-model="admin_comment" class="form-control" id="admin_comment" cols="30" rows="1" placeholder="Leave a comment"></textarea>
                    </div>
                    </div>
                    </div>

                </div>
        
      </div>
      <div class="modal-footer">
        
        <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{submitmodal}}</button>
      </div>

</form>
    </div>
  </div>
</div>

</div>
</template>

<script>
import axios from 'axios'
export default {
    data (){
        return{
        
        formSuccess: 0,
        info:[],
        auth_check: false,
        alert: null,
        checked: true,
        keyid_validate: this.$route.params.id,
        keyid:'',
        selectToggleValue:'',
        modifyItem: '',
        listStatus: '',
        isChecked:false,
        alertmodal: null,
        token: null,
        username: null,
        email: null,
        amount: null,
        duration: '',
        old_duration: '',
        extension: '',
        year_apply: '',
        month_apply: '',
        day_apply: '',
        year_expire: '',
        month_expire: '',
        day_expire: '',
        comment: null,
        admin_comment: null,
        expire_date: '',
        uniqueCode: null,
        loader: false,
        selectDefault:"Select",
        classname: '',
        submit:'Update',
        submittxt:'Update',
        submitmodal:'Update',
        submitmodaltxt:'Update',
        isDisabled: false,
        error_btn: null,
        record:null,
        norecord: '',
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
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
          formCheck: function(e){
            this.error_btn="";
            this.$confirm("Are you sure you want to update this?, click Ok to continue or Cancel to go back?").then(() => {
            this.submit="Please wait.."
            this.update()
            });
    e.preventDefault();
    },

       preview: function(){
        this.norecord = 'Synchronizing...'
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/loan/validate_data/', {
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
            this.username = this.info['surname'] + ' ' + this.info['firstname'] + ' ' + this.info['othername']
            this.email = this.info['email_one']
            this.amount = this.info['request_amount']
            this.duration = this.info['duration']
            this.old_duration = this.info['duration']
            this.uniqueCode = this.info['uniqueCode']
            this.year_apply = this.info['year_apply']
            this.month_apply  = this.info['month_apply']
            this.day_apply  = this.info['day_apply']
            this.year_expire = this.info['year_expire']
            this.month_expire  = this.info['month_expire']
            this.day_expire  = this.info['day_expire']
            this.expire_date  = this.info['expire_date']
            this.comment  = this.info['user_comment']
            this.admin_comment  = this.info['admin_comment']
            this.keyid = this.info['keyid']
            this.record = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable 
            }else{
            this.record = false
            this.classname=''
            this.alert=response.data.msg
            this.classname=response.data.classname
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        }).catch(()=>{
            this.record = false
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = false
            this.opacity = this.opacity_disable
        })
    },

        update: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        this.submit = 'Please wait..'
        const form = new FormData();
        form.append('amount', this.amount)
        form.append('duration', this.duration)
        form.append('old_duration', this.old_duration)
        form.append('extension', this.extension)
        form.append('year_apply', this.year_apply)
        form.append('month_apply', this.month_apply)
        form.append('day_apply', this.day_apply)
         form.append('year_expire', this.year_expire)
        form.append('month_expire', this.month_expire)
        form.append('day_expire', this.day_expire)
        form.append('expire_date', this.expire_date)
        form.append('email', this.email)
        form.append('admin_comment', this.admin_comment)
        form.append('username', this.info['surname'])
        form.append('uniqueCode', this.uniqueCode)
        form.append('keyid', this.keyid)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/loan/update/', form)
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

 modify: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        this.submitmodal = 'Please wait..'
        const form = new FormData();
        form.append('listStatus', this.listStatus)
        form.append('admin_comment', this.admin_comment)
        form.append('uniqueCode', this.uniqueCode)
        form.append('keyid', this.keyid)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/loan/modify/', form)
        .then(response => {
        if(response.data.status==response.data.statusmsg){
        this.classnamemodal=response.data.classname
        this.alertmodal=response.data.msg
        this.submitmodal=this.submitmodaltxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.formSuccess = 1
        }else{
        this.classnamemodal=response.data.classname
        this.alertmodal=response.data.msg
        this.submitmodal=this.submitmodaltxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.formSuccess = 2
        }
    }).catch(()=>{
        this.classnamemodal='alert-danger p-2'
        this.alertmodal=localStorage.getItem('error')
        this.submitmodal=this.submitmodaltxt
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