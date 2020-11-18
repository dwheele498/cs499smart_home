<template>
  <v-main>
    <v-container fluid>
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
                  @change="firePowerEvent($event)"
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
                  @change="firePowerEvent($event)"
                  color="yellow"
                  :label="light"
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
                  @change="firePowerEvent($event)"
                  color="amber darken-4"
                  :label="pow"
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
import { mapMutations, mapState } from "vuex";
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
    for (const k of Object.entries(this.$store.state.lights)) {
      this.lights.push(k);
    }
  },
  methods: {
    ...mapMutations(["addPower", "addWater"]),
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
      console.log(event);
      if (event === true) {
        this.timer.start();
      } else {
        this.timer.pause();
        this.addPower([name, this.getTime()]);
        this.timer.stop();
      }
    },
    fireWaterEvent(event: any, name: string) {
      console.log(name);
      if (event === true) {
        this.timer.start();
      } else {
        this.timer.pause();
        this.addWater([name, this.getTime()]);
        this.timer.stop();
      }
    },
  },
});
</script>

<style></style>
