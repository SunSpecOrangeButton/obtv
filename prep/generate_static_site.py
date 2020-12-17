# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import generator

import json
from oblib import taxonomy


tax = taxonomy.Taxonomy()


data = generator.entrypoints()
with open("../web/resources/entrypoints.json", "w") as outfile:
    outfile.write(json.dumps(data))

entrypoints = data
with open("../web/resources/entrypoints-details.json", "w") as outfile:
    data = {}
    for entrypoint in entrypoints:
        try:
            data[entrypoint["entrypoint"]] = generator.entrypoint_detail(entrypoint["entrypoint"])
        except:
            pass
    outfile.write(json.dumps(data))

with open("../web/resources/entrypoints-concepts.json", "w") as outfile:
    data = {}
    for entrypoint in entrypoints:
        data[entrypoint["entrypoint"]] = []
        for concept in tax.semantic.get_entrypoint_concepts(entrypoint["entrypoint"]):
            data[entrypoint["entrypoint"]].append(concept.split(":")[1])
    outfile.write(json.dumps(data))

data = generator.concepts("none")
with open("../web/resources/concepts.json", "w") as outfile:
    outfile.write(json.dumps(data))

with open("../web/resources/concepts-details.json", "w") as outfile:
    concepts = data
    data = {}
    for concept in concepts:
        data[concept["name"]] = generator.concept_detail(concept["name"], concept["taxonomy"])
    outfile.write(json.dumps(data))

data = generator.types()
with open("../web/resources/types.json", "w") as outfile:
    outfile.write(json.dumps(data))

data = generator.units()
with open("../web/resources/units.json", "w") as outfile:
    outfile.write(json.dumps(data))

data = generator.glossary()
with open("../web/resources/references.json", "w") as outfile:
    outfile.write(json.dumps(data))