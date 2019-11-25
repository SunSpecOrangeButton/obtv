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
    <div class="type-search-container">
        <!-- <div class="breadcrumbs">
          <router-link to="/" class="nav-link">Home Page</router-link>/
          <router-link to="/" class="nav-link disabled">Type Search</router-link>
        </div>-->
        <div class="download-search-results">
            <a href>Download Search Results</a>
        </div>
        <div class="type-count">
            <br/>
            <strong>{{ returnItemsCount }} Types</strong>
        </div>
        <div class="type-search-sidebar">
            <component-type-filter></component-type-filter>
        </div>
        <div class="type-search-body">
            <component-type-list></component-type-list>
        </div>
    </div>
</template>


<script>
import TypeFilter from "../components/TypeFilter.vue";
import TypeList from "../components/TypeList.vue";
export default {
  components: {
    "component-type-list": TypeList,
    "component-type-filter": TypeFilter
  },
  computed: {
    returnItemsCount() {
      return this.$store.state.returnItemsCount;
    }

  }
};

</script>


<style scoped>
.type-search-container {
  margin-top: 20px;
  display: grid;
  grid-template-columns: 0px 250px 15px auto 25px;
  grid-template-rows: 25px auto;
}

.type-search-sidebar {
  grid-column: 2 / 3;
  grid-row: 1 / 3;
}

.type-search-body {
  grid-column: 4 / span 2;
  grid-row: 1 / span 2;
}

.breadcrumbs {
  grid-column: 2 / span 3;
  grid-row: 1 / 2;
}

.nav-link {
  display: inline;
  padding: 0;
  padding-right: 5px;
}

.download-search-results {
  grid-column: 4 / 5;
  grid-row: 1 / 2;
  font-family: "Roboto Condensed";
}

#sort-by-button {
  float: right;
}

.type-count {
  grid-column: 4 / 5;
  grid-row: 1 / 2;
  font-family: "Roboto Condensed";
}

a {
  color: #4285f4;
}

</style>