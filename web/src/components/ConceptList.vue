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
    <div class="concept-public-list-container">
        <div class="concept-public-list">
            <b-table
                    class="concept-table"
                    primary-key="name"
                    striped
                    hover
                    outlined
                    small
                    :fields="fields"
                    :items="apiData"
                    :busy="apiLoading"
            >
                <!-- :items="json" -->
                <!-- :items="apiData.results" -->

                <template v-slot:table-busy>
                    <div class="text-center text-primary my-2">
                        <b-spinner class="align-middle"></b-spinner>
                        <strong>&nbsp; Loading...</strong>
                    </div>
                </template>
            </b-table>
            <div class="load-more-btn-container" v-if="!apiLoading">
              <b-button variant="primary" @click="loadMore" v-if="showLoadMore">Load more</b-button>
            </div>
        </div>
    </div>
</template>

<script>

export default {
  props: ["admin_page"],
  data() {
    return {
      fields: [
        {
          key: "name",
          label: "Name",
          thStyle: { width: "100px" },
          thClass: ".col-field-styling"
        },
        {
          key: "taxonomy",
          label: "Taxonomy",
          thClass: ".col-field-styling",
          thStyle: { width: "87px" }
        },
        {
          key: "datatype",
          label: "Data Type",
          thClass: ".col-field-styling",
          thStyle: { width: "87px" }
        },
        {
          key: "period",
          label: "Period",
          thClass: ".col-field-styling"
        }
      ],
      numOfElem: 100,
      showLoadMore: true,
      filteredCount: 0
    };
  },
  beforeCreate() {
    this.$store.state.actvChk = false;
    this.$store.state.searchTerm = "";
    this.$store.commit("callAPI", "concepts");
  },
  computed: {
    apiData() {
      // console.log("Concept List API DATA:");
      // console.log(this.$store.state.apiData);
      return this.searchFilter.slice(0, this.numOfElem);
    },
    apiLoading() {
      return this.$store.state.apiLoading;
    },
    dataReady() {
      return this.$store.state.dataReady;
    },
    searchFilter() {
      let tableData = this.$store.state.apiData.filter( node => {
          return node.name.toLowerCase().includes(this.$store.state.searchTerm.toLowerCase()) &&
            ((node.taxonomy.toLowerCase()=="solar" && this.$store.state.chkSolar) ||
             (node.taxonomy.toLowerCase()=="us-gaap" && this.$store.state.chkUSGaap) ||
             (node.taxonomy.toLowerCase()=="dei" && this.$store.state.chkDEI) ||
             (node.taxonomy.toLowerCase()=="solar" && !this.$store.state.actvChk) ||
             (node.taxonomy.toLowerCase()=="us-gaap" && !this.$store.state.actvChk) ||
             (node.taxonomy.toLowerCase()=="dei" && !this.$store.state.actvChk))
      });
      this.numOfElem = 100
      this.showLoadMore = true
      this.filteredCount = tableData.length;
      this.$store.state.returnItemsCount = this.filteredCount;
      return tableData;
    }
  },
  methods: {
    loadMore() {
      this.numOfElem += 100;
      if (this.numOfElem >= this.$store.state.returnItemsCount
          || this.numOfElem >= this.filteredCount) {
        this.showLoadMore = false
      }
    }
  },
  watch: {
    filteredCount() {
      if (this.numOfElem >= this.filteredCount) {
        this.showLoadMore = false
      }
    },
    "$store.state.returnItemsCount"() {
      if (this.numOfElem >= this.$store.state.returnItemsCount) {
        this.showLoadMore = false
      }
    },
    "$store.state.chkSolar"() {
      if (this.$store.state.chkSolar) {
        this.$store.state.actvChk = true
      } else {
        this.$store.state.actvChk = false
      }
    },
    "$store.state.chkUSGaap"() {
      if (this.$store.state.chkUSGaap) {
        this.$store.state.actvChk = true
      } else {
        this.$store.state.actvChk = false
      }
    },
    "$store.state.chkDEI"() {
      if (this.$store.state.chkDEI) {
        this.$store.state.actvChk = true
      } else {
        this.$store.state.actvChk = false
      }
    }
  }
};

</script>

<style>
.btn {
  margin: 5px;
}
.concept-public-list-container {
  display: grid;
  grid-template-rows: 50px 720px 50px;
  grid-template-columns: auto;
  height: 100%;
  padding-top: 5px;
  width: 1163px;
}

li {
  margin-top: -6px;
  margin-bottom: -6px;
}
ul {
  padding: 0;
  list-style: none;
}

.card {
  border: 2px solid #444549;
  box-shadow: 3px 3px 8px 0px rgba(0, 0, 0, 0.3);
  border-radius: 4px;
  height: 227px;
  width: 488px;
  padding: 10px;
  margin-right: 10px;
  margin-bottom: 10px;
  display: grid;
  grid-template-columns: 33% 1fr;
  grid-template-rows: 140px auto;
  font-family: "Roboto Condensed";
}

.logo {
  width: 140px;
  height: 140px;
  background-color: #d8d8d8;
}

.card-body {
  padding: 0;
  grid-column: 2 / 3;
}

.concept-public-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  background-color: white;
  height: 725px;
  justify-content: flex-start;
  align-content: flex-start;
  grid-row: 2 / 3;
  grid-column: 1 /2;
  width: 1163px;
  //overflow-y: auto;
}

a.nav-link {
  padding: 0px;
}

.loader {
  border: 16px solid #f3f3f3; /* Light grey */
  border-top: 16px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 120px;
  height: 120px;
  animation: spin 2s linear infinite;
  margin-left: 400px;
  margin-top: 150px;
  grid-row: 2 / 3;
  grid-column: 1 /2;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

#top-buttons {
  grid-row: 1 / 2;
  margin-top: -20px;
  position: relative;
  margin-left: auto;
  margin-right: 0;
}

#bottom-buttons {
  grid-row: 3 / 4;
  position: relative;
  margin-left: auto;
  margin-right: 0;
}

.pagination {
  display: flex;
  justify-content: flex-end;
}

.btn-primary,
.btn-primary:hover,
.btn-primary:active,
.btn-primary:visited,
.btn-primary:focus,
.btn-primary:disabled {
  background-color: #1d4679;
  border-color: #1d4679;
}

a {
  color: #1d4679;
}

.concept-table {
  margin-left: 0px;
}

.concept-code-field-col {
  width: 400px;
  text-align: center;
}

.col-field-styling {
  text-align: center;
}

.table {
  margin-bottom: 0px !important;
}

.load-more-btn-container {
  width: 100%;
  display: flex;
  justify-content: center;
}

</style>