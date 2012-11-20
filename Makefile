VIRTUALENV_FOLDER=env
PIP_BIN=$(VIRTUALENV_FOLDER)/bin/pip
PYTHON_BIN=$(VIRTUALENV_FOLDER)/bin/python


all: reqirements

environment:
	test -d "$(VIRTUALENV_FOLDER)" || virtualenv --no-site-packages $(VIRTUALENV_FOLDER)

reqirements: environment
	$(PIP_BIN) install -r requirements.txt

test: reqirements
	$(PYTHON_BIN) skeleton/tests.py
