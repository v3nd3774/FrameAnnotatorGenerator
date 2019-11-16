#!/bin/bash
set -x
rm -rf dist/
old_num=`perl -ne "print if s/.+version=\"\d\.\d\.(\d)\".+/\1/g" setup.py`
export new_num=`expr $old_num + 1`
perl -i'' -pe 's/(.*?version=\"\d\.\d\.)\d(\"..*?)/\1$ENV{new_num}\2/g' setup.py
python setup.py sdist bdist_wheel
twine upload -r testpypi dist/* -u $1 -p $2
