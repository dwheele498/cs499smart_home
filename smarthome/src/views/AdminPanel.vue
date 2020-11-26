<template>
  <v-main>
    <v-container fluid>
      <v-expansion-panels accordion>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <v-banner>Manual Controls</v-banner>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-row class="justify-center">
              <v-col>
                <v-radio-group label="Minutes">
                  <v-radio
                    @change="radioPick(5)"
                    color="success"
                    label="5"
                    value="120"
                  >
                  </v-radio>
                  <v-radio
                    @change="radioPick(10)"
                    color="success"
                    label="10"
                    value="240"
                  >
                  </v-radio>
                  <v-radio
                    @change="radioPick(15)"
                    color="success"
                    label="15"
                    value="360"
                  >
                  </v-radio>
                </v-radio-group>
              </v-col>
              <v-col>
                <v-select :items="power" v-model="appliance" clearable label="Appliance Name"></v-select>
                <v-btn @click="manualSubmit()" color="success" rounded>Submit</v-btn>
              </v-col>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

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
    <v-snackbar v-model="submit">Successfully Submitted Manual Operation <template v-slot:action="{ attrs }">
        <v-btn
          color="green"
          text
          v-bind="attrs"
          @click="submit = false"
        >
          Close
        </v-btn>
      </template></v-snackbar>
  </v-main>
</template>

<script lang="ts">
import Vue from "vue";
import { ROOMS, POWER_DEVICES, WATER_DEVICES } from "../consts";
import { Timer } from "easytimer.js";
import { mapActions, mapGetters, mapMutations, mapState } from "vuex";
import { powerApi } from "@/services/PowerApi";
import store from "@/store";
import { waterApi } from "@/services/WaterApi";
export default Vue.extend({
  data: () => ({
    rooms: [] as string[],
    power: [] as string[],
    water: [] as string[],
    timer: new Timer(),
    doors: [] as string[],
    lights: [] as string[],
    radio: 0,
    appliance: "",
    submit: false,
  }),
  created() {
    this.rooms = ROOMS;
    this.power = POWER_DEVICES;
    console.log(this.power);
    this.water = WATER_DEVICES;
    for (const [k, v] of Object.entries(this.$store.state.doors)) {
      this.doors.push(k);
    }
    for (const [k, v] of Object.entries(this.$store.state.lights)) {
      this.lights.push(k);
    }
  },
  methods: {
    ...mapMutations([
      "addPower",
      "addWater",
      "powerSwitch",
      "waterSwitch",
      "openCloseDoor",
      "onOffLight",
    ]),
    radioPick(event: any) {
      console.log(event);
      this.radio = Number.parseInt(event) * 60;
    },
    manualSubmit(){
      this.addPower([this.appliance,this.radio]);
      this.submit = true;
      this.appliance = '';


    },
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
        switch (name) {
          case "livetv":
            powerApi.sendPower("livingtv", pow);
            break;
          case "bathexhaust":
            powerApi.sendPower("exhaust", pow);
            break;
          default:
            powerApi.sendPower(name, pow);
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
        waterApi.sendWater(name, wat);
        this.timer.stop();
      }
    },
    lightSwitch(name: string) {
      console.log(name);
      this.onOffLight(name);
    },
  },
});
</script>

<style></style>
