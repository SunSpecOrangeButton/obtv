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

const localVue = createLocalVue()
localVue.use(Vuex)

describe('EntrypointsPage', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(EntrypointsPage, { store, localVue })
    expect(wrapper.html()).toContain('Download Search Results')
  })

})

describe('EntrypointFilter', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(EntrypointFilter, {store, localVue})
    expect(wrapper.html()).toContain('Documents')
  })

  it('clears all filters on clear clearFilters()', () => {
    const wrapper = shallowMount(EntrypointFilter, {store, localVue})
    wrapper.vm.clearFilters();
    let result = wrapper.vm.$store.state.chkData || wrapper.vm.$store.state.chkDocuments ||
        wrapper.vm.$store.state.chkProcess || wrapper.vm.search_string != "";
    expect(result).toBe(false);
  })
})

describe('EntrypointList', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(EntrypointList, {store, localVue})
    expect(wrapper.html()).toContain('entrypoint-public-list-container')
  })
})