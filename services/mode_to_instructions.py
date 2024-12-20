# get the instructions for the mode
# read the instruction from the file
# the location of the file is in the modes/instructions folder
# the file is in markdown format
# return the instruction as a string
#

import os
from pathlib import Path

def mode_to_instructions(mode):
    instructions_path = Path(f"./modes/instructions/{mode}.md")
    if instructions_path.exists():
        with open(instructions_path, "r") as file:
            instructions = file.read()
            # make the instructions a string
            instructions = str(instructions)
            return instructions

