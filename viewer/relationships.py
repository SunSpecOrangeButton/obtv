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
Builds JSON relationships which can be returned by the viewer to OBTV.
"""

from oblib import taxonomy
from dataclasses import dataclass
from typing import List


@dataclass
class Child(object):
    pass


@dataclass
class Table(object):

    name: str
    pks: List[str]
    pk_values_enum: List[List[str]]
    members: List[str]
    children: List[Child]


@dataclass
class Abstract(Child):

    name: str
    members: List[str]
    tables: List[Table]
    children: List[Child]


@dataclass
class OB(object):

    abstracts: List[Abstract]
    tables: List[Table]


tax = taxonomy.Taxonomy()

def abstract_relationships(entrypoint, abstracts):

    relationships = tax.semantic.get_entrypoint_relationships(entrypoint)
    if relationships is None:
        print("Entry Point command line argument does not exist in Taxonomy.")
        return []

    for r in relationships:
        f = r.from_.split(":")[1]
        t = r.to.split(":")[1]
        if f.endswith("Abstract") and t.endswith("Abstract"):
            parent = None
            child = None
            for item in abstracts.items():
                if item[1].name == f.replace("Abstract", ""):
                    parent = item[1]
                if item[1].name == t.replace("Abstract", ""):
                    child = item[1]
            if parent.children:
                parent.children.append(child)
            else:
                parent.children = [child]


def table_relationships(entrypoint, abstracts):

    relationships = tax.semantic.get_entrypoint_relationships(entrypoint)
    if relationships is None:
        print("Entry Point command line argument does not exist in Taxonomy.")
        return []

    for r in relationships:
        f = r.from_.split(":")[1]
        t = r.to.split(":")[1]
        if f.endswith("LineItems") and t.endswith("Abstract"):
            parent = None
            child = None
            for item in abstracts.items():
                if item[1].tables:
                    for table in item[1].tables:
                        # TODO: Fix brittle code which assumes that LineItems and Table name is always identically prefixed
                        # This is the cause of the warning: "Warning - parent/child relationship not found"
                        if table.name == f.replace("LineItems", ""):
                            parent = table
                            break

                        # for member in table.members:
                        #     if member == f.replace("LineItems", ""):
                        #         parent = table
                        #         break
            for item in abstracts.items():
                if item[1].name == t.replace("Abstract", ""):
                    child = item[1]

            if not parent or not child:
                print("  Warning - parent/child relationship not found", parent, child)
            else:
                if parent.children:
                    parent.children.append(child)
                else:
                    parent.children = [child]


def create_abstracts(entrypoint):

    relationships = tax.semantic.get_entrypoint_relationships(entrypoint)
    if relationships is None:
        print("Entry Point command line argument does not exist in Taxonomy.")
        return []

    if len(relationships) < 1:
        concepts = tax.semantic.get_entrypoint_concepts(entrypoint)
        name = ""
        members = []
        for concept in concepts:
            if concept.endswith("Abstract"):
                name = concept.split(":")[1].replace("Abstract", "")
            else:
                members.append(concept.split(":")[1])
        return {name: Abstract(name, members, None, None)}

    abstracts = {}
    last_abstract = None
    last_table = None
    pk_count = -1
    for r in relationships:
        f = r.from_.split(":")[1]
        t = r.to.split(":")[1]
        if r.role.value == "domain-member" and f.endswith("Abstract"):
            name = f.replace("Abstract", "")
            if name in abstracts:
                if not t.endswith("LineItems"):
                    abstracts[name].members.append(t)
                last_abstract = abstracts[name]
            else:
                if t.endswith("LineItems"):
                    abstracts[name] = Abstract(name, [], None, None)
                else:
                    abstracts[name] = Abstract(name, [t], None, None)
                last_abstract = abstracts[name]
        elif r.role.value == "domain-member" and f.endswith("LineItems"):
            last_table.members.append(t.replace("Abstract", "(A)"))
        elif r.role.value == "domain-member" and f.endswith("Domain"):
            if last_table.pk_values_enum == None:
                last_table.pk_values_enum = [[]]
                for i in range(1, pk_count+1):
                    last_table.pk_values_enum.append([])
            last_table.pk_values_enum[pk_count].append(t.replace("Member", ""))
        elif r.role.value == "all":
            if last_abstract.tables == None:
                last_abstract.tables = []
            last_table = Table(t.replace("Table", ""), [], None, [], None)
            last_abstract.tables.append(last_table)
            pk_count = -1
        elif r.role.value == "dimension-domain":
            pass
        elif r.role.value == "hypercube-dimension":
            last_table.pks.append(t.replace("Axis", ""))
            pk_count += 1
            if last_table.pk_values_enum:
                last_table.pk_values_enum.append([])

    abstract_relationships(entrypoint, abstracts)
    table_relationships(entrypoint, abstracts)

    return abstracts

def create_json(entrypoint):
    abstracts = create_abstracts(entrypoint)
    j = {}
    for key in abstracts:
        subprocess(abstracts[key], 1, j)
        break
    return j

def subprocess(a, level, j):
    j["name"] = a.name
    if a.members:
        j["members"] =  a.members
    if a.tables:
        t = []
        for table in a.tables:
            data = []
            i = 0
            for pk in table.pks:
                if table.pk_values_enum and table.pk_values_enum[i]:
                    data.append({"name": pk, "purpose": "PK", "valuesenum": table.pk_values_enum[i]})
                else:
                    data.append({"name": pk, "purpose": "PK"})
                i += 1
            for member in table.members:
                if member.endswith("(A)"):
                    data.append({"name": member.replace("(A)", ""), "purpose": "Abstract"})
                else:
                    data.append({"name": member, "purpose": "Data Element"})
            tt = {
                "name": table.name,
                "columns": data
            }
            if table.children:
                tt["children"] = []
                for c in table.children:
                    if c is not None:
                        jj = {}
                        subprocess(c, level + 1, jj)
                        tt["children"].append(jj)
            t.append(tt)
        j["tables"] = t

    if a.children:
        j["children"] = []
        for c in a.children:
            if c is not None:
                jj = {}
                subprocess(c, level+1, jj)
                j["children"].append(jj)