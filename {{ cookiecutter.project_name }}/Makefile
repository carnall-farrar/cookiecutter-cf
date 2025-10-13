#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = {{cookiecutter.project_name}}
PYTHON_VERSION = 3.10
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

###     DEV COMMANDS

## Set up Python interpreter environment
.PHONY: create_environment
create_environment:
	@echo "🚀 Creating a virtual environment using conda"
	conda create --name $(PROJECT_NAME) python=$(PYTHON_VERSION) -y
	@echo ">>> A conda environment named $(PROJECT_NAME) has been created"
	conda activate $(PROJECT_NAME)
	uv pip compile pyproject.toml -o requirements.txt
	uv pip install -r requirements.txt
	pre-commit install

## Install Python dependencies
.PHONY: requirements
requirements:
	uv pip compile pyproject.toml -o requirements.txt
	uv pip install -r requirements.txt
	pre-commit install

## Lint using ruff (use `make format` to do formatting)
.PHONY: lint
lint:
	ruff format --check
	ruff check

## Format source code with ruff
.PHONY: format
format:
	ruff check --fix
	ruff format

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

dist: clean ## builds source and wheel package
	python -m build
	ls -l dist

###     TESTS

## Run tests
.PHONY: test
test:
	python -m pytest --cov --cov-config=pyproject.toml

###     DOCS

## Test if documentation can be built without warnings or errors
.PHONY: docs-test
docs-test:
	cd docs && mkdocs build -s

## Build and serve the documentation
.PHONY: docs
docs:
	cd docs && mkdocs serve


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
