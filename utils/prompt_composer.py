import json


def composePrompt(prompt, mode, instructions, past_sections):

    current_section_prompt = f"""
    # {prompt}

    ```{mode}```

    ```{instructions}```
    """

    return current_section_prompt

