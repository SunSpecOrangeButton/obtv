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
            <div class="form-group">
                <label for="keyword_search">
                    <h1>Keyword</h1>
                    <input
                            type="text"
                            class="form-control"
                            id="keyword_search"
                            v-model="$store.state.searchTerm"
                            @keyup.enter="updateQuery"
                    />
                </label>
            </div>

            <h1>Type</h1>
            <div class="form-group">
                <label for="solar">
                    <input type="checkbox" id="Solar" value="Solar" v-model="$store.state.chkSolarType"/> Solar
                </label>
                <label for="numeric">
                    <input type="checkbox" id="Numeric" value="Numeric" v-model="$store.state.chkNumeric"/> Numeric
                </label>
                <label for="basic">
                    <input type="checkbox" id="Basic" value="Basic" v-model="$store.state.chkBasic"/> Basic
                </label>
                <label for="dei">
                    <input type="checkbox" id="DEI" value="DEI" v-model="$store.state.chkDeiType"/> DEI
                </label>
            </div>
            <div class="button-group">
                <button type="button" class="btn btn-primary" @click="clearFilters">
                    <v-icon name="times" class="clear-icon"/>&nbsp;&nbsp;Clear filters
                </button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
  methods: {
    clearFilters() {
      this.$store.commit("toggleAPILoading");
      this.$store.state.searchTerm = "";
      this.$store.commit("clearQueryString");
      this.$store.commit("clearTypesChks")
      this.$store.commit("callAPI", "types/");
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
  justify-content: left;
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
</style>
