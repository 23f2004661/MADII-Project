<script>
    import axios from 'axios';
    export default{
        name:"Createlot",
        data(){
            return{
                token: "",
                prime_loc_name: "",
                price: "",
                address: "",
                pin_code: "",
                max_spots: "",
                message: "",
                messageColor: ""
            }
        },
        methods: {
            loadUser(){
                this.token=localStorage.getItem("token")
            },
            createLot(){
                const postData = {
                        prime_loc_name: this.prime_loc_name,
                        price: this.price,
                        address: this.address,
                        pin_code: this.pin_code,
                        max_spots: this.max_spots
                    };

                    const config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${this.token}`
                    }
                };
                axios.post("http://localhost:5000/api/createLot",postData,config)
                .then(res=> {
                    if (res.status==200){
                      console.log(res.data.message)
                      this.message=res.data.message
                      this.messageColor="green"
                    }
                })
                .catch(err=>{
                    if(err.status==409)
                    console.log(err)
                    this.message="Lot already exists"
                    this.messageColor="red"
                })
            }
        },
        mounted(){
            this.loadUser()
        }
    }
</script>

<template>
  <div v-if="token" class="container vh-100 d-flex justify-content-center align-items-center">
    <div class="card p-4 shadow-sm" style="width: 100%; max-width: 400px;">
      <h3 class="text-center mb-4">Create a Lot</h3>
      <p v-if="message" :style="{ color: messageColor }">{{ message }}</p>
      <form @submit.prevent="createLot">
        <div class="mb-3">
          <label for="username" class="form-label">Lot name</label>
          <input type="text" v-model="prime_loc_name" class="form-control" id="username" placeholder="Enter Lotname">
        </div>
        <div class="mb-3">
          <label for="price" class="form-label">Price</label>
          <input type="number" v-model="price" class="form-control"  placeholder="Rs. 30">
        </div>
        <div class="mb-3">
          <label for="address" class="form-label">Address</label>
          <input type="text" v-model="address" class="form-control"  placeholder="In the Vicinity">
        </div>
        <div class="mb-3">
          <label for="pincode" class="form-label">Pincode</label>
          <input type="number" v-model="pin_code" class="form-control"  placeholder="445566">
        </div>
        <div class="mb-3">
          <label for="max spots" class="form-label">Max spots</label>
          <input type="number" v-model="max_spots" class="form-control"  placeholder="20">
        </div>
        <button type="submit" class="btn btn-primary w-100">Create</button>
      </form>
    </div>
  </div>
  <div v-else>
        <h1>Please log in first</h1>
    </div>
</template>