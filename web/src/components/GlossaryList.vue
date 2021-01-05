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
    <div class="glossary-public-list-container">
        <div class="glossary-public-list">
            <b-table
                    class="glossary-table"
                    striped
                    hover
                    outlined
                    small
                    :fields="fields"
                    :items="apiData"
                    :busy="apiLoading"
            >
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
          key: "type",
          label: "Type",
          thClass: ".col-field-styling",
          thStyle: { width: "100px" }
        },
        {
          key: "code",
          label: "Code",
          thClass: ".col-field-styling",
          thStyle: { width: "100px" }
        },
        {
          key: "definition",
          label: "Definition",
          thClass: ".col-field-styling"
        },
      ],
      numOfElem: 100,
      showLoadMore: true,
      filteredCount: 0
    };
  },
  beforeCreate() {
    this.$store.state.actvChk = false;
    this.$store.state.searchTerm = "";
    this.$store.commit("callAPI", "glossary/");
  },
  computed: {
    apiData() {
      // console.log("Glossary List API DATA:");
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
          return node.code.toLowerCase().includes(this.$store.state.searchTerm.toLowerCase()) &&
            ((node.type.toLowerCase()=="acronym" && this.$store.state.chkAcronym) ||
             (node.type.toLowerCase()=="abbreviation" && this.$store.state.chkAbbreviation) ||
             (node.type.toLowerCase()=="acronym" && !this.$store.state.actvChk) ||
             (node.type.toLowerCase()=="abbreviation" && !this.$store.state.actvChk))
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
    "$store.state.returnItemsCount"() {
      if (this.numOfElem >= this.$store.state.returnItemsCount) {
        this.showLoadMore = false
      }
    },
    "$store.state.chkAcronym"() {
      if (this.$store.state.chkAcronym) {
        this.$store.state.actvChk = true
      } else {
        this.$store.state.actvChk = false
      }
    },
    "$store.state.chkAbbreviation"() {
      if (this.$store.state.chkAbbreviation) {
        this.$store.state.actvChk = true
      } else {
        this.$store.state.actvChk = false
      }
    }
  }
};


</script>

<style>
.glossary-public-list-container {
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
