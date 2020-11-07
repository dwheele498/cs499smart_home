import Vue from "vue";
import Vuex, { MutationTree } from "vuex";

Vue.use(Vuex);

export interface RootState {
  index?: number;
  power: number;
  water: number;
  doors: Record<string, boolean>;
  lights: Record<string,boolean>;
  windows: Record<string,boolean>;
}

const mutations: MutationTree<RootState> = {
  resetIndex(state) {
    state.index = undefined;
  },
  addPower(state, payload: number) {
    state.power += payload;
  },
  addWater(state, payload: number) {
    state.water += payload;
  },
  resetPower(state) {
    state.power = 0;
  },
  resetWater(state) {
    state.water = 0;
  },
  openCloseDoor(state, payload: string) {
    for (const [k, v] of Object.entries(state.doors)) {
      if (k === payload) {
        console.log(k + ' ' + v);
        state.doors[k]=!v;
        console.log(k +' ' + state.doors[k]);
      }
    }
  },
  onOffLight(state, payload: string) {
    for (const [k, v] of Object.entries(state.lights)) {
      if (k === payload) {
        console.log(k + ' ' + v);
        state.lights[k]=!v;
        console.log(k +' ' + state.lights[k]);
      }
    }
  },
  openCloseWindow(state, payload: string) {
    for (const [k, v] of Object.entries(state.windows)) {
      if (k === payload) {
        console.log(k + ' ' + v);
        state.windows[k]=!v;
        console.log(k +' ' + state.windows[k]);
      }
    }
  },

};

const store = new Vuex.Store<RootState>({
  state: {
    index: undefined,
    power: 0,
    water: 0,
    doors: {
      "Master Bedroom Door": false,
      "Kid's Bedroom 1 Door": false,
      "Kid's Bedroom 2 Door": false,
      "Garage Door 1": false,
      "Garage Door 2": false,
      "Front Door": false,
      "Back Door": false,
      "House to Garage Door": false,
      "Bathroom Door 1": false,
      "Bathroom Door 2": false,
    },
    lights:{
      "Master Bedroom Overhead":false,
      "MB Lamp 1": false,
      "MB Lamp 2": false,
      "Kid 1 Overhead":false,
      "Kid 2 Overhead":false,
      "Kid 1 Lamp 1": false,
      "Kid 2 Lamp 2": false,
      "Bathroom 1 Overhead":false,
      "Bathroom 2 Overhead": false,
      "Living Room Overhead": false,
      "LVR Lamp 1": false,
      "LVR Lamp 2": false,
      "Kitchen Overhead": false,
      
    },
    windows:{
      "Master Bedroom Window 1":false,
      "Master Bedroom Window 2": false,
      "Kid 1 Window 1": false,
      "Kid 1 Window 2": false,
      "Kid 2 Window 1":false,
      "Kid 2 Window 2":false,
      "Bath 1 Window":false,
      "Bath 2 Window":false,
      "Living Room Window 1":false,
      "LVR Window 2":false,
      "LVR Window 3": false,
      "Kitchen Window 1":false,
      "Kitchen Window 2":false,
    }
  },
  mutations: mutations,
});

export default store;
