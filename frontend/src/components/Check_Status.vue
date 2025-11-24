<script>
    import axios from 'axios';
    export default {
        name: "CheckStatus",
        data(){
            return {
                token: "",
                reserver_spots: [],
                details:{
                    "id": "",
                    "username": "",
                    "lot_name": "",
                    "spot_number": 0,
                    "vehicle_number": "",
                    "parking_time_stamp": ""
                }
            }
        },
        methods: {
            loadToken() {
                this.token = localStorage.getItem("token");
            },
            async getStatus(){
                const headers={
                    'Content-Type':'application/json',
                    "Authorization": `Bearer ${this.token}`
                }
                this.id=this.$route.params.id
                const response = await axios.get(`http://localhost:5000/api/check_status/${this.id}`,{headers: headers})
                console.log(response)
                this.details=response.data.details
            }
        },
        mounted() {
            this.loadToken();
            this.getStatus();
        }
    };
</script>

<template>
    <div v-if="token" id="main" class="container-lg justify-content-center">
        <div class="row">
            <div class="col"><h2 class="bg-primary text-center">Lot Status</h2></div>
        </div>
        <div class="row">
            <div class="col">
                <table class="table table-hover">
                    <thead class="table-light">
                        <tr>
                            <th class="col-2">id</th>
                            <th class="col-2">User Name</th>
                            <th class="col-2">Lot Name</th>
                            <th class="col-2">Spot Number</th>
                            <th class="col-2">Vehicle Number</th>
                            <th class="col-2">Parking Time</th>
                        </tr>
                    </thead>   
                    <tbody>
                        <tr v-for="detail in details" :key="detail">
                            <td>{{detail.id}}</td>
                            <td>{{detail.username}}</td>
                            <td>{{detail.lot_name}}</td>
                            <td>{{detail.spot_number}}</td>
                            <td>{{detail.vehicle_number}}</td>
                            <td>{{detail.parking_time_stamp}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <div v-else>
        <h1>Please log in first</h1>
    </div>
</template>

<style scoped></style>