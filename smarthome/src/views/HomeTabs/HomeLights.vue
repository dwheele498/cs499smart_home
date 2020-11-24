<template>
    <v-container>
      <v-flex min-width="600px">
        <img src="../../assets/homeicons/FloorPlan.svg"
        width="600px"
        max-width="100%"
        @click="lightSwitch($event)"
        >
      </v-flex>
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
    </v-container>  
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
    lightSwitch(event: MouseEvent){
    console.log(event.layerX);
    console.log(event.layerY)
    if (event.layerX>=439 && event.layerX<560 && event.layerY<=129 && event.layerY>16){
      this.onOffLight("Master Bedroom Overhead");
      }else if(event.layerX>=561 && event.layerX<591 && event.layerY<=43 && event.layerY>19){
        this.onOffLight("MB Lamp 1");
      }else if(event.layerX>=561 && event.layerX<591 && event.layerY<=129 && event.layerY>102){
        this.onOffLight("MB Lamp 2");
      }else if(event.layerX>=374 && event.layerX<420 && event.layerY<=68 && event.layerY>16){
        this.onOffLight("Bathroom 1 Overhead");
      }else if(event.layerX>=374 && event.layerX<420 && event.layerY<=133 && event.layerY>77){
        this.onOffLight("Bathroom 2 Overhead");
      }else if(event.layerX>=398 && event.layerX<476 && event.layerY<=300 && event.layerY>199){
        this.onOffLight("Kid 1 Overhead");
      }else if(event.layerX>=374 && event.layerX<397 && event.layerY<=300 && event.layerY>199){
        this.onOffLight("Kid 1 Lamp 1");
      }else if(event.layerX>=515 && event.layerX<590 && event.layerY<=300 && event.layerY>199){
        this.onOffLight("Kid 2 Overhead");
      }else if(event.layerX>=477 && event.layerX<514 && event.layerY<=300 && event.layerY>199){
        this.onOffLight("Kid 2 Lamp 2");
      }else if(event.layerX>=234 && event.layerX<362 && event.layerY<=307 && event.layerY>169){
        this.onOffLight("Living Room Overhead");
      }else if(event.layerX>=204 && event.layerX<233 && event.layerY<=304 && event.layerY>238){
        this.onOffLight("LVR Lamp 1");
      }else if(event.layerX>=204 && event.layerX<233 && event.layerY<=239 && event.layerY>168){
        this.onOffLight("LVR Lamp 2");
      }else if(event.layerX>=204 && event.layerX<362 && event.layerY<=160 && event.layerY>12){
        this.onOffLight("Kitchen Overhead");
      }
  },
  },
});

</script>

<style></style>
