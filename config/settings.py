# import env
import os
from dotenv import load_dotenv
load_dotenv()

# ollama | mistral | openai
AI_PROVIDER = "ollama"

# Constants
INSTRUCTIONS_DIR = "./modes/instructions"
SECTION_FILE_EXT = ".md"
WORKING_FILE = "working_file.json"
SAVE_FOLDER = "generated"

OLLAMA_SERVICE_URL = "http://localhost:11434/api"
MISTRAL_SERVICE_URL = "https://api.mistral.ai/v1"
OPENAI_SERVICE_URL = "https://api.openai.com/v1"

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

AI_API_KEY = os.getenv("AI_API_KEY") # Ollama API Key