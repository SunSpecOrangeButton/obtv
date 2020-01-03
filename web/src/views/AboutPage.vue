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
    <div class="about">
        <br/>
        <br/>
        <center>
            <p>
                <img src="@/assets/tv.png" alt="OBTV"/>
            </p>
            <table width="95%">
                <tr>
                    <td>
                        <p>
                            Orange Button is an open data exchange standard for the distributed solar PV industry. Comprising
                            information models, a standard taxonomy, a standard Application Program Interface (API), and supporting
                            compliance test suites, Orange Button enables the free flow of data between information systems used in
                            the solar asset lifecycle to decrease long term costs and increase innovation.
                        </p>
                        <p>
                            Orange Button is powered by XBRL. XBRL is a global open data standard that renders information machine-readable
                            and improves ability to communicate and exchange business information. These communications are defined by
                            metadata set out in taxonomies, which define individual reporting concepts as well as the relationships
                            between concepts and other semantic meaning.
                        </p>
                        <p>
                            The Orange Button Taxonomy Viewer allows for searching and displaying Orange Button Entrypoints, Concepts, Types,
                            and Units by non-XBRL Experts. XBRL Experts may prefer using XBRL desktop software such as
                            the open source <a href="http://arelle.org/arelle/">Arelle</a> software which fully exposes the
                            XBRL syntax.
                        </p>
                        <p>
                            The following screens are available in OBTV:
                        </p>
                    </td>
                </tr>
            </table>
            <table width="90%">
                <tr>
                    <td valign="top"><b>Entrypoints:</b></td>
                    <td>
                        A taxonomy entry point identifies a subset (or "view") of a taxonomy. An entry point contains
                        a set of concepts (concepts may be present in multiple entrypoints) grouped into Abstracts and
                        Tables.
                    </td>
                </tr>
                <tr>
                    <td valign="top"><b>Concepts:</b></td>
                    <td>
                        A taxonomy element that provides the meaning for a fact. For example, "Profit", "Turnover", and
                        "Assets" would be typical concepts. Please note that although XBRL contains Abstract Concepts
                        (concepts that do not have facts) they are not displayed as Concepts in OBTV (use XBRL Desktop
                        Software to display instead) but rather indirectly reflected in the Entrypoint hierarchies in
                        order to simplify concept display for business users.
                    </td>
                </tr>
                <tr>
                    <td valign="top"><b>Types:</b></td>
                    <td>
                        Item Types may be a simple data type (String, Integer, ...) but also may also may be more specific
                        (Monetary, Energy, ...) for various concepts. All concepts have an Item Type.
                    </td>
                </tr>
                <tr>
                    <td valign="top"><b>Units:</b></td>
                    <td>Units of measurement may be assigned to certain concepts. Units are required for certain numeric
                        facts.  For example, monetary units must have an associated currency, such as US dollars (USD).
                    </td>
                </tr>
                <tr>
                    <td valign="top"><b>Glossary</b></td>
                    <td>Acronyms and Abbreviations used to shorten Orange Button Concepts.</td>
                </tr>
            </table>
        </center>

    </div>
</template>
