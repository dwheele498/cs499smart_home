import Vue from "vue";
import Vuex, { GetterTree, MutationTree } from "vuex";
import { UpdateDbModel } from "../services/models";

Vue.use(Vuex);

export interface RootState {
  index?: number;
  power: Record<string, UpdateDbModel>;
  water: Record<string, UpdateDbModel>;
  doors: Record<string, UpdateDbModel>;
  lights: Record<string, boolean>;
  windows: Record<string, boolean>;
  thermo: number;
  outSideTemp: number;
}

const mutations: MutationTree<RootState> = {
  resetIndex(state) {
    state.index = undefined;
  },
  addPower(state, payload: [string, number]) {
    for (const [k, v] of Object.entries(state.power)) {
      if (k == payload[0]) {
        state.power[k].amt += payload[1];
      }
    }
  },
  powerSwitch(state, payload: string) {
    for (const [k, v] of Object.entries(state.power)) {
      if (k == payload) {
        state.power[k].on
          ? (state.power[k].on = false)
          : (state.power[k].on = true);
      }
    }
  },
  addWater(state, payload: [string, number]) {
    for (const [k, v] of Object.entries(state.water)) {
      if (k == payload[0]) {
        state.water[k].amt += payload[1];
      }
    }
  },
  waterSwitch(state, payload: string) {
    for (const [k, v] of Object.entries(state.water)) {
      if (k == payload) {
        state.water[k].on
          ? (state.water[k].on = false)
          : (state.water[k].on = true);
      }
    }
  },
  doorsSwitch(state, payload: string){
    for (const [k, v] of Object.entries(state.doors)) {
      if (k == payload) {
        state.doors[k].on
          ? (state.doors[k].on = false)
          : (state.doors[k].on = true);
      }
    }
  },
  openCloseDoor(state, payload: [string,number]) {
    for (const [k, v] of Object.entries(state.doors)) {
      if (k == payload[0]) {
        state.doors[k].on
          ? (state.doors[k].on = false)
          : (state.doors[k].on = true);
        state.doors[k].amt += payload[1];

        console.log(k + " " + state.doors[k]);
      }
    }
  },
  onOffLight(state, payload: string) {
    for (const [k, v] of Object.entries(state.lights)) {
      if (k == payload) {
        console.log(k + " " + v);
        state.lights[k] ? (state.lights[k] = false) : (state.lights[k] = true);
        console.log(k + " " + state.lights[k]);
      }
    }
  },
  openCloseWindow(state, payload: string) {
    for (const [k, v] of Object.entries(state.windows)) {
      if (k === payload) {
        console.log(k + " " + v);
        state.windows[k]
          ? (state.windows[k] = false)
          : (state.windows[k] = true);
        console.log(k + " " + state.windows[k]);
      }
    }
  },
  setOutsideTemp(state, payload: number) {
    state.outSideTemp = payload;
  },
  setThermo(state, payload: number) {
    state.thermo += payload;
  },
};

const store = new Vuex.Store<RootState>({
  state: {
    index: undefined,
    power: {
      Microwave: { on: false, amt: 0 },
      Stove: { on: false, amt: 0 },
      Oven: { on: false, amt: 0 },
      BedTv: { on: false, amt: 0 },
      LivingTv: { on: false, amt: 0 },
      DishWasher: { on: false, amt: 0 },
      ClothesWasher: { on: false, amt: 0 },
      Dryer: { on: false, amt: 0 },
      HVAC: { on: false, amt: 0 },
      Exhaust: { on: false, amt: 0 },
    },

    water: {
      ClothesWasher: { on: false, amt: 0 },
      DishWasher: { on: false, amt: 0 },
      Shower: { on: false, amt: 0 },
      Bath: { on: false, amt: 0 },
    },
    doors: {
      "Master Bedroom Door": { on: false, amt: 0 },
      "Kid's Bedroom 1 Door": { on: false, amt: 0 },
      "Kid's Bedroom 2 Door": { on: false, amt: 0 },
      "Garage Door 1": { on: false, amt: 0 },
      "Garage Door 2": { on: false, amt: 0 },
      "Front Door": { on: false, amt: 0 },
      "Back Door": { on: false, amt: 0 },
      "House to Garage Door": { on: false, amt: 0 },
      "Bathroom Door 1": { on: false, amt: 0 },
      "Bathroom Door 2": { on: false, amt: 0 },
    },
    lights: {
      "Master Bedroom Overhead": false,
      "MB Lamp 1": false,
      "MB Lamp 2": false,
      "Kid 1 Overhead": false,
      "Kid 2 Overhead": false,
      "Kid 1 Lamp 1": false,
      "Kid 2 Lamp 2": false,
      "Bathroom 1 Overhead": false,
      "Bathroom 2 Overhead": false,
      "Living Room Overhead": false,
      "LVR Lamp 1": false,
      "LVR Lamp 2": false,
      "Kitchen Overhead": false,
    },
    windows: {
      "Master Bedroom Window 1": false,
      "Master Bedroom Window 2": false,
      "Kid 1 Window 1": false,
      "Kid 1 Window 2": false,
      "Kid 2 Window 1": false,
      "Kid 2 Window 2": false,
      "Bath 1 Window": false,
      "Bath 2 Window": false,
      "Living Room Window 1": false,
      "LVR Window 2": false,
      "LVR Window 3": false,
      "Kitchen Window 1": false,
      "Kitchen Window 2": false,
    },
    thermo: 68,
    outSideTemp: 0,
  },
  mutations: mutations,
});

export default store;
