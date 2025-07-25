import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROMPT_FILE = 'prompts/inputs.json'
ARTICLE_INSTRUCTIONS_FILE = 'prompts/article-instructions.txt'
API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)


def get_prompt():
    with open(PROMPT_FILE, 'r') as file:
        data = json.load(file)
        return data.get('5')
    return False


def get_instructions():
    with open(ARTICLE_INSTRUCTIONS_FILE, 'r') as file:
        return file.read()
    return False


def create_article(article_header):
    prompt = get_prompt()
    prompt = f"{prompt}\n{article_header}"
    instructions = get_instructions()

    if not prompt or not instructions:
        print("Error: Prompt or instructions not found.")
        return False
    
    response = client.responses.create(
        model="gpt-4o",
        instructions=instructions,
        input=prompt,
    )
    return response.output_text
