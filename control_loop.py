import json
import os

import requests



# load the /output/processing/lovecraft_at_the_mountains_of_madness.json
path = 'output/processing/lovecraft_at_the_mountains_of_madness.json'
endpoint = 'http://localhost:8000/generate_section'
def open_file(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

data = open_file(path)

# curl -X POST "http://localhost:8000/generate_section" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"prompt\":\"I am forced into speech because men of science have refused to followmy advice without knowing why. It is altogether against my will that Itell my reasons for opposing this contemplated invasion of the antarctic -with its vast fossil hunt and its wholesale boring and melting of the ancient ice caps. And I am the more reluctant because my warning may bein vain.",\"model\":\"llama3.1:latest, \"mode\":\"shoggoth_tweet_gen.md\"}"
def generate_section(prompt, model, mode):
    url = "http://localhost:8000/generate_section"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": prompt,
        "model": model,
        "mode": mode,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# generate a section
# loop through the data and generate a section
for i in range(len(data)):
    prompt = data[i]
    model = "llama3.1:latest"
    mode = "shoggoth_tweet_gen.md"
    response = generate_section(prompt, model, mode)
    print(response)
    # save the response to the /output/actions directory
    with open(f'output/actions/{i}.json', 'w') as f:
        json.dump(response, f)


    
