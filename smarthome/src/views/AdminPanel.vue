<template>
  <v-main>
    <v-container fluid>
      <v-btn @click="save()">Save</v-btn>
      <v-expansion-panels accordion>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <v-banner
              ><v-icon class="material-icons">house</v-icon>Rooms</v-banner
            >
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-row class="justify-center">
              <v-col v-for="room in rooms" :key="room + ' ' + 'power'">
                <v-switch
                  @change="firePowerEvent($event)"
                  color="orange"
                  :label="room"
                ></v-switch>
              </v-col>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

      <v-expansion-panels accordion>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <v-banner
              ><v-icon class="material-icons">sensor_door</v-icon
              >Doors</v-banner
            >
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-row>
              <v-col v-for="door in doors" :key="door + ' ' + 'power'">
                <v-switch
                  @change="openCloseDoor(door)"
                  color="red"
                  :label="door"
                ></v-switch>
              </v-col>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

      <v-expansion-panels accordion>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <v-banner
              ><v-icon class="material-icons">wb_incandescent</v-icon
              >Lights</v-banner
            >
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-row>
              <v-col v-for="light in lights" :key="light + ' ' + 'power'">
                <v-switch
                  @change="lightSwitch(light)"
                  color="yellow"
                  :label="light"
                  :input-value="$store.state.lights[light]"
                ></v-switch>
              </v-col>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

      <v-expansion-panels accordion>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <v-banner
              ><v-icon class="material-icons">water_damage</v-icon
              >Water</v-banner
            ></v-expansion-panel-header
          >
          <v-expansion-panel-content>
            <v-row>
              <v-col v-for="wat in water" :key="wat + ' ' + 'water'">
                <v-switch
                  @change="fireWaterEvent($event, wat)"
                  color="teal darken-4"
                  :label="wat"
                  :input-value="$store.state.water[wat].on"
                ></v-switch>
              </v-col>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

      <v-expansion-panels accordion>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <v-banner><v-icon class="flash_on"></v-icon>Power</v-banner>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-row>
              <v-col
                cols="auto"
                v-for="pow in power"
                :key="pow + ' ' + 'power'"
              >
                <v-switch
                  @change="firePowerEvent($event, pow)"
                  color="amber darken-4"
                  :label="pow"
                  :input-value="$store.state.power[pow].on"
                ></v-switch>
              </v-col>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </v-main>
</template>

<script lang="ts">
import Vue from "vue";
import { ROOMS, POWER_DEVICES, WATER_DEVICES } from "../consts";
import { Timer } from "easytimer.js";
import {UpdateDbModel} from '../services/models/UpdateDbModel';
import { mapActions, mapGetters, mapMutations, mapState } from "vuex";
import { powerApi } from '@/services/PowerApi';

import store from '@/store';
import { waterApi } from '@/services/WaterApi';
export default Vue.extend({
  data: () => ({
    rooms: [] as string[],
    power: [] as string[],
    water: [] as string[],
    timer: new Timer(),
    doors: [] as string[],
    lights: [] as string[],
  }),
  created() {
    this.rooms = ROOMS;
    this.power = POWER_DEVICES;
    this.water = WATER_DEVICES;
    for (const [k, v] of Object.entries(this.$store.state.doors)) {
      this.doors.push(k);
    }
    for (const [k,v] of Object.entries(this.$store.state.lights)) {
      this.lights.push(k);
    }
  },
  methods: {
    ...mapMutations(["addPower", "addWater","powerSwitch","waterSwitch","openCloseDoor","onOffLight"]),
    getTime(): number {
      console.log("Sending time");
      const sp = this.timer
        .getTimeValues()
        .toString()
        .split(":");
      Number.parseInt(sp[2]) < 30 ? (sp[2] = "30") : sp[2];
      return Number.parseInt(sp[2]);
    },
    firePowerEvent(event: any, name: string) {
      console.log(name);
      if (event === true) {
        this.timer.start();
        this.powerSwitch(name);
      } else {
        this.powerSwitch(name);
        this.timer.pause();
        this.addPower([name, this.getTime()]);
        const pow = this.$store.state.power[name].amt;
        name = name.toLowerCase();
        switch(name){
          case "livingtv":
            powerApi.sendPower('livingtv',pow);
            break;
          case "exhaust":
            powerApi.sendPower('exhaust',pow);
            break;
          default:
            powerApi.sendPower(name,pow);
            break;
        }
        this.timer.stop();
      }
    },
    fireWaterEvent(event: any, name: string) {
      console.log(name);
      if (event === true) {
        this.timer.start();
        this.waterSwitch(name);
      } else {
        this.timer.pause();
        this.waterSwitch(name);
        this.addWater([name, this.getTime()]);
        const wat = this.$store.state.water[name].amt;
        name = name.toLowerCase();
        waterApi.sendWater(name,wat);
        this.timer.stop();
      }
    },
    lightSwitch(name: string){
      console.log(name);
      this.onOffLight(name);
    },
    async save(){
      const powerHold = []
      const waterHold = []
      Object.entries(this.$store.state.power).forEach((k)=>{
        powerHold.push([k[0].toLowerCase(),k[1].amt]);
        // console.log(v);
      })
      Object.entries(this.$store.state.water).forEach((k)=>{
        waterHold.push([k[0].toLowerCase(),k[1].amt]);
      })


      await powerApi.sendPower(powerHold).then(()=>{
        waterApi.sendWater(waterHold).then(()=>{
          this.submit=true;
          this.snackMessage="Successfully Saved Data";
          })
      })
    }
  },
});
</script>

<style></style>
