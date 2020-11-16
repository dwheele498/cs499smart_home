<template>
  <v-main>
    <tabsview @tab-set="setTab"></tabsview>
    <v-container>
      <div v-if="callComplete && tab == 0">
        <graph :chartData="weatherPrediction.chartData"></graph>
      </div>
      <div v-if="callComplete && tab == 1">
        <graph :chartData="waterData.graphData"></graph>
      </div>
      <div v-if="callComplete && tab === 2">
        <graph :chartData="powerData.graphData"></graph>
      </div>
    </v-container>
  </v-main>
</template>

<script lang="ts">
import Vue from "vue";
import TabViewsVue from "./Graphs/TabViews.vue";
import { WeatherPrediction } from "../consts";
import { GraphData } from "../services/models";
import GraphVue from "./Graphs/Graph.vue";
import { WeatherPredcitGraphModel } from "../services/models";
export default Vue.extend({
  data: () => ({
    tab: 0,
    callComplete: false,
    weathercall: WeatherPrediction,
    labels: [] as string[],
    value: [] as number[],
    weatherPrediction: {} as WeatherPredcitGraphModel,
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
      this.callComplete = false;
    this.weathercall(this.value, this.labels)
      .then((result: WeatherPredcitGraphModel) => {
        console.log(result);
        this.weatherPrediction = result;
      })
      .finally(() => {
        this.callComplete = true;
      });
  },
});
</script>
>

<style></style>
