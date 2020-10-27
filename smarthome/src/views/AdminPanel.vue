<template>
  <v-main>
    <v-container fluid>
      <v-row>
        <v-banner>Room Control</v-banner>
        <v-col v-for="room in rooms" :key="room">
          <v-switch color="orange" :label="room"></v-switch>
        </v-col>
      </v-row>
      <v-row>
        <v-banner>Door Control</v-banner>
        <v-col v-for="room in rooms" :key="room + ' ' + door">
          <v-switch color="red" :label="room"></v-switch>
        </v-col>
      </v-row>
      <v-row>
        <v-banner>Light Control</v-banner>
        <v-col v-for="room in rooms" :key="room + ' ' + door">
          <v-switch color="yellow" :label="room"></v-switch>
        </v-col>
      </v-row>
      <v-row>
        <v-banner>Water Control</v-banner>
        <v-col v-for="wat in water" :key="wat">
          <v-switch color="teal darken-4" :label="wat"></v-switch>
        </v-col>
      </v-row>
      <v-row>
        <v-banner>Power Control</v-banner>
        <v-col cols="auto"  v-for="pow in power" :key="pow">
          <v-switch color="amber darken-4" :label="pow"></v-switch>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script lang="ts">
import Vue from "vue";
import { ROOMS, POWER_DEVICES, WATER_DEVICES } from "../consts";
export default Vue.extend({
  data: () => ({
    rooms: [] as string[],
    power: [] as string[],
    water: [] as string[] 
  }),
  created() {
    this.rooms = ROOMS;
    this.power = POWER_DEVICES;
    this.water = WATER_DEVICES;

  },
});
</script>

<style></style>


1 blahblahflsdsldhdkjfhf;ksdhf 2019 sjkfhsdlkfhdfn 
