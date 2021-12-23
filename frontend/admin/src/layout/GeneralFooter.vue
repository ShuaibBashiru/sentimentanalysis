<template>
    <div>


<div class="container-fluid border-top p-0 pb-1 pt-1 pb-md-2 mt-2 pt-md-2 bg-dark text-white position-absolute bottom-0">
<div class="row p-0 m-0">
<div class="col-md-6 p-3 pt-2 pb-2">
    <small>&copy; {{settings.copyright}}</small>
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
            "settings":appsettings.settings,
            "appinfo":appsettings.appinfo,
            errorStr: null,
            location: null

        }
    },
    methods:{

    },

 

}
</script>