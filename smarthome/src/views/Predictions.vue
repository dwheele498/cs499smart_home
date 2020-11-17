<template>
  <v-main>
    <tabsview @tab-set="setTab"></tabsview>
    <v-container>
      <div v-if="callComplete && tab == 0">
        <graph :chartData="prediction.chartData"></graph>
      </div>
      <div v-if="callComplete && tab == 1">
        <graph :chartData="prediction.chartData"></graph>
      </div>
      <div v-if="callComplete && tab === 2">
        <graph :chartData="prediction.chartData"></graph>
      </div>
    </v-container>
    <v-overlay :value="isLoading">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </v-main>
</template>

<script lang="ts">
import Vue from "vue";
import TabViewsVue from "./Graphs/TabViews.vue";
import {
  PowerPrediction,
  WaterPrediction,
  WeatherPrediction,
} from "../predictions";
import { GraphData, PredictionModel } from "../services/models";
import GraphVue from "./Graphs/Graph.vue";
import { PredcitGraphModel } from "../services/models";
export default Vue.extend({
  data: () => ({
    tab: 0,
    callComplete: false,
    weathercall: WeatherPrediction,
    watercall: WaterPrediction,
    powercall: PowerPrediction,
    labels: [] as string[],
    value: [] as number[],
    prediction: {} as PredcitGraphModel,
    isLoading: false,
  }),
  components: {
    tabsview: TabViewsVue,
    graph: GraphVue,
  },
  methods: {
    setTab(selected: number) {
      console.log(selected);
      this.tab = selected;
    },
  },
  created() {
    this.isLoading = true;
    this.callComplete = false;
    this.weathercall(this.value, this.labels)
      .then((result: PredcitGraphModel) => {
        console.log(result);
        this.prediction = result;
      })
      .finally(() => {
        this.callComplete = true;
        this.isLoading = false;
      });
  },
  watch: {
    tab(newVal) {
      this.value = [] as number[];
      this.labels = [] as string[];
      this.prediction = {} as PredcitGraphModel;
      switch (newVal) {
        case 0:
          this.callComplete = false;
          this.isLoading = true;
          this.weathercall(this.value, this.labels)
            .then((weather) => {
              this.prediction = weather;
              console.log(this.prediction);
            })
            .catch((err) => console.log(err))
            .finally(() => {
              this.callComplete = true;
              this.isLoading = false;
            });
          break;
        case 1:
          this.isLoading = true;
          this.callComplete = false;
          this.watercall(this.value, this.labels)
            .then((waterResult) => {
              this.prediction = waterResult;
              this.prediction.labels = this.labels;
              console.log(this.prediction);
            })
            .finally(() => {
              this.isLoading = false;
              this.callComplete = true;
            });
          break;
        case 2:
          this.isLoading = true;
          this.callComplete = false;
          this.powercall(this.value, this.labels)
            .then((powerResult) => {
              this.prediction = powerResult;
            })
            .finally(() => {
              this.isLoading = false;
              this.callComplete = true;
            });
          break;
        default:
          console.log("Tab is " + this.tab);
      }
    },
  },
});
</script>
>

<style></style>
