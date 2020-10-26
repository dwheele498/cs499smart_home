<template>
  <v-main class="ma-auto py-0">
    <div>
      <temp
        v-if="index > 0"
        :date="labels[index]"
        :temp="value[index]"
        :high="highs[index]"
        :low="lows[index]"
      ></temp>
    </div>

    <div v-if="callComplete"><graph :chartData="graphData"></graph></div>
    <v-overlay :value="isLoading">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </v-main>
</template>

<script lang="ts">
import Vue from "vue";
import { mapState } from "vuex";
import { weatherApi } from "../services/WeatherApi";
import { WeatherModel } from "../services/WeatherModel";
import Graph from "../views/Graph.vue";
import { DateTime } from "luxon";
import TempViewVue from './TempView.vue';
export default Vue.extend({
  props: ["dates"],
  data: () => ({
    value: [] as number[],
    labels: [] as string[],
    highs: [] as number[],
    lows: [] as number[],
    isLoading: false,
    month: "",
    callComplete: false,
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
  }),

  components: {
    graph: Graph,
    temp: TempViewVue
  },
  computed: {
    ...mapState(["index"]),
  },
  created() {
    this.callComplete = false;
    this.initialize();
  },
  methods: {
    async initialize() {
      this.isLoading = true;
      this.$store.commit("resetIndex");
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
                this.labels.push(dt.toFormat("M/d"));
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
          this.graphData.datasets[0].data = this.value;
          this.graphData.labels = this.labels;
          this.callComplete = true;
          this.isLoading = false;
        });
    },
  },
});
</script>

<style></style>
