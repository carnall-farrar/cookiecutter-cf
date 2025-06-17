#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = {{cookiecutter.project_name}}
PYTHON_VERSION = 3.10
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

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

## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

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

## Run tests
.PHONY: test
test:
	python -m pytest --cov --cov-config=pyproject.toml

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
