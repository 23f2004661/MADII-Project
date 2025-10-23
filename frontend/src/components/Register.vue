<script>
import axios from 'axios'
 export default{
    name: "Register",
    data() {
      return {
          username: '',
          password: '',
          fullname: '',
          pincode: ''
      };
    },
    methods: {
      registerUser(){
        const headers = {
          "Content-Type": "application/json"
        };
        const body = {
          username: this.username,
          password: this.password,
          fullname: this.fullname,
          pincode: this.pincode
        };
        axios.post("http://localhost:5000/register", body, { headers })
          .then(response => {
            console.log(response.data);
            if (response.status == 200){
                alert("registerd successfully")
                this.$router.push("/login")
            }
          })
          .catch(error => {
            console.error(error.response?.data || error.message);
          });
       }
    }
 }
</script>


<template>
  <div class="container vh-100 d-flex justify-content-center align-items-center">
    <div class="card p-4 shadow-sm" style="width: 100%; max-width: 400px;">
      <h3 class="text-center mb-4">Register</h3>
      <form @submit.prevent="registerUser">
        <div class="mb-3">
          <label for="fullname" class="form-label">Full Name</label>
          <input type="text" v-model="fullname" class="form-control" id="fullname" placeholder="Enter full name">
        </div>
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input type="text" v-model="username" class="form-control" id="username" placeholder="Enter username">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input type="password" v-model="password" class="form-control" id="password" placeholder="Enter password">
        </div>
        <div class="mb-3">
          <label for="pincode" class="form-label">Pincode</label>
          <input type="text" v-model="pincode" class="form-control" id="pincode" placeholder="Enter pincode">
        </div>
        <button type="submit" class="btn btn-success w-100">Register</button>
      </form>
    </div>
  </div>
</template>


<style></style>