<template>
<div>
    <AdminHeader/>
    <div class="col-md-10 col-md-offset-2 col-12 maindiv">
<section v-if="loader==false">
<div class="col m-2 mt-0 mb-1"><div v-bind:class="classname">{{alert}}</div></div>

<div class="container">
<div class="row">
<div class="col-md-4">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"><i class="bi-person-plus" style="font-size: 1.5rem;"></i> Widgets </h5>
</div>
</div>
<div class="col-md-8 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" role="group" aria-label="First group"><a href="#" class="btn btn-outline-primary text-center" @click="preview">  <i class="bi-plus"></i> New </a></div>
<div class="btn-group m-2" role="group" aria-label="First group"><a href="#" class="btn btn-outline-secondary text-center" @click="preview">  <i class="bi-arrow-clockwise"></i> Refresh </a></div>
<div class="btn-group m-2" role="group" aria-label="First group"><a href="#" class="btn btn-outline-primary text-center dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"> Menu </a>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Download report</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Excel</a></li>
    <li><a class="dropdown-item" href="#">PDF</a></li>
    <li><a class="dropdown-item" href="#">DOCS</a></li>
  </ul></div>
</div>

</div>
</div>
</div>
<div class="container">
<div class="border">
<div class="row">
<div class="col-md-12">
    <div class="p-2">
            <form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="border p-2 pt-0">
                <legend class="w-auto" style="float: none; padding: inherit;">New</legend>
            <div class="row">
            <div class="col-md-5">
                <div class="m-1">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">Widget</button>
                    
                   <select v-model="widget" class="form-control" id="widget" required>
                       <option disabled value="" selected>Select</option>
                       <option value="Banner">Banner</option>
                       <option value="Slider_single_row">Slider-Single-Row</option>
                       <option value="Slider_double_row">Slider-Double-Row</option>
                       <option value="List_three_columns">List-Three-Columns</option>
                       <option value="List_Four_columns">List-Four-Columns</option>
                       <option value="Testimonie">Testimonies</option>
                       <option value="Partners">Partners</option>
                   </select>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{err_widget}}</small>
                
                </div>
            </div>
         <div class="col-md-5">
                <div class="m-1">
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">Title</button>
                    <input type="text" name="title" v-model="title" maxlength="100" class="form-control" required placeholder="Name this widget for quick reference">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>

            <div class="col-md-2 d-flex justify-content-end">
                <div class="m-1">
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{submit}}</button>
                </div>
                </div>
                    <small class="pb-2 text-danger text-center">{{error_btn}}</small>
            </div>

                </div>
                </fieldset>
            </form>
        
    </div>
</div>
</div>
</div>
</div>

<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="table-responsive">
                <table class="table border" id="myTable">
                    <thead>
                        <tr>
                            <th><div class="form-check"><input type="checkbox" @click="selectToggle(this)" v-model="selectToggleValue" class="form-check-input"></div></th>
                            <th>Name</th>
                            <th>Title</th>
                            <th>Last Modified</th>
                            <th class="text-center">Status</th>
                            <th class="text-center">Edit</th>
                            <th class="text-center">Delete</th>
                        </tr>
                        <tr v-for="(d, index) in info" :key="index">
                            <td> <div class="form-check"><input type="checkbox" name="checkbox" :id="d['id']" :value="d['id']" v-model="list_id" class="form-check-input"></div> </td>
                            <td>{{d['widgetName']}}</td>
                            <td>{{d['widgetTitle']}}</td>
                            <td>{{d['date_modified']}} {{d['time_modified']}}</td>
                            <td class="text-center" v-if="d['status_id']==1"> <i class="bi-check-square btn p-0 text-primary"></i></td>
                            <td class="text-center" v-else> <i class="bi-x-square btn p-0 text-danger"></i></td>
                            
                            <td class="text-center"> <i class="bi-pencil-square btn p-0 text-primary"></i> </td>
                            <td class="text-center"> <i class="bi-trash btn p-0 text-danger"></i>  </td>
                        </tr>
                    </thead>
                </table>
            </div>
        </div>
    </div>
    </div>
    
</section>
<section v-else>
   <div class="container-fluid">
       <div class="row mt-5 ">
           <div class="col-12 mt-5 d-flex justify-content-center">
<div class="lds-roller"><div></div><div></div><div></div></div>
           </div>
           <div class="col-12 mt-5 d-flex justify-content-center"><small></small></div>
       </div>
   </div>
</section>
</div>

</div>
</template>
<script>
import axios from 'axios'
import $ from "jquery";
export default {
    data (){
        return{
        auth_check: false,
        alert: null,
        info: [],
        checked: true,
        list_id: [],
        selectToggleValue:'',
        isChecked:false,
        alertmodal: null,
        token: null,
        widget: null,
        title: null,
        loader: false,
        err_widget: null,
        err_title: null,
        selectDefault:"Select",
        classname: '',
        submit:'Submit',
        isDisabled: false,
        error_btn: null,
    }
    },

    created(){
    this.tokenize()
    this.preview()
    }, 

    methods:{
    formCheck: function(e){
        this.addwidget()
    e.preventDefault();
    },

    addwidget: function(){
        this.loader=true
    const form = new FormData();
        form.append('widget', this.widget)
        form.append('title', this.title)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/widget/', form)
        .then(response => {
        if(response.data.status==response.data.statusmsg){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit="Submit"
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit="Submit"
        }
        this.loader=false
        this.preview()
    }).catch(()=>{
        this.loader=false
        this.classname='alert-danger p-2'
        this.alert=localStorage.getItem('error')
        this.submit="Submit"
    })  
    },

    preview: function(){
        this.norecord = 'Synchronizing...'
        this.loader = true
        axios.get('/api/widget/')
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.info = response.data.result
            }else{
            this.alert=response.data.msg
            this.classname=response.data.classname
            }
            this.loader=false

        }).catch(()=>{
            this.loader=false
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
        })
    },

    tokenize: function(){
    const form = new FormData();
    form.append('token', Math.random(9,99999))
    axios.get('/auth/tokenize/',form, {
    }).then(response => {
        if(response.data.status==response.data.statusmsg){
        this.token=response.data.key
        axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
        }else{
        this.alert=localStorage.getItem('error')
        }
        
    }).catch(()=>{
        this.classname='alert-danger p-2'
       this.alert=localStorage.getItem('error')

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


    },


    }
</script>