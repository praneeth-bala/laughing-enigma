VENV := .venv
INSTALL_STAMP := $(VENV)/.install.stamp
PYTHON := $(VENV)/bin/python

$(PYTHON):
	python3 -m venv $(VENV)

install: $(PYTHON) requirements.txt
	$(PYTHON) -m pip install -r requirements.txt

server:
	$(PYTHON) ./maldetect/manage.py runserver