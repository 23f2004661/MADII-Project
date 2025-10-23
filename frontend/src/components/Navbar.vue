<script>
export default {
  name: "Navbar",
  data() {
    return {
      navlinks: {
        user: [
          { name: "Book", path: "/user/book" }
        ],
        admin: [
          { name: "Users", path: "/admin/users" }
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
      </ul>
    </div>
    <div v-else-if="role === 'admin'" class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li v-for="link in navlinks.admin" :key="link.path">
          <router-link :to="link.path">{{ link.name }}</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style></style>
