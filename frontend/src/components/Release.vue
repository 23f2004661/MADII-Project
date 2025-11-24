<script>
    import axios from 'axios'
    export default{
        name: "Release",
        data(){
            return {
                token: "",
                details:{
                    lot_name: "",
                    parking_time: "",
                    leaving_time: "",
                    vehicle_number: "",
                    parking_cost: 0
                }
            }   
        },
        methods: {
            getToken(){
                try{
                    this.token=localStorage.getItem("token")
                } catch (error){
                    console.log(error)
                }
            },
            async fetchData(){
                try{
                    const headers={
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${this.token}`
                    }
                    const response = await axios.get("http://localhost:5000/api/user/release",{headers: headers})
                    console.log(response.data)
                    this.details = response.data

                } catch (error){
                    console.log(error.toJSON())
                }
            },
            async release(){
                const headers={
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${this.token}`
                }
                axios.post("http://localhost:5000/api/user/release", {},{headers: headers})
                .then(r => {
                    console.log(r.data)
                    alert("spot released successfully")
                    this.$router.push('/user')  
                })
                .catch(error => {console.log(error.toJSON())})   
            },
        },
        mounted(){
            this.getToken();
            this.fetchData();
        }
    }
</script>
<template>
    <div v-if="token" class="container-lg justify-content-center ">
        <div class="row">
            <div class="col mx-2">
                <h1 class="bg-primary fs-4 fw-light my-3">Thank you for availing our services</h1>
                <form @submit.prevent="release">
                    <div class="mx-auto d-flex flex-column" style="width: 400px;">
                        <label for="LotName">Lot Name </label>
                        <input type="text" :placeholder="details.lot_name" disabled />
                    </div>
                    <div class="mx-auto d-flex flex-column" style="width: 400px;">
                        <label for="ParkingTime">Parking Time </label>
                        <input type="text" :placeholder="details.parking_time"  disabled />
                    </div>
                    <div class="mx-auto d-flex flex-column" style="width: 400px;">
                        <label for="LeavingTime">Leaving Time </label>
                        <input type="text" name="" id="" :placeholder="details.leaving_time" disabled />
                    </div>
                    <div class="mx-auto d-flex flex-column" style="width: 400px;">
                        <label for="VehicleNumber">Vehicle Number </label>
                        <input type="text" name="" id="" :placeholder="details.vehicle_number" disabled />
                    </div>
                    <div class="mx-auto d-flex flex-column" style="width: 400px;">
                        <label for="Cost">Parking Cost </label>
                        <input type="number" name="" id="" :placeholder="details.parking_cost" disabled />
                    </div>
                    <div class="mx-auto d-flex flex-column my-2" style="width: 200px;">
                        <button type="submit" class="btn btn-outline-primary text-start">Pay</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <div v-else>
        <h1>Please Log in First</h1>
    </div>
</template>
<style></style>