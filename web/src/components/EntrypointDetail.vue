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
     <div class="entrypoint-detail-container">
        <div v-if="entrypointName === ''">
                <h1>Click on a row to display details</h1>
        </div>
        <div v-else>
             <entrypoint-child v-bind:abstract="apiData" v-bind:key="apiData.name"></entrypoint-child>
        </div>
    </div>
</template>

<script>


import EntrypointDetailChild from "../components/EntrypointDetailChild.vue";

export default {
  props: ["cn"],
  methods: {
  },
  components: {
    "entrypoint-child": EntrypointDetailChild
  },
  computed: {
    apiData() {
      return this.$store.state.apiDetailData;
    },
    entrypointName() {
      return this.$store.state.entrypointDetail;
    }
  }
};


</script>

<style scoped>
    .entrypoint-detail-container {
      overflow-wrap: break-word;
      overflow-y: scroll;
      height: 87vh;
    }

    h1 {
      font-size: 18px;
      color: #4b4e52;
      font-family: "Roboto Condensed";
      font-weight: bold;
    }
</style>
