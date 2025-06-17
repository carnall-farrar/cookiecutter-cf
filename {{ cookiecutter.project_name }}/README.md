# {{cookiecutter.project_name}}

[![Python Version](https://img.shields.io/badge/python-3.8%7C3.9%7C3.10%7C3.11-blue?style=for-the-badge&logo=python)](pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://www.mkdocs.org/)
[![Cookiecutter-CF](https://img.shields.io/badge/Cookiecutter--CF-red?style=plastic)](https://github.com/carnall-farrar/cookiecutter-cf/)


{{cookiecutter.description}}

## Project Context/Background

_Comprehensively detail the project context here._

## Repository Organization

```
├── Makefile                    <- Makefile with convenience commands
├── README.md                   <- The top-level README for developers using this project.
├── data
│   ├── output                  <- The final, canonical data sets.
│   ├── processed               <- Intermediate data that has been transformed.
│   └── raw                     <- The original, immutable data dump.
│
├── docs                        <- A default mkdocs project; see www.mkdocs.org for details
│
├── pyproject.toml              <- Project configuration file with package metadata for 
│                                  {{ cookiecutter.module_name }} and configuration for tools like black
│
├── .pre-commit-config.yaml     <- Hooks that run prior to a git commit command
│ 
├── mkdocs.yml                  <- Configuration file for the mkdocs project
│
├── figures                     <- Generated graphics and figures to be used in reporting
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

--------

