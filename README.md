# Cookiecutter CF

_A template for setting up GitHub repositories for CF projects._

[![Python Version](https://img.shields.io/badge/python-3.8%7C3.9%7C3.10%7C3.11-blue?style=for-the-badge&logo=python)](pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://www.mkdocs.org/)


This repository provides a standardized template for setting up data science projects at CF, incorporating our best practices in project structure, documentation, and tooling.
It uses [Cookiecutter](https://github.com/cookiecutter/cookiecutter) — a CLI (Command Line Interface) utility that generates project scaffolding based on a defined template. The template leverages the [Jinja2 templating engine] (https://jinja.palletsprojects.com/en/stable/intro/) to customize folder names, file names, and content based on user input, enabling users to quickly spin up consistent and well-structured repositories.

## Getting Started

To generate a new project using this template, you’ll need the `Cookiecutter` CLI. We recommend using `uvx` which automatically sets up an isolated environment with all required dependencies and runs Cookiecutter with the correct configuration. `uvx` is a command from `uv`, more info on which is in [the DI Knowledge Hub]().

### Step 1: Install uv

To start, we will need to install `uv`. The instructions to install uv can be found
[here](https://docs.astral.sh/uv/#getting-started). For MacOS or Linux;

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

or through Homebrew

```bash
brew install uv
```

## Step 2: Generate your project

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/carnall-farrar/cookiecutter-cf.git
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created.



### The resulting directory structure

The directory structure of your new project will look like this:

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
│                                  {{cookiecutter.module_name}} and configuration for tools like black
│
├── .pre-commit-config.yaml     <- Hooks that run prior to a git commit command
│ 
├── mkdocs.yml                  <- Configuration file for the mkdocs project
│
├── figures                     <- Generated graphics and figures to be used in reporting
│
└── src
    └── {{cookiecutter.module_name}}   <- Source code for use in this project.
        │
        ├── __init__.py             <- Makes {{cookiecutter.module_name}} a Python module
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