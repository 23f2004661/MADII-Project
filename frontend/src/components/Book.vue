<template>
  <div v-if="token && lot" class="userbook">
    <div class="form-box">
      <form class="form" @submit.prevent="bookSpot">
        <h1>Book a Spot</h1>
        <label>Location Name</label>
        <input type="text" :placeholder="lot.Name" disabled />
        <label>Price:</label>
        <input type="text" :placeholder="lot.Price" disabled />
        <label>Address:</label>
        <input type="text" :placeholder="lot.Address" disabled />
        <label>Pincode:</label>
        <input type="text" :placeholder="lot.pin_code" disabled />
        <label>Vehicle Number:</label>
        <input v-model="v_n" type="text" required />
        <button type="submit" class="btn btn-primary">Book</button>
      </form>
    </div>
  </div>
  <div v-else-if="!token">
    <h1 style="text-align: center; color: red;">Please Log in first</h1>
  </div>
  <div v-else>
    <h1 style="text-align: center; color: red;">Invalid lot data</h1>
  </div>
</template>
<script>
    import axios from 'axios';
    export default{
        name: "Book",
        props: ["id"],
        data(){
            return{
                token: "",
                lot: "",
                message: "",
                error: "",
                v_n:""
            }
        },
        methods:{
            loadUser(){
                this.token = localStorage.getItem("token")
            },
            async bookSpot() {
                const payload = {
                    v_n: this.v_n
                };
                const headers = {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.token}`
                };

                try {
                    const r = await axios.post(
                    `http://localhost:5000/api/book/${this.$route.params.id}`,
                    payload,
                    { headers }
                    );
                    this.message = r.data.message;
                    alert(this.message);
                } catch (err) {
                    // Axios wraps error responses in err.response
                    this.error = err.response?.data?.message || "Booking failed due to an unexpected error.";
                    alert(this.error);
                }
            }
        },
        created() {
            this.loadUser();
            this.lot = {
                Name: this.$route.query.name,
                Price: this.$route.query.price,
                Address: this.$route.query.address,
                pin_code: this.$route.query.pin
            };
        }
    }
</script>

<style scoped>
    .userbook{
        text-align: center;

    }
    .form{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
    }
    .form label, .form input{
        width: 300px;
        text-align: left;
    }
    .form-box{
        border: 2px solid black;
        width: 400px;
        margin: auto;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
    }
</style>