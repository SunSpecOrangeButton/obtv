#! /bin/bash

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

rm -rf resources
rm -rf dist
rm -rf web-build
mkdir resources
cd viewer
python3.7 generate_static_site.py
cd ..
cp -r web web-build
cd web-build
rm resources/*
cp ../resources/* resources
rm package-lock.json
rm -rf node_modules
npm install
npm run-script build
cd ..
mkdir dist
mv web-build/dist dist/orange-button-taxonomy-viewer
rm -rf resources
rm -rf web-build
