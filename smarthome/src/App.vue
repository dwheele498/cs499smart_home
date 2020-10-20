<template>
  <v-app >
    <v-navigation-drawer
    floating
    right
    >
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </v-navigation-drawer>
  <thermostat></thermostat>
    <router-view/>
    
  </v-app>
</template>
<script lang="ts">
import Vue from 'vue';
import Thermostat from './views/Thermostat.vue';


export default Vue.extend({
  name: 'App',

  components: {
    Thermostat,
  },

  data: () => ({
    //
  }),
});
</script>
