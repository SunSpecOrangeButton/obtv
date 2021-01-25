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
    <div class="glossary-search-container">
        <div class="glossary-count">
            <br/>
            <strong>{{ returnItemsCount }} Glossary Items</strong>
        </div>
        <div class="glossary-search-sidebar">
            <component-glossary-filter></component-glossary-filter>
        </div>
        <div class="glossary-search-body">
            <component-glossary-list></component-glossary-list>
        </div>
    </div>
</template>


<script>
import GlossaryFilter from "../components/GlossaryFilter.vue";
import GlossaryList from "../components/GlossaryList.vue";
export default {
  components: {
    "component-glossary-list": GlossaryList,
    "component-glossary-filter": GlossaryFilter
  },
  computed: {
    returnItemsCount() {
      return this.$store.state.returnItemsCount;
    }

  }
};


</script>


<style scoped>
.glossary-search-container {
  display: grid;
  grid-template-columns: 0% 16em 1% 83%;
  grid-template-rows: 13.75em auto;
  padding-top: 1.25em;
}

.glossary-search-sidebar {
  grid-column: 1 / 3;
}

.glossary-search-body {
  grid-column: 4;
  grid-row: 1 / 3;
  overflow-y: scroll;
}

.glossary-count {
    grid-column:  2 / 3;
    grid-row: 2;
    padding-left: 0.5em;
    text-align: left;
    font-weight: bold;
}

a {
  color: #4285f4;
}

</style>
