# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import unittest
from viewer import viewer

class TestViewer(unittest.TestCase):

    def test_entrypoints(self):
        data = json.loads(viewer.entrypoints())
        self.assertEqual(161, len(data))
        self.assertTrue("entrypoint" in data[0])
        self.assertTrue("type" in data[0])
        self.assertTrue("description" in data[0])

    def test_concepts(self):
        data = json.loads(viewer.concepts())
        self.assertEqual(3404, len(data))
        self.assertTrue("name" in data[0])
        self.assertTrue("taxonomy" in data[0])
        self.assertTrue("datatype" in data[0])
        self.assertTrue("period" in data[0])

    def test_types(self):
        data = json.loads(viewer.types())
        self.assertEqual(80, len(data))
        self.assertTrue("code" in data[0])
        self.assertTrue("type" in data[0])
        self.assertTrue("values" in data[0])
        self.assertTrue("definition" in data[0])

    def test_units(self):
        data = json.loads(viewer.units())
        self.assertEqual(296, len(data))
        self.assertTrue("id" in data[0])
        self.assertTrue("name" in data[0])
        self.assertTrue("symbol" in data[0])
        self.assertTrue("type" in data[0])
        self.assertTrue("standard" in data[0])
        self.assertTrue("definition" in data[0])

    def test_references(self):
        data = json.loads(viewer.references())
        self.assertEqual(305, len(data))
        self.assertTrue("type" in data[0])
        self.assertTrue("code" in data[0])
        self.assertTrue("definition" in data[0])