<template>
  <v-card v-if="callCompleted" raised class="mx-auto my-10" max-width="200" height="6rem">
    <h2 class="text-center">{{ date.toFormat("D") }}</h2>
      <h2 class="mx-auto px-auto lime-text text-center">
        Avg: {{ temp }}&#8457;
      </h2>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import { weatherApi } from "../services/WeatherApi";
import { API_KEY, WEATHER_STATS } from "../consts";
import { DateTime } from "luxon";
import { HourlyWeatherModel } from "../services/models"
export default Vue.extend({
  data: () => ({
    date: DateTime.local(),
    temp: 0,
    callCompleted: false
  }),
  created() {
    this.initialize();
  },
  methods: {
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
          this.callCompleted = true
        });
    },
  },
});
</script>

<style></style>
