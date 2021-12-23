<template>
<div>
 <!-- 
<div class="modal fade" id="profile" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog ">
    <div class="modal-content">
<form @submit.prevent="formCheckStatus" class="needs-validation">
                    <input type="hidden" class="form-control d-none" v-model="token" required readonly>

      <div class="modal-header">
        <h5 class="modal-title sitecolor" id="staticBackdropLabel">Basic info</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
                   <div class="row">
                <div class="col-12 m-1 mt-0 mb-0">
                    <div v-bind:class="'alert '+ classnamemodal + ' p-2 text-center'">{{alertmodal}}</div>
                    </div>
            <div class="col-md-6">
                <div class="m-2">
                    <label for="surname">Surname</label>
                <div class="input-group">
                    <input type="text" class="form-control" v-model="surname" placeholder="surname" id="surname">
                </div>
                </div>
            </div>
                   <div class="col-md-6">
                <div class="m-2">
                    <label for="firstname">Firstname</label>
                <div class="input-group">
                    <input type="text" class="form-control" v-model="firstname" placeholder="Firstname" id="firstname">
                </div>
                </div>
            </div>
              <div class="col-md-6">
                <div class="m-2">
                    <label for="gender">Gender</label>
                <div class="input-group">
                   <select v-model="listStatus" class="form-control" id="gender" required>
                       <option disabled value="" selected>Select</option>
                       <option value="Male">Male</option>
                       <option value="Female">Female</option>
                   </select>
                </div>
                </div>
            </div>

              <div class="col-md-6">
                <div class="m-2">
                    <label for="age">Age</label>
                <div class="input-group">
                <input type="text" class="form-control" v-model="age" placeholder="age" id="age">
                </div>
                </div>
            </div>

             <div class="col-md-12">
                <div class="m-2">
                    <label for="email">Email</label>
                <div class="input-group">
                    <input type="text" class="form-control" v-model="surname" placeholder="Email" id="email">
                </div>
                </div>
            </div>
                   <div class="col-md-12">
                <div class="m-2">
                    <label for="phone">Phone</label>
                <div class="input-group">
                    <input type="text" class="form-control" v-model="phone" placeholder="Phone number" id="phone">
                </div>
                </div>
            </div>
                </div>
        
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" data-bs-target="#measurement" data-bs-toggle="modal" data-bs-dismiss="modal">{{next}}</button>
      </div>

</form>
    </div>
  </div>
</div>


<div class="modal fade" id="measurement" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
<form @submit.prevent="formCheckStatus" class="needs-validation">
                    <input type="hidden" class="form-control d-none" v-model="token" required readonly>

      <div class="modal-header">
        <h5 class="modal-title sitecolor" id="staticBackdropLabel">Measurement</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
                   <div class="row">
                <div class="col-12 m-1 mt-0 mb-0">
                    <div v-bind:class="'alert '+ classnamemodal + ' p-2 text-center'">{{alertmodal}}</div>
                    </div>
            <div class="col-md-6">
                <div class="m-2">
                    <label for="surname">Surname</label>
                <div class="input-group">
                    <input type="text" class="form-control" v-model="surname" placeholder="surname" id="surname">
                </div>
                </div>
            </div>
                   <div class="col-md-6">
                <div class="m-2">
                    <label for="firstname">Firstname</label>
                <div class="input-group">
                    <input type="text" class="form-control" v-model="firstname" placeholder="Firstname" id="firstname">
                </div>
                </div>
            </div>

                </div>
        
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-target="#profile" data-bs-toggle="modal" data-bs-dismiss="modal">Back</button>
        <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{submit}}</button>
      </div>

</form>
    </div>
  </div>
</div>

 -->
</div> 


</template>
<script>
export default{

    data(){
    return{
        next: 'Next',
        submit: 'submit',
        token: null,
        listStatus: '',
    }
        
    },
    
    }
</script>
