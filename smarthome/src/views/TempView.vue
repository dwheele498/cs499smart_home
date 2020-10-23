<template>
  <v-card class="mx-auto my-10"  width="200" height="8rem">
        <h2 class="text-center">{{formatDate()}}</h2>
    <v-card-text class="text-center">
      <h2 class="mx-auto px-auto red--text text--lighten-3">High: {{high}}&#8457;</h2>
      <h2 class="mx-auto px-auto lime-text">Avg: {{ temp }}&#8457;</h2>
      <h2 class="mx-auto px-auto teal--text">Low: {{low}}&#8457;</h2>
      </v-card-text
    ></v-card
  >
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    props:['date','temp','high','low'],
    methods:{
      formatDate(){
        const dateSplit = this.date.split('-')
        return [dateSplit[1],dateSplit[2]].join('/')
      }
    }
})
</script>

<style>

</style>