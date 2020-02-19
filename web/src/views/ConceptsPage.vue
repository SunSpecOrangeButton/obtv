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
    <div class="concept-search-container">
        <div class="concept-count">
            <br/>
            <strong>{{ returnItemsCount }} Concepts</strong>
        </div>
        <div class="concept-search-sidebar">
            <component-concept-filter></component-concept-filter>
        </div>
        <div class="concept-search-body">
            <component-concept-list></component-concept-list>
        </div>
        <div class="concept-detail-sidebar">
            <component-concept-detail></component-concept-detail>
        </div>
    </div>
</template>


<script>
import ConceptFilter from "../components/ConceptFilter.vue";
import ConceptList from "../components/ConceptList.vue";
import ConceptDetail from "../components/ConceptDetail.vue";
export default {
  components: {
    "component-concept-list": ConceptList,
    "component-concept-filter": ConceptFilter,
    "component-concept-detail": ConceptDetail
  },
  computed: {
    returnItemsCount() {
      return this.$store.state.returnItemsCount;
    }
  },
  created() {
      this.$store.state.conceptDetail = "";
  }
};

</script>


<style scoped>
.concept-search-container {
  margin-top: 20px;
  display: grid;
  grid-template-columns: 0px 250px 15px auto 25px;
  grid-template-rows: 25px auto;
}

.concept-search-sidebar {
  grid-column: 2 / 3;
  grid-row: 1 / 3;
}

.concept-search-body {
  grid-column: 4 / span 2;
  grid-row: 1 / span 2;
  height: 100%;
}

.concept-detail-sidebar {
  grid-column: 6 / span 2;
  grid-row: 2 / 3;
}

.concept-count {
    grid-column:  2 / 3;
    grid-row: 1 / 3;
    place-self: start;
    justify-self: center;
    padding-top: 340px;
    font-weight: bold;
}

a {
  color: #4285f4;
}

</style>