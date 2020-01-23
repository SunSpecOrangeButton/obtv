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
    <div class="public-filter">
        <form @submit.prevent>
            <h1>Keyword</h1>
            <div class="form-group">
                <input
                        type="text"
                        class="form-control"
                        id="keyword_search"
                        v-model="$store.state.searchTerm"
                        @keyup.enter="updateQuery"
                />
            </div>

            <h1>Concept Type</h1>
            <div class="form-group">
                <label for="data">
                    <input type="checkbox" id="solar" value="Solar" v-model="$store.state.chkSolar"/> Solar
                </label>
                <label for="documents">
                    <input type="checkbox" id="usgaap" value="USGaap" v-model="$store.state.chkUSGaap"/> US-Gaap
                </label>
                <label for="process">
                    <input type="checkbox" id="dei" value="DEI" v-model="$store.state.chkDEI"/> DEI
                </label>
                <label for="entryPointSelector">
                  <h1>Select entrypoint:</h1>
                  <b-form-select v-model="entryPointSelected" :options="entryPointList" />
                </label>
            </div>
            <div class="button-group">
                <button type="button" class="btn btn-primary" @click="updateQuery">
                    <v-icon name="search" class="search-icon"/>&nbsp; Search
                </button>
                <button type="button" class="btn btn-primary" @click="clearFilters">
                    <v-icon name="times" class="clear-icon"/>&nbsp;&nbsp;Clear filters
                </button>
            </div>
        </form>
    </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      entryPointList: [],
      entryPointSelected: ''
    }
  },
  beforeCreate() {
    axios
    .get(this.$store.state.apiURL + "entrypoints/", {
    })
    .then(response => {
      let entrypoint_data = response.data;
      for (let i in entrypoint_data) {
        this.entryPointList.push(entrypoint_data[i]["entrypoint"])
      }
    });
  },
  methods: {
    updateQuery() {
       // TODO: Remove - currently referenced in other code.
    },
    clearFilters() {
      this.$store.commit("toggleAPILoading");
      this.$store.state.searchTerm = "";
      this.$store.commit("clearQueryString");
      this.$store.commit("clearConceptsChks");
      this.entryPointSelected = '';
      this.$store.commit("callAPI", "concepts/none");
    }
  },
  watch: {
    entryPointSelected() {
      if (this.entryPointSelected) {
        this.$store.commit("callAPI", "concepts/" + this.entryPointSelected);
      }
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

.public-filter {
  padding-left: 20px;
  padding-top: 5px;
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

</style>
