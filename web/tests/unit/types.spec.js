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
import TypesPage from "@/views/TypesPage.vue";
import TypeFilter from "@/components/TypeFilter.vue"
import TypeList from "@/components/TypeList.vue"
import store from "@/store.js"

const localVue = createLocalVue()
localVue.use(Vuex)

describe('TypesPage', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(TypesPage, { store, localVue })
    expect(wrapper.html()).toContain('Download Search Results')
  })

})

describe('TypeFilter', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(TypeFilter, {store, localVue})
    expect(wrapper.html()).toContain('numeric')
  })

  it('clears all filters on clearFilters()', () => {
    const wrapper = shallowMount(TypeFilter, {store, localVue})
    wrapper.vm.clearFilters();
    let result = wrapper.vm.$store.state.chkNumeric || wrapper.vm.$store.state.chkNonNumeric ||
        wrapper.vm.search_string != "";
    expect(result).toBe(false);
   })
})

describe('TypeList', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(TypeList, {store, localVue})
    expect(wrapper.html()).toContain('type-public-list-container')
  })
})