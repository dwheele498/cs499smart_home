<template>
  <canvas height="400" width="1080" id="graph"></canvas>
</template>

<script lang="ts">
import Vue from "vue";
import Chart from "chart.js";
import { ChartDataModel } from "../services/ChartDataModel";
export default Vue.extend({
  props: {
    chartData: {
      type: Object as () => ChartDataModel,
      default: null,
    },
  },
  data: () => ({
    chart: {} as Chart,
    options: {
      legend:{
        labels:{
          fontColor:'darkgrey'
        }
      },
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        yAxes: [
          {
            ticks: {
              fontColor: 'darkgrey',
              beginAtZero: true,
            },
          },
        ],
        xAxes:[
          {
          ticks: {
            fontColor: 'darkgrey',
          }
          }
        ]
      },
    },
    data: {},
  }),
  mounted() {
    Chart!.defaults!.global!.responsive=true;
    this.createChart(this.chartData);
  },
  watch: {
    chartData() {
      this.$data._chart.update();
    },
  },
  methods: {
    createChart(chartData: any) {
      const cv = document.getElementById("graph") as HTMLCanvasElement;
      const ctx = cv.getContext("2d");
      const grd = ctx!.createLinearGradient(0, 0, 0, cv.height / 0.75);
      grd.addColorStop(0, "red");
      grd.addColorStop(0.25, "orange");
      grd.addColorStop(0.5, "yellow");
      grd.addColorStop(0.75, "blue");
      this.chartData.datasets[0].backgroundColor = grd;
      this.chartData.datasets.push()
      const options = {
        type: "line",
        data: chartData,
        options: this.options,
      };
      this.chart = new Chart(cv, options);

      cv.onclick = (evt) => {
        const a = this.chart.getElementAtEvent(evt);
        this.$store.state.index = a[0]._index;
      };
    },
  },
});
</script>

<style></style>
