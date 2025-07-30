import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import requests


load_dotenv()

PROMPT_FILE = 'prompts/inputs.json'
ARTICLE_INSTRUCTIONS_FILE = 'prompts/article-instructions.txt'
IMAGE_INSTRUCTIONS_FILE = 'prompts/image-instructions.txt'
IMAGES_PATH = 'images/'
API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)


def get_prompt():
    with open(PROMPT_FILE, 'r') as file:
        data = json.load(file)
        return data.get('5')
    return False


def get_article_instructions():
    with open(ARTICLE_INSTRUCTIONS_FILE, 'r') as file:
        return file.read()
    return False

def get_image_instructions():
    with open('prompts/image-instructions.txt', 'r') as file:
        return file.read()
    return False


def create_article(article_header):
    prompt = get_prompt()
    prompt = f"{prompt}\n{article_header}"
    instructions = get_article_instructions()

    if not prompt or not instructions:
        print("Error: Prompt or instructions not found.")
        return False

    response = client.responses.create(
        model="gpt-4o",
        instructions=instructions,
        input=prompt,
    )
    return response.output_text


def create_image(article_title):
    instructions = get_image_instructions()

    if not instructions:
        print("Error: Image instructions not found.")
        return False

    prompt = f"{instructions}\n{article_title}"

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    print(f"Image created: {response.data[0].url}\n")
    return response.data[0].url


def download_image(image_url, filename):
    response = requests.get(image_url)

    if response.status_code == 200:
        with open(os.path.join(IMAGES_PATH, filename), 'wb') as file:
            file.write(response.content)
        print(f"Image saved as {filename}\n")
    else:
        print("Failed to download image.\n")
