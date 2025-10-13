# Opinions

The default project structure reflects certain opinions about how to do collaborative data science work. These opinions grew out of our own experiences with what works and what doesn't. Some of these opinions are about workflows, and others are about tools that can make the process easier. These opinions are discussed below. If you have any thoughts, please [contribute or share them](contributing.md).

## 1. Data analysis is a directed acyclic graph

_Don't ever edit your raw data. Especially not manually. And especially not in Excel._

The most important features of a quality data analysis are correctness and reproducibility—anyone should be able to re-run your analysis using only your code and raw data and produce the same final products. The best way to ensure correctness is to test your analysis code. **The best way to ensure reproducibility is to treat your data analysis pipeline as a directed acyclic graph ([DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph))**. This means each step of your analysis is a node in a directed graph with no loops. You can run through the graph forwards to recreate any analysis output, or you can trace backwards from an output to examine the combination of code and data that created it.

### Raw data is immutable

That proper data analysis is a DAG means that **raw data must be treated as immutable**—it's okay to read and copy raw data to manipulate it into new outputs, but never okay to change it in place. This informs the design of the default `data/` directory subfolders in which data originates from `raw/`, intermediate analytical outputs get serialized or cached in `processed/`, and final products end up in `outputs/` (the number or names of these folders is less important than flow of data between them). 

Some **do**s and **don't**s that follow from treating data analysis as a DAG:

* ✅ **Do** write code that moves the raw data through a pipeline to your final analysis.
* ✅ **Do** serialize or cache the intermediate outputs of long-running steps.
* ✅ **Do** make it possible (and ideally, documented and automated) for anyone to reproduce your final data products with only the code in `{{cookiecutter.module_name}}` and the data in `data/raw/`.

* ⛔ **Don't** _ever_ edit your raw data, especially not manually, and _especially_ not in Excel. This includes changing file formats or fixing errors that might break a tool that's trying to read your data file.
* ⛔ **Don't** overwrite your raw data with a newly processed or cleaned version.
* ⛔ **Don't** save multiple versions of the raw data. 

### Data should (mostly) not be kept in source control

Another consequence of treating data as immutable is that data doesn't need source control in the same way that code does. Therefore, **by default, the `data/` folder is included in the `.gitignore` file.** If you have a small amount of data that rarely changes, you _may_ want to include the data in the repository. GitHub [currently](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#file-size-limits) warns you if files are over 50MB and rejects any files over 100MB. 

