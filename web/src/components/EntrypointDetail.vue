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
         <entrypoint-child v-bind:abstract="apiData" v-bind:key="apiData.name"></entrypoint-child>
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
.clear-icon {
  color: #db4437;
  margin-bottom: 3px;
}

.search-icon {
  color: #4285f4;
  margin-bottom: 3px;
}
h1 {
  font-size: 18px;
  color: #4b4e52;
  font-family: "Roboto Condensed";
  font-weight: bold;
}

h2 {
  font-size: 16px;
  color: #4b4e52;
  font-family: "Roboto Condensed";
  font-weight: bold;
}

.entrypoint-detail-container {
  padding-left: 20px;
  padding-top: 5px;
  height: 100vh;
  overflow-y: scroll;
}

.form-group {
  font-family: "Roboto Condensed";

  display: block;
}

button {
  margin: 5px;
  margin-bottom: 15px;
}

label {
  display: block;
}

.button-group {
  display: flex;
  justify-content: center;
  margin-bottom: 5px;
  margin-left: -17px;
}

.btn-primary,
.btn-primary:active,
.btn-primary:visited,
.btn-primary:focus,
.btn-primary:disabled {
  background-color: white;
  border-color: #4b4e52;
  color: #4b4e52;
}

.btn-primary:hover {
  background-color: #eeeeee;
  color: #4b4e52;
  border-color: #4b4e52;
}

label {
  margin-top: 3px;
  margin-bottom: 3px;
}

#keyword_search {
  width: 214px;
}

ul.a {
  list-style-type: circle;
}

li {
    list-style-type: disc;
    margin-left: 35px;
}

</style>
