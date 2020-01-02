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

import Vue from "vue";
import Router from "vue-router";
import Home from "./views/HomePage.vue";
import About from "./views/AboutPage.vue";
import Concepts from "./views/ConceptsPage.vue"
import EntrypointsPage from "./views/EntrypointsPage.vue";
import TypesPage from "./views/TypesPage.vue";
import UnitsPage from "./views/UnitsPage";
import ReferencesPage from "./views/ReferencesPage";

Vue.use(Router);

export default new Router({
  routes: [
    { path: "/", redirect: "/entrypoints" },
    {
      path: "/entrypoints",
      name: "entrypoints",
      component: EntrypointsPage
    },
     {
       path: "/concepts",
       name: "concepts",
       component: Concepts
     },
    {
      path: "/types",
      name: "types",
      component: TypesPage
    },
     {
       path: "/units",
       name: "units",
       component: UnitsPage
     },
     {
       path: "/references",
       name: "references",
       component: ReferencesPage
     },
     {
       path: "/about",
       name: "about",
       component: About
     }
  ]
});
