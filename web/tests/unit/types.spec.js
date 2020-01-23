//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.

import { shallowMount, createLocalVue} from '@vue/test-utils'
import Vuex from 'vuex'
import TypesPage from "@/views/TypesPage.vue";
import TypeFilter from "@/components/TypeFilter.vue"
import TypeList from "@/components/TypeList.vue"
import store from "@/store.js"

// import BootstrapVue from "node_modules/bootstrap-vue";
// import Icon from "node_modules/vue-awesome/components/Icon";
// Vue.component("v-icon", Icon);
// Vue.use(BootstrapVue);

const localVue = createLocalVue();
localVue.use(Vuex);

process.env.TEST_JSON = `[
    {"code": "fundStatus", "type": "solar", "values": "Closed, Open, Committed"},
    {"code": "force", "type": "numeric", "values": "N/A"}
]`;

describe('TypesPage', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(TypesPage, { store, localVue });
    expect(wrapper.html()).toContain('Types');
  });

  it('sets the computed count correctly', () => {
    const wrapper = shallowMount(TypesPage, {store, localVue});
    wrapper.vm.$store.state.returnItemsCount = 10;
    expect(wrapper.vm.returnItemsCount).toBe(10);
  });

});

describe('TypeFilter', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(TypeFilter, {store, localVue});
    expect(wrapper.html()).toContain('numeric');
  });

  it('clears all filters on clearFilters()', () => {
    const wrapper = shallowMount(TypeFilter, {store, localVue});
    wrapper.vm.clearFilters();
    let result = wrapper.vm.$store.state.chkNumeric || wrapper.vm.$store.state.chkBasic ||
        wrapper.vm.$store.state.chkSolarType || wrapper.vm.$store.state.chkDeiType ||
        wrapper.vm.$store.state.searchTerm != "";
    expect(result).toBe(false);
   });
});

describe('TypeList', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(TypeList, {store, localVue});
    expect(wrapper.html()).toContain('type-public-list-container');
  });

  it('loads the mock JSON correctly', () => {
    const wrapper = shallowMount(TypeList, {store, localVue});
    expect(wrapper.vm.$store.state.returnItemsCount).toBe(2);
    expect(wrapper.vm.$store.state.apiData[0]["code"]).toBe("fundStatus");
    expect(wrapper.vm.$store.state.apiData[1]["type"]).toBe("numeric");
    expect(wrapper.vm.$store.state.apiData[0]["values"]).toBe("Closed, Open, Committed");
    expect(wrapper.vm.$store.state.apiLoading).toBe(false);
    expect(wrapper.vm.$store.state.dataReady).toBe(true);
  });

});