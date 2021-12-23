<template>
<div :style="opacity">
<AdminHeader>
<div class="container p-0">
<div class="row">
<div class="col">
    <p class="lead">Welcome, admin</p>
</div>
</div>
</div>


</AdminHeader>
</div>
</template>

<style scoped>

</style>

<script>
// import axios from 'axios'
export default {
    data (){
        return{
        auth_check: false,
        token: '',
        alert: null,
        alertmodal: null,
        error: '',
        info: [],
        loader: false,
        loadermodal: false,
        classname: '',
        classnamemodal: null,
        submit: 'Submit',
        submittxt:'Submit',
        isDisabled: false,
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
        errormodal: null,
        record:false,
        norecord: '',
    }
    },

    created(){
    // this.tokenize()
    }, 

    methods:{
     
    },


    }
</script>