#!/bin/zsh

PY_DIR='build/python/lib/python3.6/site-packages'
mkdir -p $PY_DIR
pip install -r requirements_aws.txt -t $PY_DIR