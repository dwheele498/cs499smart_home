<template>
<v-container>
    <v-banner class="text-center"><h2>{{month}}</h2></v-banner>
  <v-sparkline :value="value" fill=True :labels="labels" auto-draw></v-sparkline>
</v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { DateTime } from "luxon";
import {weatherApi} from '../services/WeatherApi';
import {WeatherModel} from '../services/WeatherModel'
import {MONTHS} from '../consts';
export default Vue.extend({
  data: () => ({
    value: [] as number[],
    labels: [] as string[],
    start: DateTime.local().set({day:1}),
    end: DateTime.local(),
    month: ''

  }),
  created(){
      this.initialize()
      this.month = MONTHS[this.end.month]
  },
  methods:{
      initialize(){
          weatherApi.getDay(this.start.toFormat("yyyy-LL-dd"),this.end.toFormat("yyyy-LL-dd")).then((res: any)=>{
              res.data.data.forEach((temp: WeatherModel) => {
                  this.value.push(temp.tavg);
                  this.labels.push(temp.date.split('-')[2]);
              });
            
          })
          }
      }
  
});
</script>

<style></style>
