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
  display: grid;
  grid-template-columns: 0% 16em 1% 83%;
  grid-template-rows: 23em auto;
  padding-top: 1.25em;
}

.type-search-sidebar {
  grid-column: 1 / 3;
}

.type-search-body {
  grid-column: 4;
  grid-row: 1 / 3;
  overflow-y: scroll;
}

.type-count {
    grid-column:  2 / 3;
    grid-row: 2;
    text-align: center;
    font-weight: bold;
}

a {
  color: #4285f4;
}

</style>
