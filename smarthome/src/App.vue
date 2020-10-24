<template>
  <v-app>
    <div
      class="navbar horizontal end "
      role="navigation"
      :class="{ 'is-dark': $vuetify.theme.dark }"
    >
        <router-link class="navbar-item center" to="/">Home</router-link>
        <router-link class="navbar-item" to="/about">Data</router-link>

      <div class="navbar-end">
        <p class="navbar-item">Dark Mode</p>
        <v-switch
          class="navbar-item "
          :value="true"
          ref="switch"
          v-model="$vuetify.theme.dark"
        ></v-switch>
      </div>
    </div>

    <router-view />
  </v-app>
</template>
<script lang="ts">
import Vue from "vue";
import Thermostat from "./views/Thermostat.vue";

export default Vue.extend({
  name: "App",

  components: {},

  data: () => ({
    //
  }),
  created() {
    this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
  },
});
</script>

<style scoped>
</style>
