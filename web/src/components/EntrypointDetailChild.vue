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
        <h2>{{ abstract.name }}</h2>

        <form @submit.prevent>
            <br/>
            <h2><a :name="abstract.name">{{ abstract.name }} (Abstract)</a> </h2>
            <ul>
                <li v-for="item in abstract.members">
                    <div v-if="item.indexOf('Abstract') != -1">{{ item.replace('Abstract', '') }}<a :href="'#'+item.replace('Abstract', '')"> (Abstract)</a></div>
                    <div v-else>{{ item }}</div>
                </li>

                <div v-if="abstract.tables != null">
                    <br/>
                    <div v-for="item in abstract.tables" style="margin-left:25px">
                        <h2>{{ item.name }} (Table)</h2>
                        <table border="1" style="margin-left:5px">
                            <tr>
                                <th>Concept</th>
                                <th>Purpose</th>
                            </tr>
                            <tr v-for="citem in item.columns">
                                <td>{{ citem.name }}</td>
                                <td v-if="citem.purpose == 'Abstract'"><a :href="'#'+citem.name">{{ citem.purpose }}</a></td>
                                <td v-else>{{ citem.purpose }}
                                    <div v-if="citem.valuesenum != null">
                                        Legal Values:
                                        <ul>
                                            <li v-for="vitem in citem.valuesenum">
                                                {{ vitem }}
                                            </li>
                                        </ul>
                                    </div>
                                </td>
                            </tr>
                        </table>
                        <entrypoint-child v-for="abstract in item.children" :abstract="abstract" v-bind:key="abstract.name"></entrypoint-child>
                        <br/>
                    </div>
                </div>
                <entrypoint-child v-for="abstract in abstract.children" :abstract="abstract" v-bind:key="abstract.name"></entrypoint-child>
            </ul>
        </form>
    </div>
</template>

<script>

export default {
  name: "entrypoint-child",
  props: ["abstract"]
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
