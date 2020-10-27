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
    timer: {} as Timer,
  }),
  created() {
    this.resetPower();
    this.resetWater();
    this.rooms = ROOMS;
    this.power = POWER_DEVICES;
    this.water = WATER_DEVICES;
    this.timer = new Timer();
  },
  methods: {
    ...mapMutations(['addPower','addWater','resetPower','resetWater']),
    timerStart() {
      this.timer.reset();
      this.timer.start();
      console.log('Timer start');
    },
    timerStop() {
      this.timer.pause();
    },
    getTime(){
      console.log('Sending time');
      const sp = this.timer.getTimeValues().toString().split(':');
      Number.parseInt(sp[2])<30?sp[2]='30':sp[2];
      this.addPower(Number.parseInt(sp[2]));
      
    },
    getWaterTime(){
      this.addWater(1);
    },
    firePowerEvent(event: any){
      console.log(event);
      if(event===true){
        this.timerStart();
      } 
      else{
        this.timerStop();
        this.getTime();
      }
    },
    fireWaterEvent(event: any){
           if(event===true){
        this.timerStart();
      } 
      else{
        this.timerStop();
        this.getWaterTime();
      }
    }
  },
});
</script>

<style></style>
