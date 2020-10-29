<template>
    <div>
  <v-card class="mx-auto my-10"  width="200" height="10rem">
        <h2 class="text-center">{{date}}</h2>
    <v-card-text class="text-center">
      <h2 class="mx-auto px-auto cyan--text text--lighten-3">Total: {{total}} gal/hr</h2>
      <h2 class="mx-auto px-auto orange--text text--darken-3">Washer: {{ washer }} gal/hr</h2>
      <h2 class="mx-auto px-auto green--text text--darken-2">Dishwasher: {{dishwasher}} gal/hr</h2>
      <h2 class="mx-auto px-auto teal--text">Shower: {{ shower }} gal/hr</h2>
      <h2 class="mx-auto px-auto blue--text text--darken-3">Bath: {{bath}} gal/hr</h2>
      </v-card-text
    ></v-card
  ></div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    props:['date','total','washer','dishwasher','shower','bath']
})
</script>

<style>

</style>