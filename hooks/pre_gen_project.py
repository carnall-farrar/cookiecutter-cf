from __future__ import annotations

import re
import sys

PROJECT_NAME_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"
project_name = "{{cookiecutter.project_name}}"
if not re.match(PROJECT_NAME_REGEX, project_name):
    print(
        f"ERROR: The project name {project_name} is not valid. Please do not use a _ and use - instead."
    )
    # Exit to cancel project
    sys.exit(1)

PROJECT_SLUG_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{cookiecutter.module_name}}"
if not re.match(PROJECT_SLUG_REGEX, module_name):
    print(
        f"ERROR: {module_name} is not a valid Python module name. Please do not use a - and use _ instead."
    )
    # Exit to cancel project
    sys.exit(1)
