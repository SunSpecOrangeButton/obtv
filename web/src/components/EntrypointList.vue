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
    <div class="entrypoint-public-list-container">
        <div class="entrypoint-public-list">
            <b-table
                    class="entrypoint-table"
                    striped
                    hover
                    outlined
                    small
                    :fields="fields"
                    :items="apiData"
                    :busy="apiLoading"
                    @row-clicked="rowClickHandler"
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
              <b-button @click="loadMore" v-if="showLoadMore">Load more</b-button>
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
          key: "entrypoint",
          label: "Entrypoint",
          thStyle: { width: "160px" },
          thClass: ".col-field-styling",
          tdClass: ".col-entrypoint-field-styling"
        },
        {
          key: "type",
          label: "Standard",
          thClass: ".col-field-styling",
          thStyle: { width: "87px" }
        },
        {
          key: "description",
          label: "Description",
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
    this.$store.commit("callAPI", "entrypoints/");
  },
  computed: {
    apiData() {
      // console.log("Entrypoint List API DATA:");
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
          return node.entrypoint.toLowerCase().includes(this.$store.state.searchTerm.toLowerCase()) &&
            ((node.type.toLowerCase()=="data" && this.$store.state.chkData) ||
             (node.type.toLowerCase()=="documents" && this.$store.state.chkDocuments) ||
             (node.type.toLowerCase()=="process" && this.$store.state.chkProcess) ||
             (node.type.toLowerCase()=="data" && !this.$store.state.actvChk) ||
             (node.type.toLowerCase()=="documents" && !this.$store.state.actvChk) ||
             (node.type.toLowerCase()=="process" && !this.$store.state.actvChk))
      });
      this.$store.state.returnItemsCount = tableData.length;
      
      if (this.numOfElem + 1 >= this.$store.state.returnItemsCount) {
        this.showLoadMore = false
      } else {
        this.showLoadMore = true
      }

      return tableData;
    }

  },
  methods: {
    rowClickHandler(rowDetails) {
      this.$store.commit("callAPIdetail", ["entrypointdetail", rowDetails["entrypoint"]]);
      this.$store.state.entrypointDetail = rowDetails["entrypoint"];
    },
    loadMore() {
      this.numOfElem += 100;
      if (this.numOfElem + 1 >= this.$store.state.returnItemsCount) {
        this.showLoadMore = false
      } else {
        this.showLoadMore = true
      }
    }
  },
  watch: {
    "$store.state.returnItemsCount"() {
      this.numOfElem = 100
      if (this.numOfElem + 1 >= this.$store.state.returnItemsCount) {
        this.showLoadMore = false
      } else {
        this.showLoadMore = true
      }
    },
    "$store.state.chkDocuments"() {
      if (this.$store.state.chkDocuments) {
        this.$store.state.actvChk = true
      } else {
        this.$store.state.actvChk = false
      }
    },
    "$store.state.chkData"() {
      if (this.$store.state.chkData) {
        this.$store.state.actvChk = true
      } else {
        this.$store.state.actvChk = false
      }
    },
    "$store.state.chkProcess"() {
      if (this.$store.state.chkProcess) {
        this.$store.state.actvChk = true
      } else {
        this.$store.state.actvChk = false
      }
    }
  }
};

</script>

<style>
.entrypoint-public-list-container {
  height: 87vh;
}

.load-more-btn-container {
  text-align: center;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

a {
  color: #1d4679;
}

</style>
