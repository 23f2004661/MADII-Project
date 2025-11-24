<script>
    import axios from 'axios';
    export default{
        name:"Editlot",
        data(){
            return{
                token:"",
                price: 0,
                address: "",
                max_spots: 0,
                pin_code: 0,
                id: "",
                message: "",
                messageColor: ""
            }
        },
        methods: {
            getUser(){
                this.token=localStorage.getItem("token")
            },
            async editLot(){
                const headers = {
                    "content-type": "application/json",
                    "Authorization": `Bearer ${this.token}`
                }
                const payload = {
                    price: this.price,
                    address: this.address,
                    pin_code: this.pin_code,
                    max_spots: this.max_spots
                }
                try{
                    const response= await axios.post(`http://localhost:5000/api/edit_lot/${this.id}`,payload,{headers: headers})
                    if (response.status==200){
                        console.log(response)
                        this.message=response.data.message
                        this.messageColor="green"
                    }
                    else{
                        this.message=response.data.message
                        this.messageColor="red"
                    }
                }catch(error){
                    console.log(error)
                    this.message=error.response.data.message
                    this.messageColor="red"
            }

            }
        },
        mounted(){
            this.id= this.$route.params.id
            this.getUser()
        }
        
    }
</script>

<template>
  <div v-if="token" class="container-fluid">
    <div class="row justify-content-center">
        <div class="col-3 m-3">
            <h1>Edit This Lot</h1>
            
            <form @submit.prevent="editLot">
                <p v-if="message" class="message-block">{{ message }}</p>
                <div class="form-group">
                    <label for="formGroupExampleInput2">price</label>
                    <input v-model="price" type="number" class="form-control" id="formGroupExampleInput2">
                </div>
                <div class="form-group">
                    <label for="formGroupExampleInput2">Address</label>
                    <input v-model="address" type="text" class="form-control" id="formGroupExampleInput2">
                </div>
                <div class="form-group">
                    <label for="formGroupExampleInput2">Pincode</label>
                    <input v-model="pin_code" type="number" class="form-control" id="formGroupExampleInput2">
                </div>
                <div class="form-group">
                    <label for="formGroupExampleInput2">Max spots</label>
                    <input v-model="max_spots" type="number" class="form-control" id="formGroupExampleInput2">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
    </div>
    <div v-else>
        <h1>Please log in first</h1>
    </div>
</template>

<style scoped>
    .message-block{
        color: v-bind(messageColor);
        width: 300px;
        border: 2px solid black;
        padding: 20px;
        margin: 20px;
    }
</style>