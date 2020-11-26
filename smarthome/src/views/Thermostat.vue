<template>
  <v-card
    v-if="callCompleted"
    raised
    class="mx-auto my-10"
    max-width="200"
    height="6rem"
  >
    <h2 class="cyan--text text-center">{{ date.toFormat("D") }}</h2>
    <h2 class="mx-auto px-auto lime--text text-center">
      Avg: {{ temp }}&#8457;
    </h2>
    <h2 class="mx-auto px-auto lime--text text-center">
      HVAC:
      <v-btn @click.stop="decrementHvac" elevation="2" x-small> -1 </v-btn>
      {{ getThermo }}
      <v-btn @click.stop="incrementHvac" elevation="2" x-small> +1 </v-btn>
    </h2>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import { weatherApi } from "../services/WeatherApi";
import { API_KEY, WEATHER_STATS } from "../consts";
import { DateTime } from "luxon";
import { HourlyWeatherModel } from "../services/models";
import { mapMutations, mapState } from "vuex";
export default Vue.extend({
  data: () => ({
    ...mapState([
    'thermo'
    ]),
    date: DateTime.local(),
    temp: 0,
    hvac: {
      temp: 0,
      on: false,
    },
    callCompleted: false,
  }),
  created() {
    this.initialize();
    this.hvac.temp = this.$store.state.thermo
    this.hvac.on = this.$store.state.power.Hvac.on;
  },
  computed:{
    getThermo(){
      return this.$store.state.thermo;
    }
  },
  watch:{
    getThermo(newTemp,oldTemp){
      console.log(newTemp)
    }
  },

  methods: {
    ...mapMutations(["addPower","setThermo"]),
    async initialize(): Promise<void> {
      await weatherApi
        .getDay(
          this.date.toFormat("yyyy-LL-dd"),
          this.date.toFormat("yyyy-LL-dd")
        )
        .then((res: any) => {
          this.temp = Number.parseInt(
            (res.data.data[0].temp * 1.8 + 32).toFixed(0)
          );
          this.callCompleted = true;
        })
        .catch((err: any) => {
          console.log(err);
          (this.temp = -1), (this.callCompleted = true);
        });
    },
    async incrementHvac(): Promise<void> {
      this.addPower(["Hvac", 1]);
      this.setThermo(1);
    },
    async decrementHvac(): Promise<void> {
      this.addPower(["Hvac", 1]);
      this.setThermo(-1);
    },
  },
});
</script>

<style></style>
