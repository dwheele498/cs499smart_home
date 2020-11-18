<template>
<v-img src="../../assets/homeicons/FloorPlan.svg" align-center>
<v-container fill-height align-center class="my-6">
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
  </v-img>
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
    ...mapMutations(['openCloseWindow'])
  }
})
</script>

<style>

</style>