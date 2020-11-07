<template>
  <!-- <v-item-group multiple> -->
    <v-content>
    <thermo></thermo>
    <v-tabs grow>
      <v-tab active-class="active" to="lights">
        Lights
      </v-tab>
      <v-tab active-class="active" to="doors">
        Doors
      </v-tab>
      <v-tab active-class="active" to="windows">
        Windows
      </v-tab>
    </v-tabs>
    <v-tabs-items>
      <router-view></router-view>
    </v-tabs-items>
    </v-content>

  <!-- </v-item-group> -->
</template>

<script lang="ts">
import Vue from "vue";
import { ROOMS } from "../consts";
import ThermostatVue from "./Thermostat.vue";
export default Vue.extend({
  data: () => ({
    rooms: ROOMS,
  }),
  components: { thermo: ThermostatVue},
});
</script>
