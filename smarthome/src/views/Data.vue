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
      </v-row>
      <v-banner class="text-center"
        ><h2>{{ month }}</h2></v-banner
      >
      <div v-if="apiCalled && tab == 0">
        <weather :dates="dates" :tab="tab" :key="dateMin + dateMax"></weather>
      </div>
      <div v-if="apiCalled && tab == 1">
        <weather :dates="dates" :tab="tab" :key="dateMin + dateMax"></weather>
      </div>
       <div v-if="apiCalled && tab == 2">
        <weather :dates="dates" :tab="tab" :key="dateMin + dateMax"></weather>
      </div>
       <div v-if="tab == 3">
        <weather :tab="tab" :key="dateMin + dateMax"></weather>
      </div>
    </v-container>
  </v-main>
</template>

<script lang="ts">
import Vue from "vue";
import { DateTime } from "luxon";
import { MONTHS } from "../consts";
import TempView from "./TempView.vue";
import { mapState } from "vuex";
import TabViewsVue from "./Graphs/TabViews.vue";
import WeatherVue from "./Graphs/Weather.vue";
export default Vue.extend({
  components: {
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
    setTab(selected: number) {
      console.log(selected);
      this.tab = selected;
    },
  },
});
</script>

<style></style>
