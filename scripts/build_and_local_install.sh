#!/bin/bash
set -x
rm -rf dist/
python setup.py sdist bdist_wheel
pip uninstall -y -q -q -q frame-annotator-generator-v3nd3774
pip install dist/*.whl
