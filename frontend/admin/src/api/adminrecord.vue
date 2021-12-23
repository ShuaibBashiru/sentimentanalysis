
<template>
<div :style="opacity">
<AdminHeader>
      <section v-if="alert!=''">
      <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
  </section>
<div class="container p-0">
<div class="row">
<div class="col-md-4">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"> Administrator (<span class="text-secondary">{{counter}}</span>)</h5>
</div>
</div>
<div class="col-md-8 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">

<div class="btn-group m-2" title="" role="group" aria-label="First group"><a href="/secure/adminaccount" class="btn btn-outline-primary text-center">  <i class="bi-plus" style="font-size: 1rem;"></i> New </a></div>
<div class="btn-group m-2" title="Menu" role="group" aria-label="First group">    <button class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Menu</button>
  <ul class="dropdown-menu">
    <li class="p-2 pb-0 pt-0"><strong><a href="#">Records</a></strong> </li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="listcounter">Update status</a></li>
    <li><hr class="dropdown-divider"></li>
    <li class="p-2 pb-0 pt-0"><strong><a href="#">Download</a></strong> </li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#" @click="downloadfile" data-bs-toggle="modal" data-bs-target="#downloadbox">Excel</a></li>
  </ul></div>
<div class="btn-group m-2" title="Refresh" role="group" aria-label="First group">
    <div class="input-group">
        <select name="displayNumber" v-model="displayNumber" @change="preview" class="form-control">
            <option value="5">5</option>
            <option value="10">10</option>
            <option value="50">50</option>
            <option value="100">100</option>
            <option value="500">500</option>
            <option value="1000">1000</option>
            <option value="1">All</option>
        </select>
        <span class="input-group-text" @click="preview"><i class="bi-arrow-clockwise" style="font-size: 1rem;"></i></span>
    </div>
    </div>
</div>

</div>
</div>
</div>

<div class="container p-0">
<div class="border">
<div class="row">
<div class="col-md-12">
    <div class="p-2">
                      <form class="needs-validation">
            <fieldset class="border p-2 pt-0">
                <legend class="w-auto" style="float: none; padding: inherit;"></legend>
            <div class="row">
            <div class="col-md-5">
                <div class="m-1">
                <div class="input-group">
                    <span class="input-group-text">Filter</span>
                   <select @change="filter()" v-model="filterlist" class="form-control" id="fitler">
                       <option disabled value="" selected>Select</option>
                       <option value="1">Active</option>
                       <option value="0">Inactive</option>
                   </select>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>
         <div class="col-md-7">
                <div class="m-1">
                <div class="input-group">
                    <input type="text" name="search" v-model="search" @keypress="searchby" maxlength="100" class="form-control" required placeholder="Type here to search">
                    <span class="input-group-text" @click="preview">Clear</span>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{error}}</small>
                
                </div>
            </div>

                </div>
                </fieldset>
            </form>
        
    </div>
</div>
</div>
</div>
</div>

<div class="container p-0">
    <div class="row">
        <div class="col-md-12">
            <section v-if="record==true">
            <div class="table-responsive">
                <table class="table table-hover table-bordered" id="myTable">
                    <thead>
                        <tr>
                            <th scope="col"><i class="bi-check-square btn p-0 text-primary"></i></th>
                            <th scope="col">Name</th>
                            <th scope="col">Email</th>
                            <th scope="col">Phone</th>
                            <th scope="col">Last Modified</th>
                            <th scope="col" class="text-center">Status</th>
                            <th scope="col" class="text-center">Edit</th>
                        </tr>
                       </thead>
                       <tbody>
                        <tr v-for="(d, index) in info" :key="index">
                            <td> <div class="form-check"><input type="checkbox" name="checkbox" :id="d['id']" :value="d['id']" v-model="list_id" class="form-check-input"></div> </td>
                            <td>{{d['surname']}} {{d['firstname']}} {{d['othername']}}</td>
                            <td>{{d['email_one']}}</td>
                            <td>{{d['phone_one']}}</td>
                            <td>{{d['date_modified']}} {{d['time_modified']}}</td>
                            <td class="text-center" v-if="d['status_id']==1"> <i class="bi-check-square btn p-0 text-primary"></i></td>
                            <td class="text-center" v-else> <i class="bi-x-square btn p-0 text-danger"></i></td>
                            <td class="text-center"> <a :href="'/secure/u_adminrecord/'+d['email_one']+'/'+d['id']"><i class="bi-pencil-square btn p-0 text-primary"></i> </a></td>
                        </tr>
                       </tbody>
                </table>
            </div>
</section>
<section v-else>
    <p class="text-danger mt-2">{{norecord}}</p>
</section>

        </div>
    </div>
    </div>

</AdminHeader>

<!-- Modal container -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
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

                    <p class="">You are updating <strong>{{selectedlist}}</strong> record(s)</p>
                </div>
            <div class="col-md-12">
                <div class="m-1">
                    <div class="input-group">
                    <span class="input-group-text">Status</span>
                   <select v-model="listStatus" class="form-control" id="fitler" required>
                       <option disabled value="" selected>Select</option>
                       <option value="1">Active</option>
                       <option value="0">Inactive</option>
                   </select>
                </div>
               </div>
            </div>

            <div class="col-md-12">
                 <small class="text-danger">{{errormodal}}</small>
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


<!-- modal -->
<div class="modal fade" id="downloadbox" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">

      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Download File</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>

      <div class="modal-body">
                   <div class="row">
            <div class="col-md-12">
                <div class="m-1">
                    <p class="text-primary">{{downloadmsg}}</p>
                </div>
            </div>
                </div>
      </div>
      <div class="modal-footer">
        
       <section v-if="isdownload==true">
            <a :href="baseData" :download="baseDataname"><button type="submit" class="btn btn-primary">Download now</button></a>
       </section>
      </div>

    </div>
  </div>
