
<template>
<div :style="opacity">
<AdminHeader>
<div class="container p-0">
<div class="row">
<div class="col-6">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"> New Menu </h5>
</div>
</div>
<div class="col-6 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" role="group" aria-label="First group" @click="$router.go(-1)"><button class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </button></div>

</div>
</div>

</div>
</div>
  <section v-if="alert!=''">
      <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
  </section>

<div class="container p-0">
<div class="border">
<div class="row">
<div class="col-md-12">
    <div class="p-2">
        <section v-if="formSuccess == 0">
            <form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="p-2 pt-0">
                    <div class="row m-md-0">
            <div class="col-md-6 mt-1">
                <div class="m-1 mt-3">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                <div class="input-group">
                    <span class="input-group-text">Category</span>
                    <select v-model="category" class="form-control" id="menu" required>
                       <option disabled value="" selected>Select</option>
                        <option value="Web">Web content</option>
                        <option value="Loan">Loan</option>
                        <option value="Payment">Payment</option>
                        <option value="Upload">Upload</option>
                        <option value="Mailing">Mailing</option>
                        <option value="Users">Users</option>
                        <option value="Admin">Admin</option>
                        <option value="Settings">Settings</option>
                        <option value="Dashboard">Dashboard</option>

                   </select>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>

         <div class="col-md-6">
                <div class="m-1 mt-3">
                <div class="input-group">
                     <span class="input-group-text">Menu name</span>
                    <input type="text" name="menu" v-model="menuname" class="form-control" required placeholder="Type here">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                </div>
            </div>
         <div class="col-md-6">
                <div class="m-1 mt-3">
                <div class="input-group">
                     <span class="input-group-text">Display name</span>
                    <input type="text" name="displayname" v-model="displayname" class="form-control" required placeholder="Type here">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                </div>
            </div>
            <div class="col-md-6 d-flex justify-content-end">
                <div class="m-1 mt-3">
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{submit}}</button>
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
                <button class="btn btn-warning m-2" @click="$router.go(0)">Create New</button>
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

</AdminHeader>

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
        error: '',
        info: [],
        checked: true,
        category: '',
        menuname: null,
        displayname: '',
        loader: false,
        loadermodal: false,
        selectDefault:"Select",
        classname: '',
        classnamemodal: null,
        submit: 'Submit',
        submittxt:'Submit',
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
    }, 
    methods:{
    showForm: function(){
    this.formSuccess = 0
      },
      formCheck: function(e){
       this.error_btn="";
            this.$confirm("You are about to submit this form, click Ok to continue or Cancel to go back?").then(() => {
            this.submit="Please wait.."
            this.addNew()
            });
    e.preventDefault();
    },
    addNew: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        this.submit='Please wait..'
        const form = new FormData();
        form.append('category', this.category)
        form.append('menuname', this.menuname)
        form.append('displayname', this.displayname)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/adminmenu/new/', form)
        .then(response => {
        if(response.data.status==response.data.statusmsg){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.formSuccess = 1
        this.category = ''
        this.menuicon = ''
        this.menuname = ''
        this.displayname = ''
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