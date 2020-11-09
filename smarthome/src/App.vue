<template>
  <v-app dark>
    <v-btn
      @click="openMenu = !openMenu"
      retain-focus-on-click="true"
      :disabled="openMenu"
      v-if="!openMenu"
      >Menu</v-btn
    >
    <v-btn v-else class="mb-auto">
      <router-link class="navbar-item" exact-active-class="is-active" to="/"
        >Home</router-link
      >
      <router-link class="navbar-item" active-class="is-active" to="/data"
        >Data</router-link
      >
       <router-link class="navbar-item" active-class="is-active" to="/admin"
        >Admin</router-link
      >
      <router-link class="navbar-item" active-class="is-active" to="/predictions"
        >Forecast</router-link
      >
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on">
            Options
          </v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>
                <a @click="openMenu = !openMenu">Close Menu</a>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item v-if="!$vuetify.theme.dark">
            <v-list-item-content>
              <v-list-item-title>
                <a @click="$vuetify.theme.dark = !$vuetify.theme.dark">Dark Mode</a>
                >
              </v-list-item-title>
              <v-list-item-subtitle>
                
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item v-else>
            <v-list-item-content>
              <v-list-item-title>
                <a @click="$vuetify.theme.dark = !$vuetify.theme.dark">Light Mode</a>
                >
              </v-list-item-title>
              <v-list-item-subtitle>
                
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-menu>
      ></v-btn
    >
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
    openMenu: false,
  }),
  created() {
    this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
  },
});
</script>

<style>
.v-baner {
  border-style: none;
}
</style>
