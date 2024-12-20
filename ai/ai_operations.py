# read the AI_SERVICE_URL and AI_API_KEY from the settings.py file
# import config.settings as settings
from config import settings
import requests
import json
# base64-encoded images
import base64
# resizing images
from PIL import Image
import os


# optional image
def call_ollama_ai(model, prompt, stop_sequences, imagePath=None):
    generate_url = f"{settings.OLLAMA_SERVICE_URL}/generate"
    ai_api_key = settings.OLLAMA_API_KEY
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "max_tokens": 1000,
        "stop_sequences": stop_sequences,
    }
    
    if imagePath:
        # resize and base64 encode image
        image = Image.open(imagePath)
        image = image.resize((256, 256))
        image.save(imagePath)

        with open(imagePath, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read())
            image = encoded_image.decode('utf-8')

        data["images"] = [image]

    if ai_api_key:
        headers = {
            "x-api-key": ai_api_key
        }
        request = requests.post(generate_url, json=data, headers=headers)
    else:
        request = requests.post(generate_url, json=data)
        
    response = request.json()['response']
    
    return response


def call_mistral_ai(model, prompt, stop_sequences):
    generate_url = f"{settings.MISTRAL_SERVICE_URL}/chat/completions"
    ai_api_key = settings.MISTRAL_API_KEY

    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }

    headers = { "Authorization": f"Bearer {ai_api_key}" }
    request = requests.post(generate_url, json=data, headers=headers)
    response = request.json()['choices'][0]['message']['content']
    print(response)
    return response


def call_open_ai(model, prompt, stop_sequences):
    generate_url = f"{settings.OPENAI_SERVICE_URL}/v1/engines/{model}/completions"
    ai_api_key = settings.OPENAI_API_KEY

    data = {
        "prompt": prompt,
        "max_tokens": 1000,
        "stop": stop_sequences,
    }

    headers = { "Authorization": f"Bearer {ai_api_key}" }
    request = requests.post(generate_url, json=data, headers=headers)
    response = request.json()['choices'][0]['text']
    return response


def call_ai(provider, model, prompt, stop_sequences, imagePath=None):
    if provider == "ollama":
        return call_ollama_ai(model, prompt, stop_sequences, imagePath)
    elif provider == "openai":
        return call_open_ai(model, prompt, stop_sequences)
    elif provider == "mistral":
        return call_mistral_ai(model, prompt, stop_sequences)
    else:
        return call_ollama_ai(model, prompt, stop_sequences)
