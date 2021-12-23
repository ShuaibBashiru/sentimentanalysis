<template>
<div>
<div class="container-fluid ps-0 pe-0 ps-md-5 pe-md-5 mt-3" style="">
    <div class="row ps-3 pe-3 ps-md-3 pe-md-3">
        <div class="col-md-8 mt-2">
            <div class="col-12 border-bottom pb-3">
                <div class="row">
    
                    <div class="col-md-4 mt-2 mb-2">
                    <div class="input-group">
                        <span class="input-group-text"><i class="bi-filter-left"></i></span>
                     <select v-model="category_id" class="form-control" id="category" required @change="searchby" >
                        <option disabled value="" selected>Select</option>
                        <option v-for="(d, index) in category_list" :key="index" :value="d['id']">{{d['category_name']}}</option>
                   </select>
                    </div>
                    </div>

                     <div class="col-md-3 mt-2 mb-2">
                    </div>
                </div>

            </div>
            <div class="row mt-4">
                <div class="col-12 m-2 ms-0"><h5 class="text-left">--  Devices --</h5></div>
                <div class="col-md-4">
                 <div class="wrapper p-2">
                        <div class=""></div>
                    <div class="list-items"><img src="@/assets/items/item1.png" class="img-responsive rounded w-100 m-0 p-0" alt=" "
                        height=""></div>
                    <div>
                        <!-- <p class="mb-1">Device 1</p> -->
                        </div>
                </div>
                </div>

                <div class="col-md-4">
                 <div class="wrapper p-2">
                        <div class=""></div>
                    <div class="list-items"><img src="@/assets/items/item2.jpg" class="img-responsive rounded w-100 m-0 p-0" alt=" "
                        height=""></div>
                    <div>
                        <!-- <p class="mb-1">Device 2</p> -->
                        </div>
                </div>
                </div>

                  <div class="col-md-4">
                 <div class="wrapper p-2">
                        <div class=""></div>
                    <div class="list-items"><img src="@/assets/items/item3.jpg" class="img-responsive rounded w-100 m-0 p-0" alt=" "
                        height=""></div>
                    <div>
                        <!-- <p class="mb-1">Device 3</p> -->
                        </div>
                </div>
                </div>




            </div>
        </div>
        <div class="col-md-4 mt-2">
            <div class="wrapper shadow p-2 rounded">
                <div class="row">
                    <div class="col-md-12">
                        <h5 class="pb-1 sitecolor">Categories</h5>
                             <div class="bg-secondary" style="width:30px; height:1px;"> </div>
                        </div>
                    <div class="col-md-12 mt-5">
                        <div v-for="(d, index) in info_items" :key="index">
                                <ul class="list-unstyled ps-0 border-bottom ms-3">
                                <li class="mb-1">
                                <p class=" pb-0 mb-1 align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#cat1" aria-expanded="false">
                                {{d['title']}}
                                <!-- <i class="bi-chevron-down  float-end"></i> -->
                                </p>
                                <div class="collapse" id="cat1">
                                </div>
                                </li>  
                                </ul>
                        </div>
                     
                    </div>
                </div>

            </div>
        </div>
        <!-- end col 4 -->
    </div>
</div>
</div>
</template>
<style scoped>
.list-items:hover{
opacity: 0.8;
cursor: pointer;
padding: 10px;
}
</style>
<script>
import axios from 'axios'
import appsettings from '../json/myapp.json'
// import Vslick from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
export default{
    components:{
        // Vslick,
    },
    data(){
        return{
            alert: null,
            alertmodal: null,
            error: '',
            info: [],
            category_list: [],
            category_id: '',
            info_items: [],
            search: '',
            isDisabled: false,
            opacity_enable:'opacity:0.7; pointer-events: none;',
            opacity_disable:'opacity:1; pointer-events:All;',
            "media":appsettings.media,
            "appinfo":appsettings.appinfo,
             singleSlide:{
                 infinite: true,
                 draggable: true,
                arrows: true,
                dots: true,
                rows:1,
                slidesToShow:1,
                slidesToScroll:1,
                swipe:true, 
                swipeToSlide:true,
                useCSS:true,
                autoplay:true,
                centerMode:true,
                centerPadding:'0',
                adaptiveHeight: true,
                mobileFirst: true,
                responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            },

            {
              breakpoint: 767,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            },
            {
              breakpoint: 639,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            },

          ]
            },
        }
    },
    created(){
        this.category_filter()
    },
    methods:{
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

 searchby: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
       axios.get('/api/item_category/search/', {
            params:{
                'search': this.search
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.info_items = response.data.result
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


    }
}

</script>