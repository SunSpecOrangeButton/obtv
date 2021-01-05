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
    <div class="entrypoint-search-container">
        <div class="entrypoint-count">
            {{ returnItemsCount }} Entrypoints
        </div>
        <div class="entrypoint-search-sidebar">
            <component-entrypoint-filter></component-entrypoint-filter>
        </div>
        <div class="entrypoint-search-body">
            <component-entrypoint-list></component-entrypoint-list>
        </div>
        <div class="entrypoint-detail-sidebar">
            <component-entrypoint-detail></component-entrypoint-detail>
        </div>
    </div>
</template>


<script>
import EntrypointFilter from "../components/EntrypointFilter.vue";
import EntrypointList from "../components/EntrypointList.vue";
import EntrypointDetail from "../components/EntrypointDetail.vue";
export default {
  components: {
    "component-entrypoint-list": EntrypointList,
    "component-entrypoint-filter": EntrypointFilter,
    "component-entrypoint-detail": EntrypointDetail
  },
  computed: {
    returnItemsCount() {
      return this.$store.state.returnItemsCount;
    }
  },
  created() {
      this.$store.state.entrypointDetail = "";
   }
};

</script>


<style scoped>
.entrypoint-search-container {
  display: grid;
  grid-template-columns: 0% 16em 1% 44% 41%;
  grid-template-rows: 23em auto;
  padding-top: 1.25em;
}

.entrypoint-search-sidebar {
  grid-column: 1 / 3;
}

.entrypoint-search-body {
  grid-column: 4;
  grid-row: 1 / 3;
  overflow-y: scroll;
}

.entrypoint-detail-sidebar {
  padding-left: 1em;
  grid-column: 5;
}

.entrypoint-count {
    grid-column:  2 / 3;
    grid-row: 2;
    text-align: center;
    font-weight: bold;
}

a {
  color: #4285f4;
}

</style>
