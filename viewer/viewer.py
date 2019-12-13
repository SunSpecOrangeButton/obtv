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
import re

from oblib import taxonomy, data_model, parser
from flask import Flask, request, render_template
from flask_cors import CORS

RETURN_INDEX = "<h2><a href='/html'>Return to search page</a></h2>"
tax = None

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)

TYPES = {
    "dei:legalEntityIdentifierItemType": "String",
    "nonnum:domainItemType": "String",
    "num-us:electricCurrentItemType":  "Float",
    "num-us:frequencyItemType": "Float",
    "num-us:insolationItemType": "Float",
    "num-us:irradianceItemType": "Float",
    "num-us:planeAngleItemType": "Float",
    "num-us:pressureItemType": "Float",
    "num-us:speedItemType": "Float",
    "num-us:temperatureItemType": "Float",
    "num-us:voltageItemType": "Float",
    "num:areaItemType": "Float",
    "num:energyItemType": "Float",
    "num:lengthItemType": "Float",
    "num:massItemType": "Float",
    "num:percentItemType": "Float",
    "num:powerItemType": "Float",
    "num:volumeItemType": "Float",
    "solar-types:DERItemType": "Enumeration",
    "solar-types:aLTASurveyItemType": "Enumeration",
    "solar-types:approvalRequestItemType": "Enumeration",
    "solar-types:approvalStatusItemType": "Enumeration",
    "solar-types:assetSecuredItemType": "Enumeration",
    "solar-types:batteryChemistryItemType": "Enumeration",
    "solar-types:batteryConnectionItemType": "Enumeration",
    "solar-types:climateClassificationKoppenItemType": "Enumeration",
    "solar-types:climateZoneANSIItemType": "Enumeration",
    "solar-types:communicationProtocolItemType": "Enumeration",
    "solar-types:creditSupportStatusItemType": "Enumeration",
    "solar-types:deviceItemType": "Enumeration",
    "solar-types:distributedGenOrUtilityScaleItemType": "Enumeration",
    "solar-types:divisionStateApprovalStatusItemType": "Enumeration",
    "solar-types:employeeLevelItemType": "Enumeration",
    "solar-types:employeeRoleItemType": "Enumeration",
    "solar-types:energyBudgetPhaseItemType": "Enumeration",
    "solar-types:eventSeverityItemType": "Enumeration",
    "solar-types:eventStatusItemType": "Enumeration",
    "solar-types:feeStatusItemType": "Enumeration",
    "solar-types:financialTransactionItemType": "Enumeration",
    "solar-types:financingEventItemType": "Enumeration",
    "solar-types:fundOrProjectItemType": "Enumeration",
    "solar-types:fundStatusItemType": "Enumeration",
    "solar-types:gISFileFormatItemType": "Enumeration",
    "solar-types:hedgeItemType": "Enumeration",
    "solar-types:insuranceItemType": "Enumeration",
    "solar-types:internetConnectionItemType": "Enumeration",
    "solar-types:inverterItemType": "Enumeration",
    "solar-types:inverterPhaseItemType": "Enumeration",
    "solar-types:investmentStatusItemType": "Enumeration",
    "solar-types:mORLevelItemType": "Enumeration",
    "solar-types:moduleItemType": "Enumeration",
    "solar-types:moduleOrientationItemType": "Enumeration",
    "solar-types:moduleTechnologyItemType": "Enumeration",
    "solar-types:mountingItemType": "Enumeration",
    "solar-types:occupancyItemType": "Enumeration",
    "solar-types:optimizerTypeItemType": "Enumeration",
    "solar-types:participantItemType": "Enumeration",
    "solar-types:preventiveMaintenanceTaskStatusItemType": "Enumeration",
    "solar-types:projectAssetTypeItemType": "Enumeration",
    "solar-types:projectClassItemType": "Enumeration",
    "solar-types:projectInterconnectionItemType": "Enumeration",
    "solar-types:projectPhaseItemType": "Enumeration",
    "solar-types:projectStageItemType": "Enumeration",
    "solar-types:regulatoryApprovalStatusItemType": "Enumeration",
    "solar-types:regulatoryFacilityItemType": "Enumeration",
    "solar-types:reserveCollateralItemType": "Enumeration",
    "solar-types:reserveUseItemType": "Enumeration",
    "solar-types:roofItemType": "Enumeration",
    "solar-types:roofSlopeItemType": "Enumeration",
    "solar-types:securityInterestItemType": "Enumeration",
    "solar-types:securityInterestStatusItemType": "Enumeration",
    "solar-types:siteControlItemType": "Enumeration",
    "solar-types:solarSystemCharacterItemType": "Enumeration",
    "solar-types:sparePartsStatusItemType": "Enumeration",
    "solar-types:sPVOrCounterpartyItemType": "Enumeration",
    "solar-types:systemAvailabilityModeItemType": "Enumeration",
    "solar-types:systemOperationalStatusItemType": "Enumeration",
    "solar-types:titlePolicyInsuranceItemType": "Enumeration",
    "solar-types:trackerItemType": "Enumeration",
    "solar-types:uuidItemType": "String",
    "solar-types:uuidXbrlItemType": "String",
    "solar-types:zoningPermitPropertyItemType": "Enumeration",
    "us-types:perUnitItemType": "String",
    "xbrli:anyURIItemType": "URI",
    "xbrli:booleanItemType": "Boolean",
    "xbrli:dateItemType": "Date",
    "xbrli:decimalItemType": "Float",
    "xbrli:durationItemType": "String",
    "xbrli:integerItemType": "Integer",
    "xbrli:monetaryItemType": "Float",
    "xbrli:normalizedStringItemType": "String",
    "xbrli:pureItemType": "String",
    "xbrli:stringItemType": "String"

}

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


