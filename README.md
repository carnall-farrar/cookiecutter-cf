# Cookiecutter CF

_A template for setting up GitHub repositories for CF projects._

[![Python Version](https://img.shields.io/badge/python-3.8%7C3.9%7C3.10%7C3.11-blue?style=for-the-badge&logo=python)](pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://www.mkdocs.org/)


This repository provides a standardized template for setting up data science projects at CF, incorporating our best practices in project structure, documentation, and tooling.
It uses [Cookiecutter](https://github.com/cookiecutter/cookiecutter) — a CLI (Command Line Interface) utility that generates project scaffolding based on a defined template. The template leverages the [Jinja2 templating engine] (https://jinja.palletsprojects.com/en/stable/intro/) to customize folder names, file names, and content based on user input, enabling teams to quickly spin up consistent and well-structured repositories.

## Getting Started

To generate a new project using this template, you’ll need the `Cookiecutter` CLI. We recommend using `uvx` which automatically sets up an isolated environment with all required dependencies and runs Cookiecutter with the correct configuration. `uvx` is a command from `uv`, more info on which is in [the DI Knowledge Hub]().

```bash
uvx cookiecutter https://github.com/carnall-farrar/cookiecutter-cf.git
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the README.md to complete the setup of your project.


### The resulting directory structure

The directory structure of your new project will look like this:

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── output        <- The final, canonical data sets.
│   ├── processed      <- Intermediate data that has been transformed.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         {{ cookiecutter.module_name }} and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src
    └── {{ cookiecutter.module_name }}   <- Source code for use in this project.
        │
        ├── __init__.py             <- Makes {{ cookiecutter.module_name }} a Python module
        │
        ├── config.py               <- Store useful variables and configuration
        │
        ├── utilities.py            <- Useful utilities
        │
        └── foo.py                  <- Dummy script
```


## Acknowledgements

This project is partially based on the following templates:

- Florian Maas' [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv)
- [CCDS](https://github.com/drivendataorg/cookiecutter-data-science)