<template>
  <v-row>
        <v-col v-for="k in Object.keys(windows)" :key="k" md="3" align-self="center">
          <v-banner class="text-center">{{ k }}</v-banner>
          <v-item>
            <v-card
              :color="windows[k] ? 'white' : 'black'"
              class="d-flex align-center"
              height="200"
              @click="openCloseWindow(k)"
            >
                <div
                  v-if="windows[k]"
                  class="display-3 flex-grow-1 text-center black--text"
                >
                  Open
                </div>
                <div
                  v-else
                  class="display-3 flex-grow-1 text-center white--text"
                >
                  Closed
                </div>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
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