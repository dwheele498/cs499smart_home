<template>
  <v-container class="ma-auto py-0">
    <v-row align="center">
      <v-date-picker
        class="pa-auto"
        color="primary"
        v-model="dates"
        range
        :min="dateMin"
        :max="dateMax"
      ></v-date-picker>
      ><temp
        v-if="index > 0"
        :date="labels[index]"
        :month="month"
        :temp="value[index]"
        :high="highs[index]"
        :low="lows[index]"
      ></temp>
    </v-row>
    <v-banner class="text-center"
      ><h2>{{ month }}</h2></v-banner
    >
    <graph v-if="apiCalled" :chartData="graphData"></graph>
    <v-overlay :value="isLoading">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { DateTime } from "luxon";
import { weatherApi } from "../services/WeatherApi";
import { WeatherModel } from "../services/WeatherModel";
import { MONTHS } from "../consts";
import GraphVue from "./Graph.vue";
import TempView from "./TempView.vue";
import { mapState } from "vuex";
import { AxiosResponse } from "axios";
export default Vue.extend({
  components: {
    graph: GraphVue,
    temp: TempView,
  },
  data: () => ({
    apiCalled: false,
    value: [] as number[],
    labels: [] as string[],
    highs: [] as number[],
    lows: [] as number[],
    dateMin: DateTime.local()
      .set({ day: 1 })
      .toFormat("yyyy-MM-dd"),
    dateMax: DateTime.local()
      .set({ day: DateTime.local().day - 1 })
      .toFormat("yyyy-MM-dd"),
    dates: [] as string[],
    displayDate: "",
    month: "",
    graphData: {
      labels: [] as string[],
      datasets: [
        {
          borderColor: "red",
          label: "Avg Daily Temp",
          data: [] as number[],
          backgroundColor: ["#32a852"],
        },
      ],
    },
    isLoading: false,
  }),
  computed: {
    ...mapState(["index"]),
  },
  watch: {
    dates() {
      if (this.dates.length == 2) {
        this.displayDate = this.dates[1];
        this.month = (this.dates[0].split('-')[1]);
        this.initialize();
      }
    },
  },
  created() {
    this.$store.commit("resetIndex");
    this.month = MONTHS[Number.parseInt(this.dates[0])];
  },
  methods: {
    async initialize() {
      this.$store.commit("resetIndex");
      this.apiCalled = false;
      this.isLoading = true;
      this.labels = [] as string[];
      this.value = [] as number[];
      const start = this.dates[0];
      const end = this.dates[1];
      await weatherApi
        .getMonth(start, end)
        .then((res: any) => {
          console.log(res);
          res.data.data.forEach((temp: WeatherModel) => {
            if (temp.tavg == null) {
              console.log("");
            } else {
              const inLabel = this.labels.find((d) => {
                d == `${temp.month}-${temp.day}`;
              });
              if (!inLabel) {
                const dt = DateTime.local().set({
                  month: Number.parseInt(temp.month),
                  day: Number.parseInt(temp.day),
                });
                console.log(temp);
                this.value.push(temp.tavg);
                this.labels.push(dt.toFormat("d"));
                this.lows.push(temp.tmin);
                this.highs.push(temp.tmax);
                const i = this.labels.indexOf(`${temp.month}-${temp.day}`);
                this.value[i] += Math.floor(temp.tavg / 2);
              }
            }
          });
        })
        .catch((err: Error) => console.log(err.message))
        .finally(() => {
          this.isLoading = false;
          this.graphData.datasets[0].data = this.value;
          this.graphData.labels = this.labels;
          this.apiCalled = true;
          this.dates = [];
        });
    },
  },
});
</script>

<style></style>
