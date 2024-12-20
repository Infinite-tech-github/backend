import json
import os
from utils.file_operations import get_files, read_file, save_json_file
from config.settings import INSTRUCTIONS_DIR, SECTION_FILE_EXT
from ai.ai_operations import call_ai

def modeGenerator(model, prompt):
    print("modeGenerator")
    modes = get_files(INSTRUCTIONS_DIR)
    print(modes)

    mode_list = json.dumps(modes)

    # get the mode_selector.md content
    filePath = INSTRUCTIONS_DIR + "/mode_selector.md"
    mode_selector_instructions = read_file(filePath)

    # remove the mode_selector.md content from the mode_list
    mode_list = mode_list.replace("mode_selector.md", "")
    # combine the mode_selector.md content with the mode_list
    prompt_instructions = mode_selector_instructions + mode_list.replace(
        ".md", ""
    )


    #  add the prompt to the prompt_instructions 
    prompt_instructions = prompt_instructions + "\n Prompt: '" + prompt + "'"

    # generate the content
    # def call_ai(model, prompt, stop_sequences, imagePath=None):
    stop_sequences = ["```"]
    response = call_ai(model, prompt_instructions, stop_sequences)

    print(response)
    try:
        json_response = json.loads(response)
        print(json_response)
    except:
        json_response = response

    return json_response

