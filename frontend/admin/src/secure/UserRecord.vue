<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="container">
    <div class="row">
        <div class="col-12">
            <div v-bind:class="classname">{{alert}}</div>
<div class="row border p-2 m-0 mt-2">
    <div class="col-md-5 d-flex justify-content-start">
    <h6 class="mt-2 text-primary"><i class="bi-person-plus" style="font-size: 1.5rem;"></i> User's Record </h6>
    </div>
    <div class="col-md-7 d-flex justify-content-end" @click="preview"><button class="btn btn-primary"><i class="bi-eye"></i> Preview</button></div>
</div>

<div class="row border p-2 m-0">
<div class="col-12">
    <div class="table-responsive">
        <!-- <input type="text" id="myInput" placeholder="Search"> -->
<table id="searchTable" class="table table-bordered nowrap" cellspacing="0" width="100%">
  <thead>
        <tr>
            <th>S/N</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Gender</th>
            <th>Age</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(d, index) in info" :key="index">
            <td>{{index + 1}}</td>
            <td>{{d[1]}} {{d[2]}}</td>
            <td>{{d[3]}}</td>
            <td>{{d[4]}}</td>
            <td>{{d[5]}}</td>
            <td>{{d[6]}}</td>
        </tr>

    </tbody>

</table>


    </div>
</div>
</div>

<!-- End of wrapper -->
    </div>
</div>

</div>
</div>
</div>
</template>

<script>
import axios from 'axios';
export default{
    data(){
        return {
            info:'',
            alert:null,
            progress:null,
            bulk:'',
            classname:'',
        }
    },
    methods:{
        preview: function(){
        this.norecord = 'Synchronizing...'
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait....'
            axios.get('/api/user_record/'

            ).then(response => {
               if(response.data.status == response.data.statusmsg){
                this.alert=''
                this.classname=''
                this.info = response.data.result
                console.log(response.data.result)
               }else{
                this.alert=response.data.msg
                this.classname=response.data.classname
                }
               
            }).catch((error)=>{
                this.classname='alert-danger p-2'
                this.alert=error

            })
        },
  
    },
    
    // Methods end
    created() {
        this.preview()
  }
}
</script>