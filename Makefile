.PHONY: setup lint fmt test precommit

setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	.venv/bin/pip install -r requirements-dev.txt
	.venv/bin/pre-commit install

fmt:
	black .
	isort .

lint:
	flake8 .
	mypy .

precommit:
	pre-commit install


test:
	python -m compileall .
	pipreqs --use-local --diff requirements.txt .
	pytest -q
