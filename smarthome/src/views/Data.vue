<template>
  <v-main>
    <tab-choice @tab-set="setTab"></tab-choice>
    <v-container class="ma-auto py-0">
      <h2 class="text-center">Please Select a Date Range</h2>
      <v-row align="center">
        <v-menu
          ref="startMenu"
          :close-on-content-click="false"
          :return-value.sync="dateMin"
          transition="scale-transition"
          offset-y
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="dateMin"
              label="Start Date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker v-model="dateMin" :max="dateMax" no-title scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="$refs.startMenu.save(dateMin)">
              OK
            </v-btn>
          </v-date-picker>
        </v-menu>
        <v-menu
          ref="menu"
          :close-on-content-click="false"
          :return-value.sync="dateMax"
          transition="scale-transition"
          offset-y
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="dateMax"
              label="End Date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker v-model="dateMax" no-title scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="$refs.menu.save(dateMax)">
              OK
            </v-btn>
          </v-date-picker>
        </v-menu>
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
     <div v-if="apiCalled && tab==0"><weather :dates="dates" :key=dateMin+dateMax ></weather> </div>
     
      
    </v-container>
  </v-main>
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
import TabViewsVue from "./TabViews.vue";
import WeatherVue from './Weather.vue';
export default Vue.extend({
  components: {
    temp: TempView,
    tabChoice: TabViewsVue,
    weather: WeatherVue,
  },
  data: () => ({
    apiCalled: false,
    value: [] as number[],
    labels: [] as string[],
    highs: [] as number[],
    lows: [] as number[],
    tab: 0,
    dateMin: "",
    dateMax: "",
    dates: [] as string[],
    displayDate: "",
    month: "",
    isLoading: false,
  }),
  computed: {
    ...mapState(["index"]),
  },
  watch: {
    dateMin() {
      this.dates[0] = this.dateMin;
      console.log(this.dates);
      this.displayDate = this.dateMin;
      this.apiCalled = false;
      if (this.dates.length == 2) {
        this.month = this.dateMin + " - " + this.dateMax;
        this.apiCalled = true;
        
      }
    },
    dateMax() {
      this.dates[1] = this.dateMax;
      console.log(this.dates);
      this.apiCalled = false;
      if (this.dates.length == 2 && this.dates[0]) {
        this.month = this.dateMin + " - " + this.dateMax;
        this.apiCalled = true;
      }
    },
  
  },

  created() {
    this.$store.commit("resetIndex");
  },
  methods: {
    setTab(selected: number){
      console.log(selected);
      this.tab = selected;
      this.apiCalled = false;
    },
    
    // async initialize() {
    //   this.$store.commit("resetIndex");
    //   this.apiCalled = false;
    //   this.isLoading = true;
    //   this.labels = [] as string[];
    //   this.value = [] as number[];
    //   const start = this.dateMin;
    //   const end = this.dateMax;
    //   await weatherApi
    //     .getMonth(start, end)
    //     .then((res: any) => {
    //       console.log(res);
    //       res.data.data.forEach((temp: WeatherModel) => {
    //         if (temp.tavg == null) {
    //           console.log("");
    //         } else {
    //           const inLabel = this.labels.find((d) => {
    //             d == `${temp.month}-${temp.day}`;
    //           });
    //           if (!inLabel) {
    //             const dt = DateTime.local().set({
    //               month: Number.parseInt(temp.month),
    //               day: Number.parseInt(temp.day),
    //             });
    //             console.log(temp);
    //             this.value.push(temp.tavg);
    //             this.labels.push(dt.toFormat("d"));
    //             this.lows.push(temp.tmin);
    //             this.highs.push(temp.tmax);
    //             const i = this.labels.indexOf(`${temp.month}-${temp.day}`);
    //             this.value[i] += Math.floor(temp.tavg / 2);
    //           }
    //         }
    //       });
    //     })
    //     .catch((err: Error) => console.log(err.message))
    //     .finally(() => {
    //       this.isLoading = false;
    //       this.graphData.datasets[0].data = this.value;
    //       this.graphData.labels = this.labels;
    //       this.apiCalled = true;

    //       this.dates = [];
    //     });
    // },
    // async getWater(){
    //   this.$store.commit("resetIndex");
    //   this.apiCalled = false;
    //   this.isLoading = true;
    //   this.labels = [] as string[];
    //   this.value = [] as number[];
    //   const start = this.dates[0];
    //   const end = this.dates[1];
    //   .getMonth(start, end)
    //     .then((res: any) => {
    //       console.log(res);
    //       res.data.data.forEach((temp: WeatherModel) => {
    //         if (temp.tavg == null) {
    //           console.log("");
    //         } else {
    //           const inLabel = this.labels.find((d) => {
    //             d == `${temp.month}-${temp.day}`;
    //           });
    //           if (!inLabel) {
    //             const dt = DateTime.local().set({
    //               month: Number.parseInt(temp.month),
    //               day: Number.parseInt(temp.day),
    //             });
    //             console.log(temp);
    //             this.value.push(temp.tavg);
    //             this.labels.push(dt.toFormat("d"));
    //             this.lows.push(temp.tmin);
    //             this.highs.push(temp.tmax);
    //             const i = this.labels.indexOf(`${temp.month}-${temp.day}`);
    //             this.value[i] += Math.floor(temp.tavg / 2);
    //           }
    //         }
    //       });
    //     })
    //     .catch((err: Error) => console.log(err.message))
    //     .finally(() => {
    //       this.isLoading = false;
    //       this.graphData.datasets[0].data = this.value;
    //       this.graphData.labels = this.labels;
    //       this.apiCalled = true;
    //       this.dates = [];
    //     });
    // }
  },
});
</script>

<style></style>
