<template>
    <div v-if="token">
        <h1>This is User Dashboard</h1>
        <router-view />
    </div>
    <div v-else>
        <h1>Please log in first</h1>
    </div>
</template>

<script>
    export default{
        name: "Userdashboard",
        data(){
            return{
                token: ""
            }
        },
        methods: {
            loadUser(){
                this.token=localStorage.getItem("token")
            }
        },
        mounted(){
            this.loadUser()
        }
    }
</script>