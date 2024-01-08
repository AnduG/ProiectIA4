PYTHON = python3
PIP = pip3
FLASK_APP = app
FLASK_RUN = $(PYTHON) -m flask --app $(FLASK_APP) run
REQUIREMENTS_FILE = requirements.txt

# Targets and Rules
.PHONY: setup run clean

setup:
	$(PIP) install -r $(REQUIREMENTS_FILE)

run-local:
	$(FLASK_RUN)

run-network:
	$(FLASK_RUN) --host=0.0.0.0
