<template>
    <v-container fill-height align-center>
      <v-flex min-width="600px">
        <img src="../../assets/homeicons/FloorPlanDoor.svg"
        width="600px"
        max-width="100%"
        @click="doorSwitch($event)"
        />

      </v-flex>
      <v-row>
        <v-col v-for=" k of Object.keys(doors)" :key="k" cols="12" md="2">
          <v-banner class="flex-grow-1 text-left"
          height="60"
          >{{ k }}</v-banner>
          <v-item>
            <v-card
              :color="doors[k].on ? 'white' : 'black'"
              class="d-flex align-center"
              height="200"
              @click="openCloseDoor([k,15])"
            >
                <div
                  v-if="doors[k].on"
                  class="display-3 flex-grow-1 text-center black--text"
                >
                  On
                </div>
                <div
                  v-else
                  class="display-3 flex-grow-1 text-center white--text"
                >
                  Off
                </div>
            </v-card>
          </v-item>
        </v-col>
</v-row>

</template>

<script lang="ts">
import Vue from 'vue'
import { mapMutations, mapState } from 'vuex';
import {ROOMS} from '../../consts';
import {Timer} from "easytimer.js";
export default Vue.extend({
      data: () => ({
        rooms: ROOMS,
        timer: new Timer(),
  }),
  computed: {
    ...mapState(["doors"]),
  },
  methods: {
    ...mapMutations(["openCloseDoor"]),
    doorSwitch(event: MouseEvent) {
      console.log("x:" + " " + event.layerX);
      console.log("y:" + " " + event.layerY);
      if (
        event.layerX >= 509 &&
        event.layerX < 540 &&
        event.layerY <= 157 &&
        event.layerY > 118
      ) {
        this.openCloseDoor("Master Bedroom Door");
      } else if (
        event.layerX >= 374 &&
        event.layerX < 420 &&
        event.layerY >= 135 &&
        event.layerY < 158
      ) {
        this.openCloseDoor("Bathroom Door 2");
      } else if (
        event.layerX >= 427 &&
        event.layerX < 450 &&
        event.layerY >= 36 && event.layerY < 72
      ) {
        this.openCloseDoor("Bathroom Door 1");
      } else if (
        event.layerX >= 420 &&
        event.layerX < 476 &&
        event.layerY <= 217 &&
        event.layerY > 190
      ) {
        this.openCloseDoor("Kid's Bedroom 1 Door");
      } else if (
        event.layerX >= 515 &&
        event.layerX < 590 &&
        event.layerY <= 300 &&
        event.layerY > 199
      ) {
        this.openCloseDoor("Kid's Bedroom 2 Door");
      } else if (
        event.layerX >= 234 &&
        event.layerX < 362 &&
        event.layerY <= 307 &&
        event.layerY > 169
      ) {
        this.openCloseDoor("Front Door");
      } else if (
        event.layerX >= 204 &&
        event.layerX < 362 &&
        event.layerY <= 80 &&
        event.layerY > 12
      ) {
        this.openCloseDoor("Back Door");
      } else if (
        event.layerX >= 10 &&
        event.layerX < 97 &&
        event.layerY <= 304 &&
        event.layerY > 215
      ) {
        this.openCloseDoor("Garage Door 1");
      } else if (
        event.layerX >= 98 &&
        event.layerX < 215 &&
        event.layerY <= 304 &&
        event.layerY > 215
      ) {
        this.openCloseDoor("Garage Door 2");
      } else if (
        event.layerX >= 151 &&
        event.layerX < 257 &&
        event.layerY <= 160 &&
        event.layerY > 81
      ) {
        this.openCloseDoor("House to Garage Door");
      }
    },
  },
});
</script>

<style></style>