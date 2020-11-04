<template>
  <v-row>
        <v-col v-for="n in 6" :key="n" cols="12" md="4">
          <v-banner class="text-center">{{ rooms[n - 1] }}</v-banner>
          <v-item v-slot:default="{ active, toggle }">
            <v-card
              :color="active ? 'white' : 'black'"
              class="d-flex align-center"
              height="200"
              @click="toggle"
            >
              <v-scroll-y-transition>
                <div
                  v-if="active"
                  class="display-3 flex-grow-1 text-center black--text"
                >
                  On
                </div>
                <div
                  v-else
                  class="display-3 flex-grow-1 text-center white--text"
                >
                  Off
                </div>
              </v-scroll-y-transition>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
</template>

<script lang="ts">
import Vue from 'vue'
import {ROOMS} from '../../consts';
export default Vue.extend({
      data: () => ({
        rooms: ROOMS,
  }),
})
</script>

<style>

</style>