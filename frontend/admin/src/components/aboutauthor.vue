<template>
    <div>
<div class="container-fluid ps-0 pe-0 ps-md-5 pe-md-5 mt-5 pt-3 border-top light_bg" style="">
    <div class="row ps-3 pe-3 ps-md-3 pe-md-3">
        <!-- <div class="col-md-1"></div> -->
        <div class="col-md-6 bg-light">
            <div class="wrapper p-2">
            <div class="mt-5">
            <h5 class="gradient_txt">{{settings.ownerstatus}}</h5>
            <p class="lead"><small>{{settings.ownername}}</small></p>
            <p class="lead pt-2">{{settings.ownerabout}}</p>
        </div>
        </div>
        </div>
        <div class="col-6">
            <div class="wrapper p-2">
            <div class=""><img src="@/assets/images/DSC_5146(1).jpg" class="img-responsive rounded w-100 m-0 p-0" alt=" "
            height=""></div>
            </div>
        </div>
    </div>
</div>



    </div>
</template>
<script>
import appsettings from '../json/myapp.json'
export default {
    data(){
        return {
            info:[],
            "settings":appsettings.settings,
        }
    }

}
</script>
