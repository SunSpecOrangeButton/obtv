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

import { shallowMount } from '@vue/test-utils'
import App from "@/App.vue";
import router from "@/router.js";
import store from "@/store.js";
// Note: main.js does not work correctly with jest for unknown reasons and is not part of the test
// at this point in time.

// Jest requires one test case - for the time being it always returns true (a cat is a cat) but
// it also causes syntax check for all the Javascript/Vue files.  Future expansion will add
// test cases.
describe('Main', () => {
  it('compiles ', () => {
    expect("cat").toMatch("cat")
  });
});