If you have larger amounts of data, consider storing and syncing with [Amazon S3](https://aws.amazon.com/s3/). [`awscli`](https://aws.amazon.com/cli/) is a syncing tool that can help you manage the data. Some examples:

There is also the [Git Large File Storage (LFS)](https://git-lfs.github.com/) extension which lets you track large files in git but stores the files on a separate server. GitHub provides [some storage compatible with Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage).

### Tools for DAGs

DAGs are so common in data and software processes that many tools have been built to manage them. We prefer [`make`](https://www.gnu.org/software/make/) for managing steps that depend on each other, especially the long-running ones. Make is a common tool on Unix-based platforms (and is available for Windows via [chocolatey](https://community.chocolatey.org/packages/make)). Following the [`make` documentation](https://www.gnu.org/software/make/), [Makefile conventions](https://www.gnu.org/prep/standards/html_node/Makefile-Conventions.html#Makefile-Conventions), and [portability guide](https://www.gnu.org/savannah-checkouts/gnu/autoconf/manual/autoconf-2.69/html_node/Portable-Make.html#Portable-Make) will help ensure your Makefiles work effectively across systems. Here are [some examples](https://blog.kaggle.com/2012/10/15/make-for-data-scientists/) to [get started](https://web.archive.org/web/20150206054212/https://www.bioinformaticszen.com/post/decomplected-workflows-makefiles/). A number of data folks use `make` as their tool of choice, including [Mike Bostock](https://bost.ocks.org/mike/make/).

There are other tools for managing DAGs that are written in Python, instead of their own language. Popular ones include [Airflow](https://airflow.apache.org/index.html), [Luigi](https://luigi.readthedocs.org/en/stable/index.html), [Snakemake](https://snakemake.readthedocs.io/en/stable/), [Prefect](https://github.com/PrefectHQ/prefect), [Dagster](https://github.com/dagster-io/dagster), and [Joblib](https://joblib.readthedocs.io/en/latest/memory.html). Feel free to use these if they are more appropriate for your analysis.

## 2. Notebooks are for exploration and communication, source files are for repetition

> Source code is superior for replicability because it is more portable, can be tested more easily, and is easier to code review.

[Jupyter Notebook](https://jupyter.org/) is very effective for exploratory data analysis because they enable rapid iteration and visualization of results. However, it can be less effective for reproducing an analysis. Source code is superior for replicability because it is more portable, can be tested more easily, and is easier to code review. 

Notebooks are to be stored exclusively in the `notebooks/` directory. When we use notebooks in our work, we often subdivide the `notebooks/` folder to keep things organized and legible. For example, `notebooks/exploratory/` contains initial explorations, whereas `notebooks/reports/` is more polished work that can be exported as html to the `reports/` directory. We also recommend that you follow a naming convention that shows the owner and the order the analysis was done in. We use the format `<step>-<ghuser>-<description>.ipynb` (e.g., `0.3-bull-visualize-distributions.ipynb`). Since notebooks are challenging objects for source control (e.g., diffs of the `json` are often not human-readable and merging is near impossible), we recommended not collaborating directly with others on Jupyter notebooks. We also recommend using a tool like [`nbautoexport`](https://github.com/drivendataorg/nbautoexport) to make reviewing changes to notebooks easier. 

### Refactor the good parts into source code 

Don't write code to do the same task in multiple notebooks. If it's a data preprocessing task, put it in the pipeline at `{{cookiecutter.module_name}}/data/make_dataset.py` and load data from `data/processed/`. If it's useful utility code, refactor it to `{{cookiecutter.module_name}}`. Classic signs that you are ready to move from a notebook to source code include duplicating old notebooks to start new ones, copy/pasting functions between notebooks, and creating object-oriented classes within notebooks.


## 3. Build from the environment up

The first step in reproducing an analysis is always replicating the computational environment it was run in. You need the same tools, the same libraries, and the same versions to make everything play nicely together.

Doing so in Python requires choosing and configuring an environment management tool. The ecosystem for this tooling has evolved a lot in recent years. 

For data science work, we prefer to use the **conda** package manager because it also manages non-Python packages, including system library dependencies that you often run into in data science. See the [Knowledge-Hub](https://github.com/carnall-farrar/knowledge-hub/blob/main/How-To/getting-setup.md#4-install-conda) for how to install conda.

If you have more complex requirements for recreating your environment, consider a virtual machine based approach such as [Docker](https://www.docker.com/). This tool uses a text-based format (Dockerfile) that you can easily add to source control to describe how to create a virtual machine with the requirements you need.

## 4. Keep secrets and configuration out of version control

You _really_ don't want to leak your AWS secret key on Github—see the [Twelve Factor App](https://12factor.net/config) principles on this point. Here's one way to do this:

### Store your secrets and config variables in a special file

Create a `.env` file in the project root folder. Thanks to the `.gitignore`, this file should never get committed into the version control repository. Here's an example:

```nohighlight
# example .env file
DATABASE_URL=postgres://username:password@localhost:5432/dbname
AWS_ACCESS_KEY=myaccesskey
AWS_SECRET_ACCESS_KEY=mysecretkey
OTHER_VARIABLE=something
```

### Use a package to load these variables automatically.

If you look at `{{cookiecutter.module_name}}/config.py`, it uses a package called [python-dotenv](https://github.com/theskumar/python-dotenv) to load up all the entries in this file as environment variables so they are accessible with `os.environ.get`. Here's an example snippet adapted from the `python-dotenv` documentation:

```python
# {{cookiecutter.module_name}}/data/dotenv_example.py
import os
from dotenv import load_dotenv, find_dotenv

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

database_url = os.environ.get("DATABASE_URL")
other_variable = os.environ.get("OTHER_VARIABLE")
```
