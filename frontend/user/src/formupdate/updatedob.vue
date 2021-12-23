
<template>
<div :style="opacity">
<AdminHeader>
<div class="container p-0">
<div class="row">
<div class="col-6">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"> Date of Birth </h5>
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
                <div class="row">
                    <div class="col-md-4">
                        <div class="m-1 mt-3">
                    <label for="day" class="pb-1 text-dark">Day</label>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-calendar-event"></i></span>
                    <select class="form-select p-0" v-model="day" id="day" required>
                 <option disabled value="" selected>Select</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                    <option value="7">7</option>
                    <option value="8">8</option>
                    <option value="9">9</option>
                    <option value="10">10</option>
                    <option value="11">11</option>
                    <option value="12">12</option>
                    <option value="13">13</option>
                    <option value="14">14</option>
                    <option value="15">15</option>
                    <option value="16">16</option>
                    <option value="17">17</option>
                    <option value="18">18</option>
                    <option value="19">19</option>
                    <option value="20">20</option>
                    <option value="21">21</option>
                    <option value="22">22</option>
                    <option value="23">23</option>
                    <option value="24">24</option>
                    <option value="25">25</option>
                    <option value="26">26</option>
                    <option value="27">27</option>
                    <option value="28">28</option>
                    <option value="29">29</option>
                    <option value="30">30</option>
                    <option value="31">31</option>
                    </select>
                    </div>
                    </div>
                    </div>
                    
                    <div class="col-md-4">
                     <div class="m-1 mt-3">
                    <label for="month" class="pb-1 text-dark">Month</label>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-calendar-event"></i></span>
                    <select class="form-select p-0" v-model="month" id="month" required>
                    <option disabled value="" selected>Select</option>
                    <option value="1">January</option>
                    <option value="2">February</option>
                    <option value="3">March</option>
                    <option value="4">April</option>
                    <option value="5">May</option>
                    <option value="6">June</option>
                    <option value="7">July</option>
                    <option value="8">August</option>
                    <option value="9">September</option>
                    <option value="10">October</option>
                    <option value="11">November</option>
                    <option value="12">December</option>
                    </select>
                    </div>
                    </div>
                    </div>

                    <div class="col-md-4">
                     <div class="m-1 mt-3">

                    <label for="year" class="pb-1 text-dark">Year</label>
                    <div class="input-group">
                    <span class="input-group-text"><i class="bi-calendar-event"></i></span>
                        <input type="text" maxlength="4" class="form-control" v-model="year" id="year" placeholder="Year of birth" required>
                    </div>
                    </div>
                    </div>
      
                    </div>
                    <small class="form-text text-muted"></small>
                </div>
            </div>
           <div class="col-md-8 mt-2 text-center">
           </div>

           <div class="col-md-4 mt-2 text-center d-flex justify-content-end">
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
        day: '',
        month: '',
        year: null,
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
            this.day = this.info['dob']
            this.month = this.info['mob']
            this.year = this.info['yob']
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

    validDigit: function (digits) {
    var re = /^\d+$/;
    return re.test(digits);
    },
    formCheck: function(e){
        var d = new Date();
        var currentYear = parseInt(d.getFullYear());
        if(!this.validDigit(this.year)){
            this.error_btn="Only number is required.";
        }else if(this.year.length > 4){
            this.error_btn="The year provided is invalid";
        }else if((currentYear - parseInt(this.year)) < 16){
            alert(currentYear - parseInt(this.year))
            this.error_btn="The year provided is invalid";
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
        form.append('dob', this.day)
        form.append('mob', this.month)
        form.append('yob', this.year)
        form.append('keyid', this.keyid_validate)
        form.append('emailid', this.emailid)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/user/updatedob/', form)
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