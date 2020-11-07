<template>
<v-row>
        <v-col v-for=" k of Object.keys(doors)" :key="k" cols="12" md="4">
          <v-banner class="text-center">{{ k }}</v-banner>
          <v-item>
            <v-card
              :color="doors[k] ? 'white' : 'black'"
              class="d-flex align-center"
              height="200"
              @click="openCloseDoor(k)"
            >
                <div
                  v-if="doors[k]"
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