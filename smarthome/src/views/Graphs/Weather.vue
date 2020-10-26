<template>
  <v-main class="ma-auto py-0">
    <div>
      <temp
        v-if="index > 0 && tab == 0"
        :date="weatherData.labels[index]"
        :temp="weatherData.value[index]"
        :high="weatherData.highs[index]"
        :low="weatherData.lows[index]"
      ></temp>
    </div>
     <div>
      <water
        v-if="index > 0 && tab == 1"
        :date="waterData.labels[index]"
        :total="waterData.value[index]"
        :washer="waterData.clothesWasher[index]"
        :dishwasher="waterData.dishWasher[index]"
        :bath="waterData.bath[index]"
        :shower="waterData.shower[index]"
      ></water>
    </div>

    <div v-if="callComplete && tab == 0">
      <graph :chartData="weatherData.graphData"></graph>
    </div>
    <div v-if="callComplete && tab == 1">
      <graph :chartData="waterData.graphData"></graph>
    </div>
    <v-overlay :value="isLoading">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </v-main>
</template>

<script lang="ts">
import Vue from "vue";
import { mapState } from "vuex";
import Graph from "./Graph.vue";
import TempViewVue from "./TempView.vue";
import { WeatherCall, WaterCall } from "../../consts";
import * as models from "../../services/models";
import { WeatherFuncModel } from "../../services/models";
import WaterViewVue from './WaterView.vue';
export default Vue.extend({
  props: ["dates", "tab"],
  data: () => ({
    value: [] as number[],
    labels: [] as string[],
    highs: [] as number[],
    lows: [] as number[],
    weatherData: {} as models.WeatherFuncModel,
    waterData: {} as models.WaterFuncModel,
    isLoading: false,
    month: "",
    callComplete: false,
  }),

  components: {
    graph: Graph,
    temp: TempViewVue,
    water: WaterViewVue,
  },
  computed: {
    ...mapState(["index"]),
  },
  methods: {
    initialize: WeatherCall,
    waterCall: WaterCall,
  },
  created() {
    this.value = [] as number[];
    this.labels = [] as string[];
    this.highs = [] as number[];
    this.lows = [] as number[];
    this.weatherData = {} as models.WeatherFuncModel;
    this.waterData = {} as models.WaterFuncModel;
    switch (this.tab) {
      case 0:
        this.callComplete = false;
        this.isLoading = true;
        this.initialize(
          this.dates,
          this.value,
          this.labels,
          this.highs,
          this.lows
        )
          .then((weather) => {
            this.weatherData = weather;
            console.log(this.weatherData);
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
        this.waterCall(this.dates, this.value, this.labels)
          .then((waterResult) => (this.waterData = waterResult))
          .finally(() => {
            this.isLoading = false;
            this.callComplete = true;
          });
        break;
    }
  },
  watch: {
    tab(newVal) {
    this.value = [] as number[];
    this.labels = [] as string[];
    this.highs = [] as number[];
    this.lows = [] as number[];
    this.weatherData = {} as models.WeatherFuncModel;
    this.waterData = {} as models.WaterFuncModel;
      switch (newVal) {
        case 0:
          this.callComplete = false;
          this.isLoading = true;
          this.initialize(
            this.dates,
            this.value,
            this.labels,
            this.highs,
            this.lows
          )
            .then((weather) => {
              this.weatherData = weather;
              console.log(this.weatherData);
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
          this.waterCall(this.dates, this.value, this.labels)
            .then((waterResult) => {this.waterData=waterResult; this.waterData.labels=this.labels; console.log(this.waterData);})
            .finally(() => {
              this.isLoading = false;
              this.callComplete = true;
            });
          break;
      }
    },
  },
});
</script>

<style></style>
