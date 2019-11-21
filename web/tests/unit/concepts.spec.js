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

let state
let store

const localVue = createLocalVue()
localVue.use(Vuex)

state = {
        searchTerm: "test",
        apiData: [{"name": "Curtailment", "taxonomy": "solar"}],
        returnItemsCount: 296
}

store = new Vuex.Store({
    state
})

describe('ConceptsPage', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(ConceptsPage, { store, localVue })
    expect(wrapper.html()).toContain('Download Search Results')
  })

})

describe('ConceptFilter', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(ConceptFilter, {store, localVue})
    expect(wrapper.html()).toContain('US-Gaap')
  })
})

describe('ConceptList', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(ConceptList, {store, localVue})
    expect(wrapper.html()).toContain('concept-public-list-container')
  })
})
