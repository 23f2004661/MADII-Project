<template>
    <div v-if="token">
        <h1>This is Admin Dashboard</h1>
        <router-view />
    </div>
    <div v-else>
        <h1>Please log in first</h1>
    </div>
</template>

<script>
    export default{
        name: "Admindashboard",
        data(){
            return {
                token: ""
            }
        },
        methods:{
            loadAdmin(){
                this.token=localStorage.getItem("token")
            }
        },
        mounted(){
            this.loadAdmin()
        }
    }
</script>