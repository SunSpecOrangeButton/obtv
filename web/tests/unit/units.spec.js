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
import UnitsPage from "@/views/UnitsPage.vue";
import UnitFilter from "@/components/UnitFilter.vue"
import UnitList from "@/components/UnitList.vue"

let state
let store

const localVue = createLocalVue()
localVue.use(Vuex)

state = {
        searchTerm: "test",
        apiData: [{"id": "sample", "standard": "customary"}],
        returnItemsCount: 296
}

store = new Vuex.Store({
    state
})

describe('UnitsPage', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(UnitsPage, { store, localVue })
    expect(wrapper.html()).toContain('Download Search Results')
  })

})

describe('UnitFilter', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(UnitFilter, {store, localVue})
    expect(wrapper.html()).toContain('ISO 4217')
  })
})

describe('UnitList', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(UnitList, {store, localVue})
    expect(wrapper.html()).toContain('unit-public-list-container')
  })
})