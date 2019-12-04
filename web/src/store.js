//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.

import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import constants from "./constants.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    apiData: [],
    apiURL: constants.API_ENDPOINT,
    apiLoading: true,
    returnItemsCount: 0,
    dataReady: false,
    queryString: "",
    searchTerm: "",

    chkDocuments: true,
    chkData: true,
    chkProcess: true,

    chkSolar: true,
    chkUSGaap: true,
    chkDEI: true,

    chkNonnumeric: true,
    chkNumeric: true,

    chkCustomary: true,
    chkISO4217: true,
    chkSI: true,
    chkNonSI: true,

    chkAcronym: true,
    chkAbbreviation: true
  },
  getters: {
    apiData: state => state.apiData
  },
  mutations: {
    callAPI(state, payload) {

      // Note: its very important to clear data so that views don't update with data from another page
      // before API call completes.
      state.apiLoading = true;
      state.apiData = [];
      state.returnItemsCount = 0;
      state.dataReady = false;
      if (process.env.JEST_WORKER_ID == undefined) {
          // Skip call during jest unit tests.  Please note that this is not elegant (using Mocks correctly
          // would be better) and hopefully improvements can be applied later.

          axios
              .get(state.apiURL + payload + "/", {
              })
              .then(response => {
                state.apiLoading = false;
                state.apiData = response.data;
                state.returnItemsCount = response.data.length;
                state.dataReady = true;
              });
       } else {
            var data = JSON.parse(process.env.TEST_JSON);
            state.apiLoading = false;
            state.apiData = data;
            state.returnItemsCount = data.length;
            state.dataReady = true;
       }
    },
    toggleAPILoading(state) {
      state.apiLoading = !state.apiLoading;
    },
    toggleDataReady(state) {
      state.dataReady = false;
    },
    clearQueryString(state) {
      state.queryString = "";
    },
    clearEntrypointsChks(state) {
      state.chkData = false;
      state.chkDocuments = false;
      state.chkProcess = false;
    },
    clearConceptsChks(state) {
      state.chkSolar = false;
      state.chkUSGaap = false;
      state.chkDEI = false;
    },
    clearTypesChks(state) {
      state.chkNonnumeric = false;
      state.chkNumeric = false;
    },
    clearUnitsChks(state) {
      state.chkCustomary = false;
      state.chkISO4217 = false;
      state.chkSI = false;
      state.chkNonSI = false;
    },
    clearReferencesChks(state) {
      state.chkAcronym = false;
      state.chkAbbreviation = false;
    }
  }
});
