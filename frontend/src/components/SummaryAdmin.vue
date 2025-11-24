<script>
    import axios from 'axios';
    export default{
        name: "SummaryUser",
        data(){
            return{
                token:""
            }
        },
        methods:{
            fetchUser(){
                try{
                    this.token = localStorage.getItem("token")
                }catch(error){
                    console.log(this.error)
                }
            },
            async fetchSummary(){
                try{
                    const headers = {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${this.token}`
                    }
                    const r  = await axios.get("http://localhost:5000/api/admin/summary",{headers: headers})
                    console.log(r.data)
                }catch(error){
                    console.log(error.toJSON())
                }
            }
        },
        mounted(){
            this.fetchUser();
            this.fetchSummary();
        }
    }
</script>
<template>
    <div v-if="token">
        <div class="container-lg">
            <div class="row">
                <div class="col-6 d-flex justify-content-center align-items-center">
                    <img src="../assets/bar.png" alt="img-fluid">
                </div>
                <div class="col-6 d-flex justify-content-center align-items-center"><img src="../assets/pie.png" alt="img-fluid"></div>
            </div>
        </div>
    </div>
    <div v-else>
        <h1>Please Log in First</h1>
    </div>
</template>

