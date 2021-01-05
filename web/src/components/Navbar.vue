<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->

<template>
    <nav class="navbar navbar-expand-sm navbar-light navbar-custom">
        <router-link to="entrypoints" class="navbar-brand">
            <img id="oblogo" src="@/assets/ob.png" alt="Orange Button"/>
            <h1 class="app-title">Orange Button Taxonomy Viewer</h1>
        </router-link>
        <ul class="navbar-nav ml-auto">
            <!-- <li class="nav-item">
              <router-link to="/" class="nav-link">Home</router-link>
            </li>-->

            <li class="nav-item">
                <router-link :to="{ name: 'entrypoints' }" class="nav-link">Entrypoints</router-link>
            </li>
            <li class="nav-item">
                <router-link :to="{ name: 'concepts' }" class="nav-link">Concepts</router-link>
            </li>
            <li class="nav-item">
                <router-link :to="{ name: 'types' }" class="nav-link">Types</router-link>
            </li>
            <li class="nav-item">
                <router-link :to="{ name: 'units' }" class="nav-link">Units</router-link>
            </li>
            <li class="nav-item">
                <router-link :to="{ name: 'glossary' }" class="nav-link">Glossary</router-link>
            </li>
            <li class="nav-item">
                <router-link :to="{ name: 'about' }" class="nav-link">About</router-link>
            </li>

            <!-- <li class="nav-item">
              <router-link to="/login" class="nav-link">Login</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" href id="logout">Logout</a>
            </li>-->
        </ul>
    </nav>
</template>

<style scoped>
.navbar-custom .navbar-brand:hover {
  color: #3b3932;
}
nav {
  font-family: "Roboto Condensed";
  font-size: 1.1em;
  font-style: normal;
  display: grid;
  grid-template-columns: 30% 70%;
  padding-left: 20px;
  border-bottom: 1px solid #dadce0;
  padding-top: 12px;
}

.navbar-custom {
  background-color: white;
}

.navbar-custom .navbar-brand {
  color: #3b3932;
}

#oblogo {
  margin-top: -8px;

  width: auto;
  height: 50px;
}

.nav-link {
  color: #3b3932 !important;
}

.app-title {
  font-family: "Roboto";
  font-size: 1.25em;
  font-weight: bold;
  display: inline;
  text-transform: uppercase;
  margin-left: 5px;
}

</style>


