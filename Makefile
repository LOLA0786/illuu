PYTHON := $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)
PIP := $(if $(wildcard .venv/bin/pip),.venv/bin/pip,pip3)
PRECOMMIT := $(if $(wildcard .venv/bin/pre-commit),.venv/bin/pre-commit,pre-commit)

.PHONY: setup lint fmt test precommit

setup:
	python3 -m venv .venv
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt
	$(PRECOMMIT) install

fmt:
	black .
	isort .

lint:
	flake8 .
	mypy .

precommit:
	pre-commit install


test:
	$(PYTHON) -m compileall .
	pipreqs --use-local --diff requirements.txt .
	pytest -q
