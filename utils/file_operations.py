import os
import json
import requests
from datetime import datetime
from config.settings import SAVE_FOLDER

def get_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
        
def save_json_file(file_path, data,name):
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)
    with open(os.path.join(SAVE_FOLDER, file_path), "w") as file:
        json.dump(data, file, indent=2)
