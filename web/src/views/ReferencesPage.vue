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
    <div class="reference-search-container">
        <!-- <div class="breadcrumbs">
          <router-link to="/" class="nav-link">Home Page</router-link>/
          <router-link to="/" class="nav-link disabled">Reference Search</router-link>
        </div>-->
        <div class="download-search-results">
            <a href>Download Search Results</a>
        </div>
        <div class="reference-count">
            <br/>
            <strong>{{ returnItemsCount }} References</strong>
        </div>
        <div class="reference-search-sidebar">
            <component-reference-filter></component-reference-filter>
        </div>
        <div class="reference-search-body">
            <component-reference-list></component-reference-list>
        </div>
    </div>
</template>


<script>
import ReferenceFilter from "../components/ReferenceFilter.vue";
import ReferenceList from "../components/ReferenceList.vue";
export default {
  components: {
    "component-reference-list": ReferenceList,
    "component-reference-filter": ReferenceFilter
  },
  computed: {
    returnItemsCount() {
      return this.$store.state.returnItemsCount;
    }

  }
};


</script>


<style scoped>
.reference-search-container {
  margin-top: 20px;
  display: grid;
  grid-template-columns: 0px 250px 15px auto 25px;
  grid-template-rows: 25px auto;
}

.reference-search-sidebar {
  grid-column: 2 / 3;
  grid-row: 1 / 3;
}

.reference-search-body {
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

.reference-count {
  grid-column: 4 / 5;
  grid-row: 1 / 2;
  font-family: "Roboto Condensed";
}

a {
  color: #4285f4;
}


</style>