<template>
    <div>
  <v-card class="mx-auto my-10"  width="200" height="10rem">
        <h2 class="text-center">{{date}}</h2>
  ></div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    props:['date']
})
</script>

<style>

</style>