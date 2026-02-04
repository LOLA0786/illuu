.PHONY: lint fmt test precommit

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
