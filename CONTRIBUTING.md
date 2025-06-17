# Contributing

Contributions are welcome, and they are greatly appreciated!

You can contribute in many ways:

# Types of Contributions

## Report Bugs

Report bugs at <https://github.com/carnall-farrar/cookiecutter-cf/issues

If you are reporting a bug, please include:

- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

## Fix Bugs

Look through the GitHub issues for bugs.
Anything tagged with "bug" and "help wanted" is open to whoever wants to implement a fix for it.

## Implement Features

Look through the GitHub issues for features.
Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

## Write Documentation

This package could always use more documentation, whether as part of the official docs or in docstrings.

## Submit Feedback

The best way to send feedback is to file an issue at <https://github.com/carnall-farrar/cookiecutter-cf/issues.

If you are proposing a new feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.

# Get Started!

Here's how to set up `cookiecutter-cf` for local development.
Please note this documentation assumes you already have `conda`, `uv`, and `git` installed and ready to go.

1. Clone the repo locally:

```bash
git clone https://github.com/carnall-farrar/cookiecutter-cf.git
```

2. Now we need to install the environment.
   Navigate into the project directory:

```bash
cd cookiecutter-cf
```

Create a conda virtual environment and install the necessary packages to run the project with one convenient `make` command:

```bash
make create_environment
```

4. Install pre-commit to run linters/formatters at commit time:

   uv run pre-commit install

5. Create a branch for local development:

```bash
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

6. Don\'t forget to add test cases for your added functionality to the `tests` directory.

7. When you\'re done making changes, check that your changes pass the formatting tests.

```bash
make check
```

8. Now, validate that all unit tests are passing:

```bash
make test
```

9. Before raising a pull request you should also run tox. This will run the tests across different versions of Python:

```bash
tox
```

This requires you to have multiple versions of Python installed.
This step is also triggered in the CI/CD pipeline, so you could also choose to skip this step locally.

10. Reflect your changes in the documentation. Update relevant files in the `docs` directory, and potentially the `README`.
    You can check the updated documentation with:

```bash
make docs
```

11. Commit your changes and push your branch to GitHub:

```bash
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

12. Submit a pull request through the GitHub website.

# Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add the feature to the list in README.rst.
