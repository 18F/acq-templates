#!/usr/bin/env bash

# Python distribution
#
## Get dependencies
if type pip; then
  pip install pypandoc inflection
fi

## Build distribution and upload to PyPI
## https://packaging.python.org/distributing/
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*

# Node distribution
#
## Publish to NPM
# TODO: add package.json
# npm publish

# Ruby distribution
#
## TODO: gem stuff
