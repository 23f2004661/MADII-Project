<template>
    <div v-if="token">
        <div class="container">
            <h2 class="bg-primary text-center">Parking Lots</h2>
            <div class="row">
                    <div class="col-md-4 mb-4" v-for="Lot in lots" :key="Lot.id">
                        <div class="card text-bg-light mb-3 m-2">
                            <div class="card-body">
                                <h5 class="card-title">{{Lot.Name}}</h5>
                                <p>Lot's Price: Rs.{{Lot.Price}}</p>
                                <p>Address: {{Lot.Address}}</p>
                                <p>Pincode: {{Lot.pin_code}}</p>
                                <p>Availability {{ Lot.available}}</p>
                                <router-link :to="{
                                    name: 'Book',
                                    params: { id: Lot.id },
                                    query: {
                                        name: Lot.Name,
                                        price: Lot.Price,
                                        address: Lot.Address,
                                        pin: Lot.pin_code
                                    }
                                }">Book</router-link>
                            </div>
                        </div>
                    </div>
            </div>
        </div>
    </div>
    <div v-else>
        <h1 style="text-align: center; color: red;">Please log in first</h1>
    </div>
</template>

<script>
    import axios from 'axios';
    export default{
        name: "Userdashboard",
        data(){
            return{
                token: "",
                lots: []
            }
        },
        methods: {
            loadUser(){
                this.token=localStorage.getItem("token")
            },
            async fetchMallData(){
                const headers={
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.token}`
                }
                const r = await axios.get("http://localhost:5000/api/mallData", {headers})
                console.log(r)
                this.lots=r.data.Lots
                console.log(this.lots)
            }
        },
        mounted(){
            this.loadUser(),
            this.fetchMallData()
        }
    }
</script>