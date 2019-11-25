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
import HomePage from "@/views/HomePage.vue";
import AboutPage from "@/views/AboutPage.vue";
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

const localVue = createLocalVue();

describe('HomePage', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(HomePage, { localVue });
    expect(wrapper.html()).toContain('Orange Button Taxonomy Viewer Home Page');
  });
});

describe('AboutPage', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(AboutPage, { localVue });
    expect(wrapper.html()).toContain('Orange Button');
  });
});

describe('Navbar', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(Navbar, { localVue });
    expect(wrapper.html()).toContain('Orange Button');
  });
});

describe('Footer', () => {

  it('renders a correct markup clip', () => {
    const wrapper = shallowMount(Footer, { localVue });
    expect(wrapper.html()).toContain('footer');
  });
});