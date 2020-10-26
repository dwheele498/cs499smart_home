<template>
  <v-tabs @change="$emit('tab-set',($event))" grow>
    <v-tab>Weather</v-tab>
    <v-tab>Water</v-tab>
    <v-tab>Power</v-tab>
  </v-tabs>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  data: () => ({
    weather: "weather",
    water: "water",
    power: "power",
  }),
  created(){
      this.$emit('selectedTab',0);
  },
  methods: {
    tabChange(selected: Event) {
      this.$emit('setTab',selected)
    },
  },
});
</script>

<style></style>
