import json
import os
from ai.generate_content import generate_content
from utils.file_operations import read_file, save_json_file
from config.settings import INSTRUCTIONS_DIR, SECTION_FILE_EXT


def contentGenerator(model, title, mode, instructions, past_sections,imagePath = None):
    content = generate_content(model, title, mode, instructions, past_sections,imagePath)
    try:
        section = {"title": title, "mode": mode, "content": content[0], "prompt":content[1]}
        return content

    except json.JSONDecodeError:
        return content
        
        