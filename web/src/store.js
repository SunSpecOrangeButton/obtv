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

import entrypointsJson from '../resources/entrypoints.json'
import conceptsJson from '../resources/concepts.json'
import typesJson from '../resources/types.json'
import unitsJson from '../resources/units.json'
import referencesJson from '../resources/references.json'
import entrypointsDetailsJson from '../resources/entrypoints-details.json'
import conceptsDetailsJson from '../resources/concepts-details.json'

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

    apiDetailData: {},
    apiDetailLoading: false,
    apiDetailDataReady: false,

    chkDocuments: true,
    chkData: true,
    chkProcess: true,
    actvChk: false,
    chkDocuments: false,
    chkData: false,
    chkProcess: false,

    chkSolar: false,
    chkUSGaap: false,
    chkDEI: false,

    chkSolarType: false,
    chkNumeric: false,
    chkBasic: false,
    chkDeiType: false,

    chkAcronym: true,
    chkAbbreviation: true,
    chkCustomary: false,
    chkISO4217: false,
    chkSI: false,
    chkNonSI: false,

    chkAcronym: false,
    chkAbbreviation: false,

    conceptDetail: "Click on a row to display details",
    entrypointDetail: "Click on a row to display details"
  },
  getters: {
    apiData: state => state.apiData,
    apiDetailData: state => state.apiDetailData
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

               if (entrypointsJson.length > 0){
                    // This will be encountered if the system was built with static pages (otherwise
                     if (payload == "entrypoints") {
                        state.apiData = entrypointsJson;
                        state.returnItemsCount = entrypointsJson.length;
                      } else if (payload == "concepts") {
                        state.apiData = conceptsJson;
                        state.returnItemsCount = conceptsJson.length;
                      } else if (payload == "types") {
                        state.apiData = typesJson;
                        state.returnItemsCount = typesJson.length;
                      } else if (payload == "units") {
                        state.apiData = unitsJson;
                        state.returnItemsCount = unitsJson.length;
                      } else if (payload == "references") {
                        state.apiData = referencesJson;
                        state.returnItemsCount = referencesJson.length;
                      }
                      state.apiLoading = false;
                      state.dataReady = true;
               } else {
                  // This version calls the web service interface.
                  axios
                      .get(state.apiURL + payload, {
                      })
                      .then(response => {
                        state.apiLoading = false;
                        state.apiData = response.data;
                        state.returnItemsCount = response.data.length;
                        state.dataReady = true;
                      });
              }
          axios
              .get(state.apiURL + payload, {
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
    callAPIdetail(state, payload) {

      // Note: its very important to clear data so that views don't update with data from another page
      // before API call completes.
      state.apiDetailLoading = true;
      state.apiDetailData = {};
      state.detailDataReady = false;

      if (process.env.JEST_WORKER_ID == undefined) {
          // Skip call during jest unit tests.  Please note that this is not elegant (using Mocks correctly
          // would be better) and hopefully improvements can be applied later.

            if (entrypointsJson.length > 0){
                // This will be encountered if the system was built with static pages (otherwise
                state.apiDetailLoading = false;
                if (payload[0] == "entrypointdetail") {
                  state.apiDetailData = entrypointsDetailsJson[payload[1]];
                } else {
                  state.apiDetailData = conceptsDetailsJson[payload[1]];
                }
                state.dataReady = true;
             } else {
                // This version calls the web service interface.
                axios
                     .get(state.apiURL + payload[0] + "/" + payload[1] + "/" + payload[2], {
                     })
                     .then(response => {
                       state.apiDetailLoading = false;
                       state.apiDetailData = response.data;
                       state.dataReady = true;
                     });
            }
       } else {
            var data = JSON.parse(process.env.TEST_JSON);
            state.apiDetailLoading = false;
            state.apiDetailData = data;
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
      state.chkSolarType = false;
      state.chkNumeric = false;
      state.chkBasic = false;
      state.chkDeiType = false;
    },
    clearUnitsChks(state) {
      state.chkCustomary = false;
      state.chkISO4217 = false;
      state.chkSI = false;
      state.chkNonSI = false;
    },
    clearGlossaryChks(state) {
      state.chkAcronym = false;
      state.chkAbbreviation = false;
    }
  }
});
