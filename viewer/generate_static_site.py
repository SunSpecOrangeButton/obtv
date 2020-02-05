# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import viewer

import json
from oblib import taxonomy
from flask import Flask


app = Flask(__name__)
tax = taxonomy.Taxonomy()


with app.app_context():
    data = viewer.entrypoints().data.decode('UTF-8')
    with open("../resources/entrypoints.json", "w") as outfile:
        outfile.write(data)

    entrypoints = json.loads(data)
    with open("../resources/entrypoints-details.json", "w") as outfile:
        data = {}
        for entrypoint in entrypoints:
            try:
                data[entrypoint["entrypoint"]] = json.loads(viewer.entrypoint_detail(entrypoint["entrypoint"]).data.decode('UTF-8'))
            except:
                pass
        outfile.write(json.dumps(data))

    with open("../resources/entrypoints-concepts.json", "w") as outfile:
        data = {}
        for entrypoint in entrypoints:
            data[entrypoint["entrypoint"]] = []
            for concept in tax.semantic.get_entrypoint_concepts(entrypoint["entrypoint"]):
                data[entrypoint["entrypoint"]].append(concept.split(":")[1])
        outfile.write(json.dumps(data))

    data = viewer.concepts("none").data.decode('UTF-8')
    with open("../resources/concepts.json", "w") as outfile:
        outfile.write(data)

    with open("../resources/concepts-details.json", "w") as outfile:
        concepts = json.loads(data)
        data = {}
        for concept in concepts:
            data[concept["name"]] = json.loads(viewer.concept_detail(concept["name"], concept["taxonomy"]).data.decode('UTF-8'))
        outfile.write(json.dumps(data))

    data = viewer.types().data.decode('UTF-8')
    with open("../resources/types.json", "w") as outfile:
        outfile.write(data)

    data = viewer.units().data.decode('UTF-8')
    with open("../resources/units.json", "w") as outfile:
        outfile.write(data)

    data = viewer.glossary().data.decode('UTF-8')
    with open("../resources/references.json", "w") as outfile:
        outfile.write(data)