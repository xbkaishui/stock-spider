#!/usr/bin/env bash
rm -rf dist/*
python setup.py sdist build
twine upload dist/*