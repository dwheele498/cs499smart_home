import Vue from "vue";
import Vuex, { MutationTree } from "vuex";

Vue.use(Vuex);

export interface RootState {
  index?: number;
}

const mutations: MutationTree<RootState> = {
  resetIndex(state) {
    state.index = undefined;
  },
};

const store = new Vuex.Store<RootState>({
  state: {
    index: undefined,
  },
  mutations: mutations,
});

export default store;
