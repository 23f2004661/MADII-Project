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
                    const r  = await axios.get("http://localhost:5000/api/user/summary",{headers: headers})
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
    <div v-if="token" class="mx-auto" style="width: 500px">
        <div class="container-lg justify-content-center">
            <div class="row">
                <img src="../assets/user_bar.png" alt="">
            </div>
        </div>
    </div>
    <div v-else>
        <h1>Please Log in First</h1>
    </div>
</template>
<style scoped>
    img { height: 500px; }
</style>
