<template>
    
<div class="container-fluid ps-0 pe-0 ps-md-5 pe-md-5 mt-3 border-bottom light_bg" style="">
    <div class="row ps-3 pe-3 ps-md-3 pe-md-3">
        <!-- <div class="col-md-1"></div> -->
                   <div class="col-md-6 bg-light">
            <div class="row"> 
                <div class="col-md-12 mt-md-0">
            <p class="lead pt-4"><small>   Technologists and Technicians in Computer engineering 
              Laboratories have been conducting practicals for students with a number of equipment, and maintenance
               and detection of faults of such equipment are being carried out with a conventional approach.    </small>  </p>    </div>
            <div class="col-md-12 mt-5">
   <a v-bind:class="'btn btn-primary'" href="/site/search">Search Faults</a> 

              </div>

            </div>
        </div>
        <div class="col-md-6 mt-2 mt-md-0 bg-light">
            <div class="row p-0 m-0 wrapper">
            <Vslick v-bind="singleSlide" class="p-0">
                 <div class="col-md-12 m-0 p-0 box">
                    <img src="@/assets/items/banner3.png" class="img-responsive rounded w-100 m-0 p-0" alt=" "
                        height="230">
                </div>
               <div class="col-md-12 m-0 p-0 box">
                <img src="@/assets/items/banner.jpg" class="img-responsive rounded w-100 m-0 p-0" alt=" "
                        height="230">
                </div>
            </Vslick>
            </div>
            <br/>
        </div>

        <!-- <div class="col-md-1"></div> -->
    </div>
</div>
<!-- Explore our most Loved Items -->
<!-- Best selling Bodysuits -->
<!-- Popular -->
</template>
<script>
import appsettings from '../json/myapp.json'
import Vslick from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
export default{
    components:{
        Vslick,
    },
    data(){
        return{
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
    mounted(){

    },
    methods:{

    }
}

</script>