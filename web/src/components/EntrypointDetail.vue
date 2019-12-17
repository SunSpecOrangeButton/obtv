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
-->0

<template>
    <div class="public-filter">
        <form @submit.prevent>
            <br/>
            <h1>{{ entrypointName }} </h1>
            <h2><a :name="apiData.name">{{ apiData.name }} (Abstract)</a> </h2>
            <ul>
                <li v-for="item in apiData.members">
                    <div v-if="item.indexOf('Abstract') != -1">{{ item.replace('Abstract', '') }}<a :href="'#'+item.replace('Abstract', '')"> (Abstract)</a></div>
                    <div v-else>{{ item }}</div>
                </li>

                <div v-if="apiData.tables != null">
                    <br/>
                    <div v-for="item in apiData.tables" style="margin-left:25px">
                        <h2>{{ item.name }} (Table)</h2>
                        <table border="1" style="margin-left:5px">
                            <tr>
                                <th>Concept</th>
                                <th>Purpose</th>
                            </tr>
                            <tr v-for="citem in item.columns">
                                <td>{{ citem.name }}</td>
                                <td v-if="citem.purpose == 'Abstract'"><a :href="'#'+citem.name">{{ citem.purpose }}</a></td>
                                <td v-else>{{ citem.purpose }}</td>
                            </tr>
                        </table>
                        <br/>

                        <!-- Recursive level 1 -->
                        <div v-for="apiData1 in item.children" style="margin-left:25px">
                            <br/>
                            <h2><a :name="apiData1.name">{{ apiData1.name }} (Abstract)</a> </h2>
                            <ul>
                                <li v-for="item in apiData1.members">
                                    <div v-if="item.indexOf('Abstract') != -1">{{ item.replace('Abstract', '') }}<a :href="'#'+item.replace('Abstract', '')"> (Abstract)</a></div>
                                    <div v-else>{{ item }}</div>
                                </li>

                                <!-- Tables - Recursive level 1 -->
                                <div v-if="apiData1.tables != null">
                                    <ul v-for="item in apiData1.tables" style="margin-left:25px">
                                        <h2>{{ item.name }} (Table)</h2>
                                        <table border="1" style="margin-left:5px">
                                            <tr>
                                                <th>Concept</th>
                                                <th>Purpose</th>
                                            </tr>
                                            <tr v-for="citem in item.columns">
                                                <td>{{ citem.name }}</td>
                                                <td v-if="citem.purpose == 'Abstract'"><a :href="'#'+citem.name">{{ citem.purpose }}</a></td>
                                                <td v-else>{{ citem.purpose }}</td>
                                            </tr>
                                        </table>
                                        <br/>
                                    </ul>
                                </div>
                            </ul>

                            <!-- Tables Recursive level 2 -->
                            <div v-for="apiData2 in apiData1.children" style="margin-left:25px">
                                <br/>
                                <h2><a :name="apiData2.name">{{ apiData2.name }} (Abstract)</a> </h2>
                                <ul>
                                    <li v-for="item in apiData2.members">
                                        <div v-if="item.indexOf('Abstract') != -1">{{ item.replace('Abstract', '') }}<a :href="'#'+item.replace('Abstract', '')"> (Abstract)</a></div>
                                        <div v-else>{{ item }}</div>
                                    </li>

                                    <div v-if="apiData2.tables != null">
                                        <ul v-for="item in apiData2.tables" style="margin-left:25px">
                                            <h2>{{ item.name }} (Table)</h2>
                                            <table border="1" style="margin-left:5px">
                                                <tr>
                                                    <th>Concept</th>
                                                    <th>Purpose</th>
                                                </tr>
                                                <tr v-for="citem in item.columns">
                                                    <td>{{ citem.name }}</td>
                                                    <td v-if="citem.purpose == 'Abstract'"><a :href="'#'+citem.name">{{ citem.purpose }}</a></td>
                                                    <td v-else>{{ citem.purpose }}</td>
                                                </tr>
                                            </table>
                                            <br/>
                                        </ul>
                                    </div>
                                </ul>
                            </div>

                        </div>
                        <br/>
                    </div>
                </div>
            </ul>

            <!-- Recursive level 1 -->
            <div v-for="apiData1 in apiData.children" style="margin-left:25px">
                <br/>
                <h2><a :name="apiData1.name">{{ apiData1.name }} (Abstract)</a> </h2>
                <ul>
                    <li v-for="item in apiData1.members">
                        <div v-if="item.indexOf('Abstract') != -1">{{ item.replace('Abstract', '') }}<a :href="'#'+item.replace('Abstract', '')"> (Abstract)</a></div>
                        <div v-else>{{ item }}</div>
                    </li>

                    <div v-if="apiData1.tables != null">
                        <ul v-for="item in apiData1.tables" style="margin-left:25px">
                            <h2>{{ item.name }} (Table)</h2>
                            <table border="1" style="margin-left:5px">
                                <tr>
                                    <th>Concept</th>
                                    <th>Purpose</th>
                                </tr>
                                <tr v-for="citem in item.columns">
                                    <td>{{ citem.name }}</td>
                                    <td>{{ citem.purpose }}</td>
                                </tr>
                            </table>
                            <br/>
                        </ul>
                    </div>
                </ul>

                <!-- Recursive level 2 -->
                <div v-for="apiData2 in apiData1.children" style="margin-left:25px">
                    <br/>
                    <h2><a :name="apiData1.name">{{ apiData2.name }} (Abstract)</a> </h2>
                    <ul>
                        <li v-for="item in apiData2.members">
                            <div v-if="item.indexOf('Abstract') != -1">{{ item.replace('Abstract', '') }}<a :href="'#'+item.replace('Abstract', '')"> (Abstract)</a></div>
                            <div v-else>{{ item }}</div>
                        </li>

                        <div v-if="apiData2.tables != null">
                            <ul v-for="item in apiData2.tables" style="margin-left:25px">
                                <h2>{{ item.name }} (Table)</h2>
                                <table border="1" style="margin-left:5px">
                                    <tr>
                                        <th>Concept</th>
                                        <th>Purpose</th>
                                    </tr>
                                    <tr v-for="citem in item.columns">
                                        <td>{{ citem.name }}</td>
                                        <td>{{ citem.purpose }}</td>
                                    </tr>
                                </table>
                                <br/>
                            </ul>
                        </div>
                    </ul>
                </div>

            </div>

            </ul>
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
