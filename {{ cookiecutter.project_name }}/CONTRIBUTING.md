# Contributing

Here's how to set up `{{cookiecutter.project_name}}` for local development.
Please note this documentation assumes you already have `conda`, `uv`, and `git` installed and ready to go.

1. Clone the repo locally:

```bash
git clone https://github.com/carnall-farrar/{{cookiecutter.project_name}}.git
```

2. Now we need to install the environment.
   Navigate into the project directory:

```bash
cd {{cookiecutter.project_name}}
```

Create a conda virtual environment and install the necessary packages to run the project with one convenient `make` command:

```bash
make create_environment
```

5. Create a branch for local development (always branch from `dev`, or another feature branch. Never `main`):

```bash
git checkout dev
git pull
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

6. Don't forget to add test cases for your added functionality to the `tests` directory.

7. When you're done making changes, check that your changes pass the formatting tests.

```bash
make format
```

8. Now, validate that all unit tests are passing:

```bash
make test
```

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

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds or changes functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add the feature to the list in README.rst.
