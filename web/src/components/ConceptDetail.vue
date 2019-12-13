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
            <br/>
            <h1>{{ conceptName }} </h1>
            Label: {{ apiData.label }} <br/>
            Taxonomy: {{ apiData.taxonomy}} <br/>
            Entrypoints:<br/>
            <ul>
               <li v-for="item in apiData.entrypoints">
                 {{ item }}
               </li>
            </ul>
            Description:
            <ul>
              <li>{{ apiData.description }} </li>
            </ul>
            Item Type: {{ apiData.type }}<br/>
            Validation Rule:  {{ apiData.validationRule }} <br/>
                Precision/Decimals: {{ apiData.precisionDecimals }} <br/>
            Units:
            <ul>
               <li v-for="item in apiData.units">
                 {{ item }}
               </li>
            </ul>
            Period: {{ apiData.period }} <br/>
            Nillable: {{ apiData.nillable }} <br/>
            Calculations: {{ apiData.calculations }} <br/>
        </form>
    </div>
</template>

<script>
export default {
  props: ["cn"],
  methods: {
  },
  computed: {
    apiData() {
      return this.$store.state.apiDetailData;
    },
    conceptName() {
      return this.$store.state.conceptDetail;
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

ul.a {
  list-style-type: circle;
}

li {
    list-style-type: disc;
    margin-left: 35px;
}
</style>
