<template>
  <div v-if="token">
    <div class="container">
      <h2 style="text-align: center; margin-bottom: 20px; background-color: bisque;">Parking Lots</h2>
      <div class="row">
        <div style="margin: auto;">
            <p v-if="message" :style="{ color: messageColor }">{{ message }}</p>
        </div>
        <div class="col-md-4 mb-4" v-for="Lot in Lots" :key="Lot.id">
          <div class="card border-info mb-3" style="max-width: 18rem;">
            <div class="card-body">
              <h5 class="card-title">{{ Lot.Name }}</h5>
              <p>Lot's Price: Rs.{{ Lot.Price }}</p>
              <p>Address: {{ Lot.Address }}</p>
              <p>Pincode: {{ Lot.pin_code }}</p>
              <p>Max Spots: {{ Lot.max_spots }}</p>
              <p>Availability: {{ Lot.available }}</p>
              <router-link :to="`/admin/check_status/${Lot.id}`" style="margin-right: 10px;">Check status</router-link>
              <router-link :to="`/admin/editlot/${Lot.id}`" class="btn btn-primary" style="margin-right: 10px;">Edit</router-link>
              <button @click="deleteLot(Lot.id)" class="btn btn-danger">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <h1>Please log in first</h1>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Admindashboard",
  data() {
    return {
        token: "",
        Lots: [],
        message:"",
        messageColor:""
    };
  },
  methods: {
    loadAdmin() {
      this.token = localStorage.getItem("token");
    },
    async get_lots() {
      const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.token}`
      };
      try {
        const response = await axios.get("http://localhost:5000/api/ParkingLots", { headers });
        this.Lots = response.data.Lots;
        console.log(this.Lots);
      } catch (error) {
        console.log("Error loading lots:", error);
      }
    },
    async deleteLot(id) {
      const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.token}`
      };
      try {
        const response = await axios.delete(`http://localhost:5000/api/delete_lot/${id}`, { headers });
        console.log("Deleted:", response);
        await this.get_lots(); // Refresh list after deletion
        this.message = response.data.message;
        this.messageColor = "green";
      } catch (error) {
        console.log("Error deleting lot:", error);
        this.message = error.response.data.message;
        this.messageColor = "red";
      }
    }

  },
  mounted() {
    this.loadAdmin();
    this.get_lots();
  }
};
</script>