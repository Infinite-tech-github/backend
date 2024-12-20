from ai.ai_operations import call_ai
from utils.prompt_composer import composePrompt

def generate_content(provider, model, title, mode, instructions, past_sections, imagePath=None):
    prompt = composePrompt(title, mode, instructions, past_sections)
    stop_sequences = ["```"]

    generated_content = call_ai(provider, model, prompt, stop_sequences, imagePath)

    parsed_content = parse_content(generated_content)

    return [call_ai(provider, model, prompt, stop_sequences, imagePath),prompt]

# ``` { "mode": "document" } ```
def parse_content(content):
    # attempt to remove ```` from the start and end of the content if it exists
    if content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    
    # attempt to find the first instance of ``` and return what is in the middle
    if "```" in content:
        content = content.split("```")[1]

    return content
