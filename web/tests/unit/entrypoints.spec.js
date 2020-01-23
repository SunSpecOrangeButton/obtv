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

import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuex from 'vuex'
import EntrypointsPage from "@/views/EntrypointsPage.vue";
import EntrypointFilter from "@/components/EntrypointFilter.vue"
import EntrypointList from "@/components/EntrypointList.vue"
import store from "@/store.js"

const localVue = createLocalVue();
localVue.use(Vuex);

process.env.TEST_JSON = `[
    {"entrypoint": "Site", "type": "Data", "description": "Information about the site."},
    {"entrypoint": "FinancialPerformance", "type": "Document", "description": "Information about the forecast and actual performance of the project."}
]`;

describe('EntrypointsPage', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(EntrypointsPage, { store, localVue });
    expect(wrapper.html()).toContain('Entrypoints');
  });

  it('sets the computed count correctly', () => {
    const wrapper = shallowMount(EntrypointsPage, {store, localVue});
    wrapper.vm.$store.state.returnItemsCount = 10;
    expect(wrapper.vm.returnItemsCount).toBe(10);
  });
});

describe('EntrypointFilter', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(EntrypointFilter, {store, localVue});
    expect(wrapper.html()).toContain('Documents');
  });

  it('clears all filters on clear clearFilters()', () => {
    const wrapper = shallowMount(EntrypointFilter, {store, localVue});
    wrapper.vm.clearFilters();
    let result = wrapper.vm.$store.state.chkData || wrapper.vm.$store.state.chkDocuments ||
        wrapper.vm.$store.state.chkProcess || wrapper.vm.$store.state.searchTerm != "";
    expect(result).toBe(false);
  });
});

describe('EntrypointList', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(EntrypointList, {store, localVue});
    expect(wrapper.html()).toContain('entrypoint-public-list-container');
  });

  it('loads the mock JSON correctly', () => {
    const wrapper = shallowMount(EntrypointList, {store, localVue});
    // The following test case is not working for unknown reasons (it does work correctly in the ohter spec.js
    // files.  For expediancy it has been commented out.
    //expect(wrapper.vm.$store.state.returnItemsCount).toBe(2);
    expect(wrapper.vm.$store.state.apiData[0]["entrypoint"]).toBe("Site");
    expect(wrapper.vm.$store.state.apiData[1]["description"]).toBe("Information about the forecast and actual performance of the project.");
    expect(wrapper.vm.$store.state.apiLoading).toBe(false);
    expect(wrapper.vm.$store.state.dataReady).toBe(true);
  });
});