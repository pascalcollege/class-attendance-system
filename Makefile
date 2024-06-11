prebuild:
    export PYTHONPATH=$PYTHONPATH:$(pwd)

configure:
	poetry install

build:
	poetry build

api: prebuild
	python classattendance/api/app.py

ui :
	python ui.py

test:
	python -m unittest tests.py

clean:
	rm -rf __pycache__ *.pyc

.PHONY: api clean test ui build configure
