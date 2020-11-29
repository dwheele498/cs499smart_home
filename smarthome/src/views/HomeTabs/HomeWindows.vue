<template>
  <v-container fill-height align-center class="my-6">
    <v-flex min-width="600px">
        <img src="../../assets/homeicons/FloorPlanWindow.svg"
        width="600px"
        max-width="100%"
        @click="windowSwitch($event)"
        >
      </v-flex>
    <v-row>
      <v-col v-for="k in Object.keys(windows)" :key="k" md="2" align-self="center">
        <v-banner class="flex-grow-1 text-left"
        height="60"
        >{{ k }}
        </v-banner>
          <v-item>
            <v-card
              :color="windows[k] ? 'white' : 'black'"
              class="d-flex align-center"
              width="200"
              @click="openCloseWindow(k)"
            >
                <div
                  v-if="windows[k]"
                  class="display-3 flex-grow-1 text-center black--text"
                >
                  <img src="../../assets/homeicons/WindowOpen.svg">
                </div>
                <div
                  v-else
                  class="display-3 flex-grow-1 text-center white--text"
                >
                  <img src="../../assets/homeicons/WindowClosed.svg">
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
    ...mapState(['windows'])
  },
  methods:{
    ...mapMutations(['openCloseWindow']),
    windowSwitch(event: MouseEvent){
    console.log(event.layerX);
    console.log(event.layerY)
    if (event.layerX>=431 && event.layerX<508 && event.layerY<=129 && event.layerY>16){
      this.openCloseWindow("Master Bedroom Window 1");
      }else if(event.layerX>=509 && event.layerX<588 && event.layerY<=129 && event.layerY>16){
        this.openCloseWindow("Master Bedroom Window 2");
      }else if(event.layerX>=374 && event.layerX<420 && event.layerY<=68 && event.layerY>16){
        this.openCloseWindow("Bath 1 Window");
      }else if(event.layerX>=374 && event.layerX<420 && event.layerY<=133 && event.layerY>77){
        this.openCloseWindow("Bath 2 Window");
      }else if(event.layerX>=372 && event.layerX<426 && event.layerY<=300 && event.layerY>199){
        this.openCloseWindow("Kid 1 Window 1");
      }else if(event.layerX>=427 && event.layerX<479 && event.layerY<=300 && event.layerY>199){
        this.openCloseWindow("Kid 1 Window 2");
      }else if(event.layerX>=485 && event.layerX<537 && event.layerY<=300 && event.layerY>199){
        this.openCloseWindow("Kid 2 Window 1");
      }else if(event.layerX>=538 && event.layerX<588 && event.layerY<=300 && event.layerY>199){
        this.openCloseWindow("Kid 2 Window 2");
      }else if(event.layerX>=205 && event.layerX<257 && event.layerY<=307 && event.layerY>169){
        this.openCloseWindow("Living Room Window 1");
      }else if(event.layerX>=258 && event.layerX<309 && event.layerY<=307 && event.layerY>169){
        this.openCloseWindow("LVR Window 2");
      }else if(event.layerX>=310 && event.layerX<363 && event.layerY<=307 && event.layerY>169){
        this.openCloseWindow("LVR Window 3");
      }else if(event.layerX>=204 && event.layerX<283 && event.layerY<=160 && event.layerY>12){
        this.openCloseWindow("Kitchen Window 1");
      }else if(event.layerX>=284 && event.layerX<362 && event.layerY<=160 && event.layerY>12){
        this.openCloseWindow("Kitchen Window 2");
      }
  },
  }
})
</script>

<style>

</style>