@app.route('/conceptdetail/<concept>/<taxonomy>', methods=['GET'])
def concept_detail(concept, taxonomy):

    print("Concept detail endpoint")

    try:
        concept = taxonomy.lower() + ":" + concept

        details = tax.semantic.get_concept_details(concept)

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

        validation_rule = "None"
        t = TYPES[details.type_name]
        if t == "String":
            validation_rule = "Any String is valid"
        elif t == "Boolean":
            validation_rule = "Boolean values (TRUE or FALSE) are valid"
        elif t == "Integer":
            validation_rule = "Integer values (no decimal point) are valid"
        elif t == "Float":
            validation_rule = "Float values (with or without decimal point) are valid"
        elif t == "Enumeration":
            validation_rule = "Value must be one of the enumerated values listed below:"
        elif t == "URI":
            validation_rule = "Value must be a valid internet URI/URL format (but does not necessarily need to exist on the internet)"
        elif t == "UUID":
            validation_rule = "Value must be a valid UUID (xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx)"
        elif t == "LEI":
            validation_rule = "Value must be a 20 character LEI string"

        if t == "Enumeration":
            for e in tax.types.get_type_enum(details.type_name):
                pass

        precision_decimals = ""
        if details.type_name.startswith("num:") or details.type_name.startswith("num-us:"):
            precision_decimals = "Either Precision or Decimals must be specified"
        else:
            precision_decimals= "N/A (neither precision nor decimals may be specified)"

        units = []
        if details.type_name.startswith("num:") or details.type_name.startswith("num-us:"):
            if details.type_name in ["num:percentItemType"]:
                units.append("pure")
            else:
                for unit in tax.units.get_all_units():
                    ud = tax.units.get_unit(unit)
                    if details.type_name.lower().find(ud.item_type.lower()) != -1:
                        units.append(ud.unit_name)
        else:
            units.append("N/A (units may not be specified)</li>\n")

        period = details.period_type.value
        if period == "instant":
            period = "Instant in time"
        else:
            period = "Period of time"
        nillable = details.nillable

        if concept == "us-gaap:Revenues":
            calc = "Other Income + RebateRevenue + PeformanceBasedIncentiveRevenue + Electrical Generation Revenue = Revenues"
        else:
            calc = "N/A"

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
            "calculations": calc
        }

        s = json.dumps(data)
        return s

    except Exception as e:
        print(e)
        return "Error occurred - try again"


if __name__ == "__main__":
    app.run(debug=True, port=5000)