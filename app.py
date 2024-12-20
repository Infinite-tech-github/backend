from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.content_generator import contentGenerator
from services.mode_generator import modeGenerator
from services.mode_to_instructions import mode_to_instructions
from utils.save_section import save_section
import os
import json
from pathlib import Path

# Initialize the FastAPI application
app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for request validation
class Content(BaseModel):
    prompt: str
    mode: str = None
    past_sections: list = []
    instructions: str = None
    model: str
    imagePath: str = None

@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"status": "Backend is running"}

@app.get("/modes")
def get_modes():
    """
    Retrieve the list of available modes from the instructions directory.
    """
    modes_directory = Path(__file__).parent / "modes/instructions"
    if not modes_directory.exists():
        raise HTTPException(status_code=404, detail="Modes directory not found.")

    # Fetch and filter mode files
    modes = [
        file.stem for file in modes_directory.glob("*.md")
    ]

    return {"modes": modes}
    
@app.post("/generate_section")
def generate_section(content: Content):
    """
    Generate a new content section based on the provided input.
    """
    # Validate required fields
    if not content.model or not content.prompt:
        raise HTTPException(status_code=400, detail="'model' and 'prompt' are required fields.")

    provider = content.mode or settings.AI_PROVIDER

    # Generate mode get instructions if not provided
    mode = content.mode or modeGenerator(content.model, content.prompt)
    instructions = content.instructions or mode_to_instructions(mode)

    # Call the content generator service
    generated_content = contentGenerator(
        provider, content.model, content.prompt, mode, instructions, content.past_sections, content.imagePath
    )

    # Prepare the response
    response = {
        "response": generated_content[0],
        "prompt": generated_content[1],
        "mode": mode,
        "past_sections": content.past_sections,
        "model": content.model,
    }

    # Save the response data
    save_section(json.dumps(response))

    return response
