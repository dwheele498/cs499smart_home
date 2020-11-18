<template>
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
    ...mapMutations(['openCloseDoor'])
  }
})
</script>

<style>

</style>