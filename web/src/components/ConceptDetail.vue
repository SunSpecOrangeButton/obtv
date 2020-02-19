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
        <div v-if="conceptName === ''">
                <h1>Click on a row to display details</h1>
        </div>
        <div v-else>
            <form @submit.prevent>
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
                Calculations:
                <ul>
                   <li v-for="item in apiData.calculations">
                     {{ item }}
                   </li>
                </ul>
                Usages in Calculations:
                <ul>
                   <li v-for="item in apiData.usages">
                     {{ item }}
                   </li>
                </ul>
            </form>
        </div>
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

h1 {
  font-size: 18px;
  color: #4b4e52;
  font-family: "Roboto Condensed";
  font-weight: bold;
}

.public-filter {
  width: 600px;
  border: 1px solid #dadce0;
  overflow-wrap: break-word;
  padding: 5px;
}

button {
  margin: 5px;
  margin-bottom: 15px;
}

label {
  display: block;
}

label {
  margin-top: 3px;
  margin-bottom: 3px;
}

ul.a {
  list-style-type: circle;
}

li {
    list-style-type: disc;
    margin-left: 35px;
}
</style>
