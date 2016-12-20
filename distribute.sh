#!/usr/bin/env bash

# Python distribution
#
## First, create the bonus Django template folders
mkdir -p acq_templates/templates/acq_templates
pushd acq_templates/templates/acq_templates
ln -s ../../../agile_bpa .
ln -s ../../../micropurchase .
ln -s ../../../consulting .

## Build distribution and upload to PyPI
## https://packaging.python.org/distributing/
popd
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*

# Node distribution
#
## Publish to NPM
# TODO: add package.json
npm publish

# Ruby distribution
#
## TODO: gem stuff
