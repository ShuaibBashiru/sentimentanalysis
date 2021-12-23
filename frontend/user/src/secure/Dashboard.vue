<template>
<div :style="opacity">
<AdminHeader>
<div class="container mb-4 p-0">
<div class="row  pb-3 pt-3 ps-3 pe-3 border">
<div class="col-md-8">
    <div class="row">
        <div class="col-md-2"><h5 class="mt-2">Analysis</h5> </div>
        <div class="col-md-2"> 
          <div class="input-group">
                 <select v-model="year" class="form-control" id="category_id" required>
             <option disabled value="" selected>Year</option>
             <option v-for="(d, index) in year_list" :key="index" :value="d['year_date']">{{d['year_date']}}</option>
          </select>
          <span class="input-group-text"><i class="bi-calender"></i></span>
          </div>
        </div>
        <div class="col-md-2">
          <div class="input-group">
            <select v-model="month" class="form-control" id="month" required @change="statistics">
            <option disabled value="" selected>Month</option>
            <option value="01">Jan</option>
            <option value="02">Feb</option>
            <option value="03">Mar</option>
            <option value="04">Apr</option>
            <option value="05">May</option>
            <option value="06">Jun</option>
            <option value="07">Jul</option>
            <option value="08">Aug</option>
            <option value="09">Sept</option>
            <option value="10">Oct</option>
            <option value="11">Nov</option>
            <option value="12">Dec</option>
          </select>
          <span class="input-group-text"><i class="bi-calender"></i></span>
        </div>
        </div>
    </div>
</div>
<div class="col-md-4 p-md-0">
<div class="d-flex justify-content-end">
<router-link to="contents"><button class="btn btn-primary text-center" @click="router.push('contents')">  <i class="bi-people"></i> Record </button></router-link>
</div>
</div>

</div>
</div>

<div class="container mb-3 p-0">
<div class="row">
<div class="col-md-4 pt-3 pb-3 border">
    <div class="d-flex m-2 mt-0 mb-0">
    <i class="bi-plus-circle text-primary" style="font-size: 2.5rem; color: cornflowerblue;"></i>
    <div>
        <big class="m-3 mb-0 text-muted">Positive</big>
        <p class="m-3 mt-0 lead"> {{stats_info['num_positive']}} </p>
    </div>
</div>
</div>

<div class="col-md-4 pt-3 pb-3 border">
    <div class="d-flex m-2 mt-0 mb-0">
    <i class="bi-dash-circle text-danger" style="font-size: 2.5rem; color: cornflowerblue;"></i>
    <div>
        <big class="m-3 mb-0 text-muted">Negative</big>
        <p class="m-3 mt-0 lead"> {{stats_info['num_negative']}} </p>
    </div>
</div>
</div>
<div class="col-md-4 pt-3 pb-3 border">
    <div class="d-flex m-2 mt-0 mb-0">
    <i class="bi-tree text-warning" style="font-size: 2.5rem; color: cornflowerblue;"></i>
    <div>
        <big class="m-3 mb-0 text-muted">Neutral</big>
        <p class="m-3 mt-0 lead"> {{stats_info['num_neutral']}} </p>
    </div>
</div>
</div>


</div>
</div>

<div class="container mb-4 p-0">
<div class="row justify-content-between">

<div class="col-md-6 mt-2 p-3 ps-4 pe-4 border">
<div class="row">
        <div class="col-md-12 mb-3 p-0">
    <p class="lead">Feedback summary</p>
    </div>

   <div class="col-md-6 p-0" v-for="(d, index) in stats_categ" :key="index">
        <div class="border rounded p-2 ps-2 pe-2 m-1">
        <div class="row">
            <div class="col-md-12"><big class="text-primary">{{d['category_name']}}</big></div>
            <div class="col-6"><small class="mt-4 mt-0 mt-1"> {{d['TotalItems']}}  </small></div>
            <div class="col-6"><small class="p-1 pt-0 pb-0 btn btn-outline-primary float-end">{{d['TotalItems']}}</small></div>
        </div>
        </div>   
    </div>
    
</div>


</div>


<div class="col-md-6 mt-2 p-3 ps-4 pe-4 border">
<div class="row">
        <div class="col-md-12 mb-3 p-0">
    <p class="lead">Percentage of feedback in <span class="text-primary">{{months[month_integer]}}, {{this.year}}</span></p>
    </div>

<div class="col-md-6 d-flex justify-content-center">
<div class="progress" style="height:200px; width:200px; border-radius:50%;">
    <div class="progress-bar bg-primary progress-bar-striped progress-bar-animated" role="progressbar" :style="'width:'+stats_info['positive']+'%'" :aria-valuenow="stats_info['positive']" aria-valuemin="0" aria-valuemax="100">{{stats_info['positive']}}%</div>
    <div class="progress-bar bg-danger progress-bar-striped progress-bar-animated" role="progressbar" :style="'width:'+stats_info['negative']+'%'" :aria-valuenow="stats_info['negative']" aria-valuemin="0" aria-valuemax="100">{{stats_info['negative']}}%</div>
    <div class="progress-bar bg-warning progress-bar-striped progress-bar-animated" role="progressbar" :style="'width:'+stats_info['neutral']+'%'" :aria-valuenow="stats_info['neutral']" aria-valuemin="0" aria-valuemax="100">{{stats_info['neutral']}}%</div>

</div>
</div>



<div class="col-md-6 mt-2">
<div class="row border rounded">
           <div class="col-md-12 pt-3 pb-3">
        <div class="row">
            <div class="col-12"><big class="text-primary">Positive: <span class="float-end text-primary"> {{stats_info['positive']}}% </span></big> </div>
        </div>   
    </div>

   <div class="col-md-12 pt-3 pb-3  border-top">
        <div class="row">
            <div class="col-12"><big class="text-danger">Negative: <span class="float-end text-danger"> {{stats_info['negative']}}% </span></big></div>
        </div>   
    </div> 
       <div class="col-md-12 pt-3 pb-3  border-top">
        <div class="row">
            <div class="col-12"><big class="text-warning">Neutral: <span class="float-end text-warning"> {{stats_info['neutral']}}% </span></big></div>
        </div>   
    </div> 
</div>

</div>
    </div>
    <div>
        
    <!-- </div> -->
</div>
</div>


</div>
</div>


</AdminHeader>
</div>
</template>

<style scoped>

</style>


<script>
import axios from 'axios'
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
        category_id: '',
        stats_info: [],
        stats_categ: [],
        year: '',
        month:'',
        month_integer: '',
        info: [],
        year_list: [],
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
        counter:'0',
        months: ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
    }
    },

    mounted(){
    this.get_month_year()
    this.get_years()
    this.statistics()
    }, 

    methods:{
    get_month_year: function(){
        const d = new Date()
        this.month_integer = d.getMonth()
        let new_month = d.getMonth() + 1
        this.year = d.getFullYear()
        if (new_month < 10) {
        this.month = 0+''+new_month
        }else {
        this.month = new_month
        }
    },


get_years: function(){
        this.norecord = 'Synchronizing...'
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/groups/',{
              params:{
                limitTo: this.displayNumber
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.norecord=''
            this.year_list = response.data.result
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


    statistics: function(){
        this.norecord = 'Synchronizing...'
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/statistics/',{
              params:{
                year: this.year,
                month: this.month
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.stats_info = response.data.stats_info
            this.stats_categ = response.data.stats_categ
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

    
    },


    }
</script>