<script>
export default {
  name: "Navbar",
  data() {
    return {
      navlinks: {
        user: [
          { name: "Home", path: "/user" },
          {name: "History", path: "/user/history"},
          {name: "Summary", path: "/user/summary"}
        ],
        admin: [
          { name: "Home", path: "/admin" },
          { name: "Users", path: "/admin/users" },
          { name: "Create", path: "/admin/createlot" },
          { name: "Summary", path: "/admin/summary"}
        ]
      },
      role: ""
    };
  },
  methods: {
    loadUser() {
      this.role = localStorage.getItem("role");
      // Optional: log for debugging
      console.log("Navbar role:", this.role);
    },
    logoutUser(){
      console.log("logging out ...")
      localStorage.removeItem("token")
      localStorage.removeItem("role")
      this.$router.push("/login")
    }
  },
  mounted() {
    this.loadUser();
  }
};
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Parkspree</a>
    <div v-if="role === 'user'" class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li v-for="link in navlinks.user" :key="link.path">
          <router-link :to="link.path">{{ link.name }}</router-link>
        </li>
        <li class="logout"><button @click="logoutUser">Logout</button></li>
      </ul>
    </div>
    <div v-else-if="role === 'admin'" class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li v-for="link in navlinks.admin" :key="link.path">
          <router-link :to="link.path">{{ link.name }}</router-link>
        </li>
        <li class="logout"><button @click="logoutUser">Logout</button></li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
ul {
  display: flex;
  align-items: center;
}

nav ul li:not(:last-child) {
    margin-right: 15px; /* For horizontal spacing */
}
.logout {
  margin-left: auto; /* Pushes logout to the far right */
}

</style>
