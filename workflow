python setup.py sdist bdist_wheel
pip install --index-url https://test.pypi.org/project/ --no-deps code-secret
twine upload --verbose  -u <USERNAME> -p <PASSWORd> dist/*
