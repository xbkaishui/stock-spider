rm -rf dist/*
python setup.py sdist build
twine upload dist/*