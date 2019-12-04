# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This program implements the Orange Button Viewer.  The Orange Button Viewer provides full information on the Orange Button data structures
in an easy to use format that does not require XBRL experience.

Use the following comand to start the Viewer.

    $ pip install Flask
    $ FLASK_APP=viewer.py flask run
"""

import reference

import json
from oblib import taxonomy, data_model, parser
from flask import Flask, request, render_template
from flask_cors import CORS

RETURN_INDEX = "<h2><a href='/html'>Return to search page</a></h2>"
tax = None

def init():
    """Initialize program"""

    global tax
    tax = taxonomy.Taxonomy()
    print("Initialization completed")


"""Main Code - Start Flask"""
init()
app = Flask(__name__, static_url_path='', static_folder='dist')
CORS(app)
"""End of Main Code"""

@app.route('/concepts/', methods=['GET'])
def concepts():
    """Flask Read Handler for concepts API Endpoint"""

    print("Concepts endpoint")

    try:
        data = []
        for concept in tax.semantic.get_all_concepts(details=True):
            details = tax.semantic.get_concept_details(concept)
            if not details.abstract:
                t = "SOLAR"
                if details.id.startswith("us-gaap:"):
                    t = "US-GAAP"
                elif details.id.startswith("dei:"):
                    t = "DEI"
                data.append({
                    "name": details.name,
                    "taxonomy": t,
                    "datatype": details.type_name.split(":")[1].replace("ItemType", ""),
                    "period": details.period_type.value
                })
            # })
        s = json.dumps(data)
        return s
    except Exception as e:
        print(e)
        return "Error occurred - try again"


@app.route('/units/', methods=['GET'])
def units():
    """Flask Read Handler for units API Endpoint"""

    print("Units endpoint")

    try:
        data = []
        for unit in tax.units.get_all_units():
            details = tax.units.get_unit(unit)

            data.append({
                "id": details.unit_id,
                "name": details.unit_name,
                "symbol": details.symbol,
                "type": details.item_type.replace("ItemType", ""),
                "standard": details.base_standard.value,
                "definition": details.definition
            })
            # data.append(unit)
        s = json.dumps(data)
        return s
    except Exception as e:
        print(e)
        return "Error occurred - try again"


@app.route('/types/', methods=['GET'])
def types():
    """Flask Read Handler for types API Endpoint"""

    print("Types endpoint")

    try:
        data = []
        for type in tax.types.get_all_types():

            values = ""
            first = True
            for e in tax.types.get_type_enum(type):
                if not first:
                    values += ", "
                first = False
                values += e

            data.append({
                "code": type.replace("solar-types:", "").replace("ItemType", ""),
                "type": "Non numeric",
                "values": values,
                "definition": ""
            })

        for numeric_type in tax.numeric_types.get_all_numeric_types():
            data.append({
                "code": numeric_type.replace("num-us:", ""),
                "type": "Numeric",
                "values": "N/A",
                "definition": ""
            })
        s = json.dumps(data)
        return s
    except Exception as e:
        print(e)
        return "Error occurred - try again"


@app.route('/entrypoints/', methods=['GET'])
def entrypoints():
    """Flask Read Handler for entrypoints API endpoint"""

    print("Entypoints endpoint")

    try:
        data = []
        for ep in tax.semantic.get_all_entrypoints():
            t = ""
            if ep in ["AssetManager", "Developer", "Entity", "FinanicalPerformance", "Fund", "Insurance",
                      "OperationalPerformance", "OperationsManager", "Portfolio", "Project", "Site", "Sponsor",
                      "System", "SystemDeviceListing", "Utility"]:
                t = "Data"
            elif ep == "ProjectFinancing":
                t = "Process"
            else:
                t = "Document"
            description = "This schema contains the entry point for the " + ep

            concepts = tax.semantic.get_entrypoint_concepts(ep)
            if len(concepts) > 0:
                description = tax.documentation.get_concept_documentation(concepts[0])

            data.append({
                "entrypoint": ep,
                "type": t,
                "description": description
            })
        s = json.dumps(data)
        # s = json.dumps(tax.semantic.get_all_entrypoints())
        return s
    except Exception as e:
        print(e)
        return "Error occurred - try again"

@app.route('/references/', methods=['GET'])
def references():
    """Flask Read Handler for types API Endpoint"""

    print("Reference endpoint")

    try:
        data = []
        for item in reference.ACRONYMS.items():
            data.append({
                "type": "Acronym",
                "code": item[1],
                "definition": item[0]
            })

        for item in reference.ABBREVIATIONS.items():
            data.append({
                "type": "Abbreviation",
                "code": item[1],
                "definition": item[0]
            })

        s = json.dumps(data)
        return s
    except Exception as e:
        print(e)
        return "Error occurred - try again"


if __name__ == "__main__":
    app.run(debug=True, port=5000)