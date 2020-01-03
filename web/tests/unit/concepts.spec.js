//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.

import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuex from 'vuex'
import ConceptsPage from "@/views/ConceptsPage.vue";
import ConceptFilter from "@/components/ConceptFilter.vue"
import ConceptList from "@/components/ConceptList.vue"
import store from "@/store.js"

const localVue = createLocalVue();
localVue.use(Vuex);

process.env.TEST_JSON =  `[
    {"name": "Curtailment", "taxonomy": "SOLAR", "datatype": "energy", "period": "duration"},
    {"name": "AccruedLiabilitiesCurrent", "taxonomy": "US-GAAP", "datatype": "monetary", "period": "instant"}
]`;

describe('ConceptsPage', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(ConceptsPage, { store, localVue });
    expect(wrapper.html()).toContain('Concepts');
  });

  it('sets the computed count correctly', () => {
    const wrapper = shallowMount(ConceptsPage, {store, localVue});
    wrapper.vm.$store.state.returnItemsCount = 10;
    expect(wrapper.vm.returnItemsCount).toBe(10);
  });
});

describe('ConceptFilter', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(ConceptFilter, {store, localVue});
    expect(wrapper.html()).toContain('US-Gaap');
  });

  it('clears all filters on clearFilters()', () => {
    const wrapper = shallowMount(ConceptFilter, {store, localVue});
    wrapper.vm.clearFilters();
    let result = wrapper.vm.$store.state.chkSolar || wrapper.vm.$store.state.chkUSGaap ||
        wrapper.vm.$store.state.chkDEI || wrapper.vm.$store.state.searchTerm != "";
    expect(result).toBe(false);
  });
});

describe('ConceptList', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(ConceptList, {store, localVue});
    expect(wrapper.html()).toContain('concept-public-list-container');
  });

  it('loads the mock JSON correctly', () => {
    const wrapper = shallowMount(ConceptList, {store, localVue});
    let state = wrapper.vm.$store.state;
    expect(wrapper.vm.$store.state.returnItemsCount).toBe(2);
    expect(wrapper.vm.$store.state.apiData[0]["name"]).toBe("Curtailment");
    expect(wrapper.vm.$store.state.apiData[0]["taxonomy"]).toBe("SOLAR");
    expect(wrapper.vm.$store.state.apiData[1]["datatype"]).toBe("monetary");
    expect(wrapper.vm.$store.state.apiData[1]["period"]).toBe("instant");
    expect(wrapper.vm.$store.state.apiLoading).toBe(false);
    expect(wrapper.vm.$store.state.dataReady).toBe(true);
  });
});
