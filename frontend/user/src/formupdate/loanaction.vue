
<template>
<div :style="opacity">
<AdminHeader>
<div v-bind:class="'alert '+ classname +' ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
<section v-if="record==true">
<div class="container mb-3 mb-md-0 p-md-5 pt-md-0 pb-md-3">
<div class="row">
<div class="col-md-12 p-0">
<h2 class="text-primary"> Loan </h2>
<div class="row">
    <div class="col-md-10">
        <p class="text-muted">Profile and Loan information.</p>
    </div>
    <div class="col-md-2"><button class="btn btn-primary float-end mb-1">Download</button></div>
</div>
</div>
<div class="col-md-12 p-0">
    <div class="border rounded pb-2">
        <div class="row p-md-2 pt-1 pb-3 m-0 mb-1 mt-1">
        <div class="col-md-9">
        <h4>Basic info</h4>
        <p class="text-muted"></p>
        </div>
        <div class="col-md-3">
        </div>
        </div>
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

<div class="container mb-3 mb-md-0 p-md-5 pt-md-2 pb-md-3">
<div class="row">
<div class="col-md-12 p-0">
    <div class="border rounded pb-2">
        <div class="row p-md-2 pt-1 pb-3 m-0 mb-1 mt-1">
        <div class="col-12">
        <h4>Loan</h4>
        </div>
        </div>
        <div class="row p-md-2 m-0 pt-md-3 pb-md-3 hover-effect">
            <div class="row m-0 p-0">
                <div class="col-8 p-3 pt-0 pb-0">
                   <div class="row">
                        <div class="col-md-4 d-flex justify-content-start"> <strong><p class="lead p-md-0 m-md-0" style="font-size:14px;">Date apply: {{day_apply}}-{{month_apply}}-{{year_apply}}</p> </strong></div>
                        <div class="col-md-4 d-flex justify-content-start"> <strong><p class="lead p-md-0 m-md-0" style="font-size:14px;">Due date: {{day_apply}}-{{month_apply}}-{{year_apply}}</p> </strong></div>
                        <div class="col-md-4 d-flex justify-content-start"> <strong><p class="lead p-md-0 m-md-0" style="font-size:14px;">Status: Not paid</p> </strong></div>
                   </div>
                </div>
                <div class="col-md-4">
                    <div class="col-12 d-flex justify-content-end"><button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#popOver">Modify</button> </div>
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
<form @submit.prevent="formCheckStatus" class="needs-validation">

      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Update status</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
                   <div class="row">
              <div class="col-md-12">
                <input type="hidden" class="form-control d-none" v-model="token" required readonly>
                <input type="hidden" class="form-control d-none" v-model="get_list_array">
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
                       <option value="Approved">Approved</option>
                       <option value="Declined">Declined</option>
                       <option value="Cancelled">Cancelled</option>
                   </select>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{errormodal}}</small>
                </div>
            </div>
                         <div class="col-md-12">
                     <div class="m-1 mt-3">
                    <label for="comment" class="pb-1 text-dark">Support your action with comment</label>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-pencil"></i></span>
                        <textarea v-model="comment"  class="form-control" id="comment" cols="30" rows="1" placeholder="Leave a comment"></textarea>
                    </div>
                    </div>
                    </div>

                </div>
        
      </div>
      <div class="modal-footer">
        
        <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{submit}}</button>
      </div>

</form>
    </div>
  </div>
</div>


</div>
</template>
<style scoped>
.hover-effect:hover{
    background-color:rgba(178, 60, 253, 0.2);
}
</style>
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
        listStatus: '',
        keyid_validate: this.$route.params.id,
        keyid:'',
        selectToggleValue:'',
        modifyItem: '',
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
        comment: null,
        uniqueCode: null,
        loader: false,
        selectDefault:"Select",
        classname: '',
        submit:'Update',
        submittxt:'Update',
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
            this.username = this.info['surname'] + ' ' + this.info['firstname']
            this.email = this.info['email_one']
            this.amount = this.info['request_amount']
            this.duration = this.info['duration']
            this.old_duration = this.info['duration']
            this.uniqueCode = this.info['uniqueCode']
            this.year_apply = this.info['year_apply']
            this.month_apply  = this.info['month_apply']
            this.day_apply  = this.info['day_apply']
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
        form.append('email', this.email)
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