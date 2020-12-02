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
              :color="doors[k].on ? 'grey' : 'black'"
              class="d-flex align-center"
              width="200"
              @click="doorsSwitch(k)"
            >
            <div v-if="doors[k].on == true" class="display-3 flex-grow-1 text-center white--text">
              <img src="../../assets/homeicons/DoorOpen.svg" />
            </div>
            <div v-else class="display-3 flex-grow-1 text-center white--text">
              <img src="../../assets/homeicons/DoorClosed.svg" />
            </div>
          </v-card>
        </v-item>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { mapMutations, mapState } from "vuex";
import { ROOMS } from "../../consts";
export default Vue.extend({
  data: () => ({
    rooms: ROOMS,
  }),
  computed: {
    ...mapState(["doors"]),
  },
  methods: {
    ...mapMutations(["doorsSwitch"]),
    doorSwitch(event: MouseEvent) {
      console.log("x:" + " " + event.layerX);
      console.log("y:" + " " + event.layerY);
      if (
        event.layerX >= 509 &&
        event.layerX < 540 &&
        event.layerY <= 157 &&
        event.layerY > 118
      ) {
        this.doorsSwitch("Master Bedroom Door");
      } else if (
        event.layerX >= 374 &&
        event.layerX < 420 &&
        event.layerY >= 135 &&
        event.layerY < 158
      ) {
        this.doorsSwitch("Bathroom Door 2");
      } else if (
        event.layerX >= 427 &&
        event.layerX < 450 &&
        event.layerY >= 36 && event.layerY < 72
      ) {
        this.doorsSwitch("Bathroom Door 1");
      } else if (
        event.layerX >= 420 &&
        event.layerX < 476 &&
        event.layerY <= 217 &&
        event.layerY > 190
      ) {
        this.doorsSwitch("Kid's Bedroom 1 Door");
      } else if (
        event.layerX >= 515 &&
        event.layerX < 590 &&
        event.layerY <= 300 &&
        event.layerY > 199
      ) {
        this.doorsSwitch("Kid's Bedroom 2 Door");
      } else if (
        event.layerX >= 234 &&
        event.layerX < 362 &&
        event.layerY <= 307 &&
        event.layerY > 169
      ) {
        this.doorsSwitch("Front Door");
      } else if (
        event.layerX >= 204 &&
        event.layerX < 362 &&
        event.layerY <= 80 &&
        event.layerY > 12
      ) {
        this.doorsSwitch("Back Door");
      } else if (
        event.layerX >= 10 &&
        event.layerX < 97 &&
        event.layerY <= 304 &&
        event.layerY > 215
      ) {
        this.doorsSwitch("Garage Door 1");
      } else if (
        event.layerX >= 98 &&
        event.layerX < 215 &&
        event.layerY <= 304 &&
        event.layerY > 215
      ) {
        this.doorsSwitch("Garage Door 2");
      } else if (
        event.layerX >= 151 &&
        event.layerX < 257 &&
        event.layerY <= 160 &&
        event.layerY > 81
      ) {
        this.doorsSwitch("House to Garage Door");
      }
    },
  },
});
</script>

<style></style>
