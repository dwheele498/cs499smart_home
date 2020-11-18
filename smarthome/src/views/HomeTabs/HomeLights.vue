<template>
  <v-img>
  <img 
  src="../../assets/homeicons/FloorPlan.svg"
  height="500"
  width="600"
  >
  
  <v-row>
    <v-col v-for="k in Object.keys(lights)" :key="k" md="2">
      <v-banner class="flex-grow-1 text-left"
      height="60"
      >{{ k }}</v-banner>
      <v-item>
        <v-img
          :color="lights[k] ? 'white' : 'black'"
          class="auto"
          width="200"
          @click="onOffLight(k)"
        >
          <div
            v-if="lights[k]"
            class="display-3 flex-grow-1 text-center black--text"
          >
            <img src="../../assets/homeicons/LightOn.svg">
          </div>
          <div v-else
          class="display-3 flex-grow-1 text-center white--text"
          >
            <img src="../../assets/homeicons/LightOff.svg">
          </div>
          
        </v-img>
      </v-item>
    </v-col>
  </v-row>
  </v-img>
  
</template>

<script lang="ts">
import Vue from "vue";
import { mapMutations, mapState } from "vuex";
import { ROOMS } from "../../consts";
export default Vue.extend({
  data: () => ({
    rooms: ROOMS,
  }),
  computed: {
    ...mapState(["lights"]),
  },
  methods: {
    ...mapMutations(["onOffLight"]),
  },
});
</script>

<style></style>
