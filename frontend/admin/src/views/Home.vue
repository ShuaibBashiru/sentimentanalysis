<template>
<div :style="opacity">
    <GeneralHeader>
<div class="container-fluid mt-3 p-0 bodyBg">
<div class="row p-0 d-flex justify-content-center">

    <div class="col-md-6 d-flex justify-content-end">
      <div class="">
          <p class="lead mt-2 text-success">Welcome!, here we take your feedback seriously, kindly take a minute to tell us your experience in any of the category provided.  </p>
        <img src="../assets/images/demo2.png" alt="" style="" class="img-responsive w-100">
      </div>
    </div>

    <div class="col-md-5 pe-md-4 ps-md-4 rounded mt-2">
  <form @submit.prevent="formCheck" role="form">
  <div class="form-row border pt-2 pe-4 ps-4 pb-4 rounded">
<div class="form-group col">
  <section v-if="alert!=''">
      <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
  </section>

</div>

    <div class="form-group mt-1 col">
        <label for="userid" class="text-muted pb-2">Category</label>
        <input type="hidden" v-model="token" required>
         <select v-model="category_id" class="form-control" id="category" required>
             <option disabled value="" selected>Select</option>
             <option v-for="(d, index) in category_list" :key="index" :value="d['id']">{{d['category_name']}}</option>
          </select>
    </div>

    <div class="form-group mt-4 col">
        <label for="userid" class="text-muted pb-2">Email address</label>
      <input type="email" class="form-control form-control" v-model="userid" placeholder="Enter email" id="userid" required maxlength="100" minlength="10">
    </div>

    <div class="form-group mt-4 col">
        <label for="comments" class="text-muted pb-2">Your comments</label>
      <div class="input-group">
        <textarea class="form-control" id="comments" placeholder="Give a brief details of your feedback" v-model="comments" required>
        </textarea>
        
      </div>
    </div>


      <div class="form-group mt-5 col">
     <div class="row">
       <div class="col-md-12">
         <button type="submit" name="signin" class="btn btn-success form-control" :disabled="isDisabled">{{submit}}</button></div>
     </div>
    </div>
   

  </div>
</form>
<!-- <div class="p-2">
      <p class="text-center"> User sign in? <a href="/site/signin/user" class="text-right">
        Sign in
      </a></p>
</div> -->
    </div>
</div>

</div>
  </GeneralHeader>
</div>
</template>
<style>
body{
  background-image: url('../assets/images/bg.jpg');
  background-size: 100%;
}
</style>
<script>
import axios from 'axios'
export default {
data(){
  return{
     formSuccess: 0,
        auth_check: false,
        token: '',
        alert: null,
        alertmodal: null,
        error: '',
        info: [],
        category_list: [],
        checked: true,
        category_id: '',
        category: '',
        comments: null,
        userid: null,
        displayname: '',
        loader: false,
        loadermodal: false,
        selectDefault:"Select",
        classname: '',
        classnamemodal: null,
        submit: 'Submit feedback',
        submittxt:'Submit feedback',
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
this.category_filter()
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
        form.append('category', this.category_id)
        form.append('email', this.userid)
        form.append('comments', this.comments)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/feedback/new/', form)
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
        this.comments = ''
        this.userid = ''
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
    category_filter: function(){
        this.norecord = 'Synchronizing...'
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/item_category/category/',{
              params:{
                limitTo: this.displayNumber
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.norecord=''
            this.category_list = response.data.result
            this.counter = this.info.length
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }else{
            this.counter = '0'
            this.alert=''
            this.norecord=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        
        }).catch(()=>{
            this.norecord=''
            this.counter = '0'
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = true
            this.opacity = this.opacity_disable
        })
    },

   



},
// End of methods

}

</script>