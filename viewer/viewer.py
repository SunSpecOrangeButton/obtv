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
import relationships

import json
import re

import werkzeug
from oblib import taxonomy
from flask import Flask, make_response, jsonify
from flask_cors import CORS

RETURN_INDEX = "<h2><a href='/html'>Return to search page</a></h2>"
tax = None

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)


"""Main Code - Start Flask"""
tax = taxonomy.Taxonomy()
app = Flask(__name__, static_url_path='', static_folder='dist')
CORS(app)
app.logger.setLevel(20)
app.logger.info("Initialization completed")
"""End of Main Code"""


@app.errorhandler(Exception)
def exception(e):
    """
    Handle All Exceptions here - typically Exceptions are program logic issues so there is little that can
    be returend other than an internal error has occured.  It is possible that the issue is a bad key passsed
    from the client side (KeyError) or some sort of HTTPException as well and these will be reflected.
    """

    app.logger.error(e)

    if isinstance(e, KeyError):
        response = make_response()
        response.data = json.dumps({
            "code": 404,
            "name": "404 Not Found",
            "description": str(e)
        })
        response.content_type = "application/json"
        return response
    elif isinstance(e, werkzeug.exceptions.HTTPException):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response
    else:
        response = make_response()
        response.data = json.dumps({
            "code": 500,
            "name": "500 Internal Server Error",
            "description": "An internal issue with the software occurred",
        })
        response.content_type = "application/json"
        return response


@app.route('/concepts/<entrypoint>', methods=['GET'])
def concepts(entrypoint):
    """Flask Read Handler for concepts API Endpoint"""

    if entrypoint == "none":
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
                    "itemtype": details.type_name.split(":")[1].replace("ItemType", ""),
                    "period": details.period_type.value
                })
    else:
        data = []
        entrypoint_concepts = []
        for concept in tax.semantic.get_entrypoint_concepts(entrypoint):
            entrypoint_concepts.append(concept)
        for concept in tax.semantic.get_all_concepts(details=True):
            if concept in entrypoint_concepts:
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
                        "itemtype": details.type_name.split(":")[1].replace("ItemType", ""),
                        "period": details.period_type.value
                    })

    return jsonify(data)


@app.route('/units/', methods=['GET'])
def units():
    """Flask Read Handler for units API Endpoint"""

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

    return jsonify(data)


@app.route('/types/', methods=['GET'])
def types():
    """Flask Read Handler for types API Endpoint"""

    data = []

    types = tax.types.get_all_types()
    numeric_types = tax.numeric_types.get_all_numeric_types()

    for name in tax.semantic.get_all_type_names():
        if name in types:
            values = ""
            first = True
            for e in tax.types.get_type_enum(name):
                if not first:
                    values += ", "
                first = False
                values += e
            data.append({
                "code": name.replace("solar-types:", "").replace("ItemType", ""),
                "type": reference.TYPE_MAPPINGS[name.split(":")[0]],
                "values": values,
                "definition": ""
            })
        elif name in numeric_types:
            data.append({
                "code": name.replace("num-us:", ""),
                "type": reference.TYPE_MAPPINGS[name.split(":")[0]],
                "values": "N/A",
                "definition": ""
            })
        else:
            data.append({
                "code": name.split(":")[1].replace("ItemType", ""),
                "type": reference.TYPE_MAPPINGS[name.split(":")[0]],
                "values": "N/A",
                "definition": ""
            })

    return jsonify(data)


@app.route('/entrypoints/', methods=['GET'])
def entrypoints():
    """Flask Read Handler for entrypoints API endpoint"""

    data = []
    for item in tax.semantic.get_all_entrypoints(details=True)[1].items():
        data.append({
            "entrypoint": item[1].name,
            "type": item[1].entrypoint_type.value,
            "description": item[1].description
        })

    return jsonify(data)


@app.route('/glossary/', methods=['GET'])
def glossary():
    """Flask Read Handler for glossary API Endpoint"""

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

    return jsonify(data)


@app.route('/conceptdetail/<concept>/<taxonomy>', methods=['GET'])
def concept_detail(concept, taxonomy):

    concept = taxonomy.lower() + ":" + concept

    details = tax.semantic.get_concept_details(concept)
    if not details:
        raise KeyError('Concept {} not found'.format(concept))

    label = convert(details.name)

    taxonomy = "SOLAR"
    if details.id.startswith("us-gaap:"):
        taxonomy = "US-GAAP"
    elif details.id.startswith("dei:"):
        taxonomy = "DEI"

    entrypoints = []
    for entrypoint in tax.semantic.get_all_entrypoints():
        if entrypoint != "All":
            if concept in tax.semantic.get_entrypoint_concepts(entrypoint):
                entrypoints.append(entrypoint)

    docs = tax.documentation.get_concept_documentation(concept)
    if docs is None:
        docs = "None"

    item_type = details.type_name.split(":")[1].replace("ItemType", "")

    t = reference.TYPES[details.type_name]
    if t in reference.VALIDATION_RULES:
        validation_rule = reference.VALIDATION_RULES[t]
    else:
        validation_rule = "None"

    if t == "Enumeration":
        for e in tax.types.get_type_enum(details.type_name):
            pass

    if details.type_name.startswith("num:") or details.type_name.startswith("num-us:"):
        precision_decimals = "Either Precision or Decimals must be specified"
    else:
        precision_decimals= "N/A (neither precision nor decimals may be specified)"

    units = tax.get_concept_units(concept)
    if not units:
        units = ["N/A (units are not specified)"]

    period = details.period_type.value
    if period == "instant":
        period = "Instant in time"
    else:
        period = "Period of time"
    nillable = details.nillable

    calculations = tax.semantic.get_concept_calculation(concept)
    if len(calculations)==0:
        calc = ["N/A"]
    else:
        calc = []
        for calculation in calculations:
            if calculation[1] == 1:
                sign = "+"
            else:
                sign = "-"
            calc.append(sign + " " + calculation[0])

    usages = tax.semantic.get_concept_calculated_usage(concept)
    if len(usages) == 0:
        usages = ["None"]

    data = {
        "label": label,
        "taxonomy": taxonomy,
        "entrypoints": entrypoints,
        "description": docs,
        "type": item_type,
        "validationRule": validation_rule,
        "precisionDecimals": precision_decimals,
        "units": units,
        "period": period,
        "nillable": nillable,
        "calculations": calc,
        "usages": usages
    }

    return jsonify(data)


@app.route('/entrypointdetail/<entrypoint>/undefined', methods=['GET'])
def entrypoint_detail(entrypoint):

    r = relationships.create_json(entrypoint)
    if len(r) < 1:
        raise KeyError('Entrypoint {} not found'.format(entrypoint))
    data = relationships.create_json(entrypoint)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)