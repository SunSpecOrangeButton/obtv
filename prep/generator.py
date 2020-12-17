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
This allows OBTV to be generated for the Vue.js code.  The data is generated from pyoblib and the output
is in Python lists/dictionaries that can be externalized to JSON.
"""

import reference
import relationships

import re

from oblib import taxonomy
from flask import jsonify

tax = taxonomy.Taxonomy()

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)


def concepts(entrypoint):
    """Generates concepts data"""

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
        for concept in tax.semantic.get_entrypoint_concepts(entrypoint).sort():
            entrypoint_concepts.append(concept)
        for concept in tax.semantic.get_all_concepts(details=True).sort():
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

    return data


def units():
    """Generates units data"""

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

    return data


def types():
    """Generates types data"""

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

    return sorted(data, key=lambda x: x["code"].lower())


def entrypoints():
    """Generates entrypoints data"""

    # TODO: This code is a workaround for an issue in solar-taxonomy (and perhaps pyoblib) that
    # the Monitoring Entrypoint has not metadata.  Thus there is one extra entrypoint in the non-detailed
    # list which must (at least until the next taxonomy release) be included.  After this occurs the code
    # can be shortened to just use entrypoint_details.
    data = []
    entrypoints, entrypoints_details = tax.semantic.get_all_entrypoints(details=True)
    for entrypoint in entrypoints:
        if entrypoint in entrypoints_details:
            data.append({
                "entrypoint": entrypoints_details[entrypoint].name,
                "type": entrypoints_details[entrypoint].entrypoint_type.value,
                "description": reference.ENTRYPOINTS_DESCRIPTION[entrypoint]
            })
        else:
            description = ""
            if entrypoint in reference.ENTRYPOINTS_DESCRIPTION:
                description = reference.ENTRYPOINTS_DESCRIPTION[entrypoint]
            data.append({
                "entrypoint": entrypoint,
                "type": "Documents",
                "description": description
            })

    return sorted(data, key=lambda x: x["entrypoint"])


def glossary():
    """Generates glossary data"""

    data = []
    for item in sorted(reference.ACRONYMS.items()):
        data.append({
            "type": "Acronym",
            "code": item[1],
            "definition": item[0]
        })

    for item in sorted(reference.ABBREVIATIONS.items()):
        data.append({
            "type": "Abbreviation",
            "code": item[1],
            "definition": item[0]
        })

    return data


def concept_detail(concept, taxonomy):
    """Generates concept_detail data"""

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

    return data


def entrypoint_detail(entrypoint):
    """Generates entrypoint detail data"""

    r = relationships.create_json(entrypoint)
    if len(r) < 1:
        raise KeyError('Entrypoint {} not found'.format(entrypoint))
    data = relationships.create_json(entrypoint)

    return data


