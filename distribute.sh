#!/usr/bin/env bash

# Python distribution
#
## Get dependencies
if type pip; then
  pip install pypandoc
fi
## Convert camelcase into underscore
if sed --version; then
  # We need GNU sed rather than the OSX default, and helpfully GNU sed is the
  # one of the two that has a --version flag
  sed -E 's/ buy\.(.+)([A-Z][a-z]+) / \1_\L\2 /g' */*.md
fi
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