</div>

</div>
</template>

<script>
import axios from 'axios'
import $ from "jquery";
export default {
    data (){
        return{
        
        serverMessage: 'Please wait...',
        auth_check: false,
        token: '',
        baseData: '',
        baseDataname: '',
        downloadmsg:'',
        isdownload:false,
        alert: null,
        alertmodal: null,
        error: '',
        info: [],
        filterlist:'',
        search:'',
        checked: true,
        list_id: [],
        get_list_array: '0',
        listStatus:'',
        displayNumber:10,
        selectToggleValue: '',
        selectedlist: null,
        isChecked:false,
        loader: false,
        loadermodal: false,
        selectDefault:"Select",
        classname: '',
        classnamemodal: null,
        submit: 'Submit',
        submittxt:'Submit',
        searchbtn:'Search',
        searchbtntxt:'Search',
        isDisabled: false,
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
        error_btn: null,
        errormodal: null,
        record:false,
        norecord: '',
        counter:'0'
    }
    },

    created(){
    this.preview()
    this.tokenize()
    }, 

    methods:{
    formCheckStatus: function(e){
        if (this.token.length < 1) {
        this.errormodal="Check network connection or reload this page";
        }else if(this.list_id.length < 1 || this.get_list_array.length < 1){
        this.errormodal="Please select the record(s) you wanted to update.";
        }else{
        this.updateStatus()
        }
    e.preventDefault();
    },
    updateStatus: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.submit='Please wait..'
        const form = new FormData();
        form.append('listStatus', this.listStatus)
        form.append('keyid', this.get_list_array)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/admin/update_status/', form)
        .then(response => {
        if(response.data.status==response.data.statusmsg){
        this.classnamemodal=response.data.classname
        this.alertmodal=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.unselectAll();
        this.preview()
        }else{
        this.classnamemodal=response.data.classname
        this.alertmodal=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false

        }
    }).catch(()=>{
        this.classnamemodal='alert-danger'
        this.alertmodal=localStorage.getItem('error')
        this.submit=this.submittxt
        this.$Progress.fail()
        this.isDisabled = false

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
      this.alert=''
      }else{
      this.$Progress.finish()
      this.isDisabled = false
      
      this.alert=localStorage.getItem('error')
      this.classname='alert-danger p-2'
      }
    
  }).catch(()=>{
      this.$Progress.fail()
      this.isDisabled = false
      
      this.alert=localStorage.getItem('error')
      this.classname='alert-danger p-2'
  })
  },

    preview: function(){
        this.norecord = 'Synchronizing...'
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/admin/list/',{
              params:{
                limitTo: this.displayNumber
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.info = response.data.result
            this.counter = this.info.length
            this.record = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }else{
            this.record = false
            this.counter = '0'
            this.alert=''
            this.norecord=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        
        }).catch(()=>{
            this.record = false
            this.norecord=''
            this.counter = '0'
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = true
            this.opacity = this.opacity_disable
        })
    },

       filter: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
       axios.get('/api/admin/filter/', {
            params:{
                'status_id': this.filterlist
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.info = response.data.result
            this.counter = this.info.length
            this.record = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }else{
            this.record = false
            this.counter = '0'
            this.alert=''
            this.norecord=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        
        }).catch(()=>{
            this.record = false
            this.norecord=''
            this.counter = '0'
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = true
            this.opacity = this.opacity_disable
        })
    },
       searchby: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
       axios.get('/api/admin/search/', {
            params:{
                'search': this.search
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.info = response.data.result
            this.counter = this.info.length
            this.record = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }else{
            this.record = false
            this.counter = '0'
            this.alert=''
            this.norecord=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        
        }).catch(()=>{
            this.record = false
            this.norecord=''
            this.counter = '0'
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = true
            this.opacity = this.opacity_disable
        })
    },
        listcounter: function(){
        this.selectedlist = this.list_id.length
        this.get_list_array = this.list_id
        this.errormodal="";
        this.alertmodal="";
        this.classnamemodal="";
        },
  
  
        downloadfile: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.downloadmsg='Please wait...'
        axios.get('/api/admin/download/', {
            params:{
                "filetype":"excel"
            }
        },  this.loader=true, this.loaderstatus='block')
        .then(response => {
           if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.record = true
            this.norecord=''
            this.downloadmsg = response.data.msg
            this.baseDataname=response.data.baseDataname
            this.baseData=response.data.baseData
            this.isdownload=true
            this.$Progress.finish()
            this.isDisabled = false
            }else{
            this.norecord=''
            this.downloadmsg=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            }

        }).catch(()=>{
            this.norecord=''
            this.classname=''
            this.downloadmsg=localStorage.getItem('error')
            this.$Progress.finish()
            this.isDisabled = false
        })
    },

    selectToggle: function(){
    var checkboxes = document.getElementsByName('checkbox');
    if(this.selectToggleValue == false){
        var newlist=[]
        $(checkboxes).each(function() {
            this.checked = true;
            newlist.push(this.value)                        
        });
        this.list_id = newlist
    }else{
        $(checkboxes).each(function() {
            this.checked = false;
        });
        this.list_id = []

      }
        
          },
        unselectAll: function(){
        var checkboxes = document.getElementsByName('checkbox');
             $(checkboxes).each(function() {
            this.checked = false;
        });
        this.list_id = []
        },


    },


    }
</script>