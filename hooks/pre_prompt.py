import json
from datetime import date
from pathlib import Path


with Path("cookiecutter.json") as config:
    data = json.loads(config.read_text())
    
    # Set the initial version to today's date
    data["version"] = date.today().strftime("%Y.%m.%d")
    
    config.write_text(json.dumps(data, indent=4))