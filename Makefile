SHELL := /bin/bash

PYTHON := python3
VENV := venv
ACTIVATE := source $(VENV)/bin/activate

setup: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	@bash -c "$(ACTIVATE) && pip install -r requirements.txt"
	@echo "Setup complete. To activate the environment, use 'make activate'."

activate:
	@echo "To activate the virtual environment, use: 'source $(VENV)/bin/activate'"

install:
	@bash -c "$(ACTIVATE) && pip install -r requirements.txt"

run:
	@bash -c "$(ACTIVATE) && python3 setup_nginx.py"

clean:
	rm -rf $(VENV)
	@echo "Environment cleaned."
