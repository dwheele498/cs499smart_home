<template>
  <v-row>
    <v-col v-for="k in Object.keys(lights)" :key="k" md="3">
      <v-banner class="text-center">{{ k }}</v-banner>
      <v-item>
        <v-card
          :color="lights[k] ? 'white' : 'black'"
          class="d-flex align-center"
          height="200"
          @click="onOffLight(k)"
        >
          <div
            v-if="lights[k]"
            class="display-3 flex-grow-1 text-center black--text"
          >
            On
          </div>
          <div v-else class="display-3 flex-grow-1 text-center white--text">
            Off
          </div>
        </v-card>
      </v-item>
    </v-col>
  </v-row>
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
