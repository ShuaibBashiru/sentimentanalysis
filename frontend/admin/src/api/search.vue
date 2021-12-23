<template>
<div :style="opacity">
  <GeneralHeader>

<div class="container p-0">
          <div class="row">
          <div class="col-md-12">
          <div class="p-3 ps-2 pe-2 bg w-100">
                            <h5 class="text-primary mt-0 mb-0"><strong>Repair and Troubleshooting of Computer laboratory equipment</strong></h5>
              <p class="text-white lead mt-0 mb-0"><small>Help yourself with accurate diagnosis</small></p>
          </div>
          </div>
      </div>
</div>

<div class="container p-0 mt-1">
          <div class="row">
          <div class="col-md-12">
          <div class="border p-2">
        <div class="input-group">
        <input type="text" class="form-control" v-model="search" required placeholder="Search faults" @keypress="searchby">
        <span class="input-group-text"> <i class="bi-search"></i> </span>
        </div>
          </div>
          <div class="col-md-9">
              <section v-if="record==true">
                  <div class="row">
                    <div class="col-md-12 p-2" v-for="(d, index) in info" :key="index">
                  <div class="m-2 border p-2">
                      <h5 class="mt-0 mb-0 text-primary"><strong> {{d['category_name']}}</strong></h5>
                  <h5 class=" mt-0 mb-0 text-muted"> Symptoms: {{d['title']}}</h5>
                  
                  <h5 class=" mt-0 mb-0 text-danger"><small class="text-info"><em>Common fault</em></small>: {{d['faults']}}</h5>
                  <small class="text-info"><em>Possible solution</em></small>
                    <p class="lead mt-0 mb-0 text-success"><small>{{d['solution_one']}}</small></p>
                  </div>
              </div>
                  </div>
              </section>
            <section v-else>
            <p class="text-danger mt-2">{{norecord}}</p>
            </section>
          </div>
          <div class="col-md-3"></div>
          </div>

      </div>
</div>

</GeneralHeader>
</div>
</template>
<style scoped>
h1, h2, h3, h4, h5, h6, p{
    font-family: "Geomanist book webfont',Arial,sans-serif";
line-height: 1.6;
}

.bg{
    background-image: url('../assets/items/background.png');
    background-repeat: no-repeat;
    background-size: cover;
    }

</style>
<script>
import axios from 'axios'
export default{
    data(){
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
        visibility: '',
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
methods:{
          searchby: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
       axios.get('/api/contents/search/', {
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
            this.info = ''
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
 
}
    
    }
</script>