<template>
  <v-card class="mx-auto my-12" max-width="400">
    <v-card-title>{{ date.toFormat("D") }}</v-card-title>
    <v-card-text class="text-center"
      ><h2>{{ temp }}&#8457;</h2></v-card-text
    ></v-card
  >
</template>

<script lang="ts">
import Vue from "vue";
import { weatherApi } from "../services/WeatherApi";
import { API_KEY, WEATHER_STATS } from "../consts";
import { DateTime } from "luxon";
export default Vue.extend({
  data: () => ({
    date: DateTime.local(),
    temp: 0,
  }),
  created() {
    this.initialize();
  },
  methods: {
    initialize(): void {
      weatherApi.getDay(
        this.date.toFormat("yyyy-LL-dd"),
        this.date.toFormat("yyyy-LL-dd")
      ).then((res: any) => {
        this.temp = Number.parseInt(
          (res.data.data[0].tavg * 1.8 + 32).toFixed(0)
        );
      });
    },
  },
});
</script>

<style></style>
