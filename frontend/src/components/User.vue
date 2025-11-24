<template>
    <div class="container-fluid">
        <div class="row justify-content-center">
            <div class="col-6 m-3">
                <h1>Users</h1>
                <table class="table table-success table-striped-columns">
                    <thead class="table-light">
                        <tr>
                            <th style="padding: 20px;">User Id</th>
                            <th style="padding: 20px;">User Name</th>
                            <th style="padding: 20px;">Full Name</th>
                            <th style="padding: 20px">Pincode</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="user in users" :key="user.id">
                            <td style="padding: 20px;">{{ user.id }}</td>
                            <td style="padding: 20px;">{{ user.username }}</td>
                            <td style="padding: 20px;">{{ user.fullname }}</td>
                            <td style="padding: 20px;">{{ user.pincode }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

</template>
<script>
    import axios from "axios";
    export default{
        name: "User",
        data(){
            return{
                users:[]
            }
        },
        created(){
            const headers={
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem("token")}`
            }
            const response = axios.get("http://localhost:5000/api/Users",{headers})
            response.then(res=>{
                console.log(res)
                for (let i=1;i<res.data.users.length;i++){
                    this.users.push(res.data.users[i])
                }
                console.log(this.users)
            })
        }
    }
</script>