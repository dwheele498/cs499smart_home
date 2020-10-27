import Vue from "vue";
import Vuex, { MutationTree } from "vuex";

Vue.use(Vuex);

export interface RootState {
  index?: number;
  power: number;
  water: number;
}

const mutations: MutationTree<RootState> = {
  resetIndex(state) {
    state.index = 0;
  },
  addPower(state, payload: number) {
    state.power += payload;
  },
  addWater(state, payload: number) {
    state.water += payload;
  },
  resetPower(state){
    state.power = 0;
  },
  resetWater(state){
    state.water = 0;
  }
};

const store = new Vuex.Store<RootState>({
  state: {
    index: undefined,
    power: 0,
    water: 0,
  },
  mutations: mutations,
});

export default store;
