<template>
  <v-main>
    <v-container fluid>
      <v-row>
        <v-banner>Room Control</v-banner>
        <v-col v-for="room in rooms" :key="room + ' ' + 'power'">
          <v-switch
            @change="firePowerEvent($event)"
            color="orange"
            :label="room"
          ></v-switch>
        </v-col>
      </v-row>
      <v-row>
        <v-banner>Door Control</v-banner>
        <v-col v-for="room in rooms" :key="room + ' ' + 'power'">
          <v-switch @change="firePowerEvent($event)" color="red" :label="room"></v-switch>
        </v-col>
      </v-row>
      <v-row>
        <v-banner>Light Control</v-banner>
        <v-col v-for="room in rooms" :key="room + ' ' + 'power'">
          <v-switch @change="firePowerEvent($event)" color="yellow" :label="room"></v-switch>
        </v-col>
      </v-row>
      <v-row>
        <v-banner>Water Control</v-banner>
        <v-col v-for="wat in water" :key="wat + ' ' + 'water'">
          <v-switch @change="fireWaterEvent($event)" color="teal darken-4" :label="wat"></v-switch>
        </v-col>
      </v-row>
      <v-row>
        <v-banner>Power Control</v-banner>
        <v-col cols="auto" v-for="pow in power" :key="pow + ' ' + 'power'">
          <v-switch @change="firePowerEvent($event)" color="amber darken-4" :label="pow"></v-switch>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script lang="ts">
import Vue from "vue";
import { ROOMS, POWER_DEVICES, WATER_DEVICES } from "../consts";
import  {Timer}  from 'easytimer.js';
import { mapMutations } from 'vuex';
export default Vue.extend({
  data: () => ({
    rooms: [] as string[],
    power: [] as string[],
    water: [] as string[],
  }),
  created() {
    this.resetPower();
    this.resetWater();
    this.rooms = ROOMS;
    this.power = POWER_DEVICES;
    this.water = WATER_DEVICES;
  },
  methods: {
    ...mapMutations(['addPower','addWater','resetPower','resetWater']),
    getTime(){
      console.log('Sending time');
      const sp = this.$timer.getTimeValues().toString().split(':');
      Number.parseInt(sp[2])<30?sp[2]='30':sp[2];
      this.addPower(Number.parseInt(sp[2]));
      
    },
    firePowerEvent(event: any){
      console.log(event);
      if(event===true){
        this.$timer.start()
      } 
      else{
        this.$timer.pause();
        this.getTime();
        this.$timer.stop();
      }
    },
    fireWaterEvent(event: any){
           if(event===true){
        this.$timer.start();
      } 
      else{
        this.$timer.pause()
        this.addWater(1);
        this.$timer.stop();
      }
    }
  },
});
</script>

<style></style>
