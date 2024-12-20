from datetime import datetime
from pathlib import Path
import os
import json


def save_section(response):
    file_path = f"./generated/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.json"
    
    with open(file_path, "w") as file:
        file.write(json.dumps(response))

    return file_path