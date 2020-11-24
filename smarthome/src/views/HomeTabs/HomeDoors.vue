<template>
    <v-container fill-height align-center class="my-6">
      <v-flex min-width="600px">
        <v-img src="../../assets/homeicons/FloorPlan.svg"
        width="600px"
        max-width="100%"
        @click="doorSwitch($event)"
        >
        </v-img>
      </v-flex>
      <v-row>
        <v-col v-for=" k of Object.keys(doors)" :key="k" cols="12" md="2">
          <v-banner class="flex-grow-1 text-left"
          height="60"
          >{{ k }}</v-banner>
          <v-item>
            <v-card
              :color="doors[k] ? 'grey' : 'black'"
              class="d-flex align-center"
              width="200"
              @click="openCloseDoor(k)"
            >
                <div
                  v-if="doors[k]"
                  class="display-3 flex-grow-1 text-center black--text"
                >
                  <img src="../../assets/homeicons/DoorOpen.svg">
                </div>
                <div
                  v-else
                  class="display-3 flex-grow-1 text-center white--text"
                >
                  <img src="../../assets/homeicons/DoorClosed.svg">
                </div>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapMutations, mapState } from 'vuex';
import {ROOMS} from '../../consts';
export default Vue.extend({
      data: () => ({
        rooms: ROOMS,
  }),
  computed:{
    ...mapState(['doors'])
  },
  methods:{
    ...mapMutations(['openCloseDoor']),
    doorSwitch(event: MouseEvent){
    console.log(event.layerX);
    console.log(event.layerY)
    if (event.layerX>=439 && event.layerX<560 && event.layerY<=129 && event.layerY>16){
      this.openCloseDoor("Master Bedroom Door");
      }else if(event.layerX>=374 && event.layerX<420 && event.layerY<=68 && event.layerY>16){
        this.openCloseDoor("Bathroom Door 1");
      }else if(event.layerX>=374 && event.layerX<420 && event.layerY<=133 && event.layerY>77){
        this.openCloseDoor("Bathroom Door 2");
      }else if(event.layerX>=398 && event.layerX<476 && event.layerY<=300 && event.layerY>199){
        this.openCloseDoor("Kid's Bedroom 1 Door");
      }else if(event.layerX>=515 && event.layerX<590 && event.layerY<=300 && event.layerY>199){
        this.openCloseDoor("Kid's Bedroom 2 Door");
      }else if(event.layerX>=234 && event.layerX<362 && event.layerY<=307 && event.layerY>169){
        this.openCloseDoor("Front Door");
      }else if(event.layerX>=204 && event.layerX<362 && event.layerY<=80 && event.layerY>12){
        this.openCloseDoor("Back Door");
      }else if(event.layerX>=10 && event.layerX<97 && event.layerY<=304 && event.layerY>215){
        this.openCloseDoor("Garage Door 1");
      }else if(event.layerX>=98 && event.layerX<215 && event.layerY<=304 && event.layerY>215){
        this.openCloseDoor("Garage Door 2");
      }else if(event.layerX>=151 && event.layerX<257 && event.layerY<=160 && event.layerY>81){
        this.openCloseDoor("House to Garage Door");
      }
  },
  }
})
</script>

<style>

</style>