<script>
    export default{
        name: "Home"
    }
</script>

<template>
  <div class="container-fluid bg-light vh-100 d-flex flex-column justify-content-center align-items-center text-center">
    <h1 class="display-4 text-primary mb-3">Smart Vehicle Parking System</h1>
    <p class="lead text-secondary mb-4">Efficient, secure, and real-time parking management for urban spaces.</p>
    <button @click="this.$router.push('/login')" class="btn btn-primary btn-lg">Get Started</button>

    <div class="row mt-5 w-75">
      <div class="col-md-4 mb-3">
        <div class="card h-100 shadow-sm">
          <div class="card-body">
            <h5 class="card-title">Real-Time Tracking</h5>
            <p class="card-text">Monitor parking availability and vehicle status instantly.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4 mb-3">
        <div class="card h-100 shadow-sm">
          <div class="card-body">
            <h5 class="card-title">Secure Access</h5>
            <p class="card-text">QR-based entry and exit with user authentication.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4 mb-3">
        <div class="card h-100 shadow-sm">
          <div class="card-body">
            <h5 class="card-title">Analytics Dashboard</h5>
            <p class="card-text">Track usage, revenue, and optimize parking zones.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
